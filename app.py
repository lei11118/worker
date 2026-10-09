from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, Subject, Question, KnowledgePoint, WrongRecord
from weight_engine import compute_weights
from seed_data import seed_all

app = Flask(__name__)
engine = create_engine('sqlite:///wrong_questions.db', echo=False)


@app.before_request
def init_db():
    """首次请求时初始化数据库表结构和种子数据"""
    Base.metadata.create_all(bind=engine)
    with Session(engine) as s:
        seed_all(s)


def get_session():
    return Session(engine)


# ==================== 路由 ====================

@app.route('/')
def index():
    """首页仪表盘"""
    with get_session() as s:
        subjects = s.query(Subject).all()
        # 汇总每科统计
        stats = []
        for subj in subjects:
            total_wrong = (
                s.query(WrongRecord)
                .join(Question)
                .filter(Question.subject_id == subj.id)
                .count()
            )
            # 高优先级知识点数
            weights = compute_weights(s, subj.id)
            high_count = sum(1 for w in weights if w['priority'] in ('极高', '高'))
            stats.append({
                'subject': subj,
                'total_wrong': total_wrong,
                'high_priority_count': high_count,
            })
        return render_template('index.html', stats=stats)


@app.route('/record', methods=['GET', 'POST'])
def record():
    """录入错题"""
    with get_session() as s:
        if request.method == 'POST':
            question_id = int(request.form['question_id'])
            knowledge_point_id = int(request.form['knowledge_point_id'])
            user_difficulty = int(request.form['user_difficulty'])
            notes = request.form.get('notes', '')

            record = WrongRecord(
                question_id=question_id,
                knowledge_point_id=knowledge_point_id,
                user_difficulty=user_difficulty,
                notes=notes,
            )
            s.add(record)
            s.commit()
            # 重定向到 GET，显示刚刚提交的信息 + 可继续录入
            return redirect(url_for('record', success='1'))

        subjects = s.query(Subject).all()
        return render_template('record.html', subjects=subjects)


@app.route('/api/questions/<int:subject_id>')
def api_questions(subject_id):
    """AJAX: 根据学科返回题号列表"""
    with get_session() as s:
        questions = (
            s.query(Question)
            .filter_by(subject_id=subject_id)
            .order_by(Question.question_number)
            .all()
        )
        return jsonify([{
            'id': q.id,
            'question_number': q.question_number,
            'section_type': q.section_type,
            'base_score': q.base_score,
            'difficulty': q.difficulty,
            'typical_knowledge': q.typical_knowledge,
        } for q in questions])


@app.route('/api/knowledge_points/<int:subject_id>')
def api_knowledge_points(subject_id):
    """AJAX: 根据学科返回考点列表"""
    with get_session() as s:
        kps = (
            s.query(KnowledgePoint)
            .filter_by(subject_id=subject_id)
            .order_by(KnowledgePoint.category, KnowledgePoint.name)
            .all()
        )
        return jsonify([{
            'id': kp.id,
            'category': kp.category,
            'name': kp.name,
        } for kp in kps])


@app.route('/analysis')
@app.route('/analysis/<int:subject_id>')
def analysis(subject_id=None):
    """权重分析页"""
    with get_session() as s:
        subjects = s.query(Subject).all()
        if subject_id is None:
            subject_id = subjects[0].id if subjects else 1

        current_subject = s.query(Subject).filter_by(id=subject_id).first()
        weights = compute_weights(s, subject_id)

        return render_template(
            'analysis.html',
            subjects=subjects,
            current_subject=current_subject,
            weights=weights,
            subject_id=subject_id,
        )


@app.route('/history')
def history():
    """错题历史页"""
    with get_session() as s:
        subject_id = request.args.get('subject_id', type=int)
        records_query = (
            s.query(WrongRecord)
            .order_by(WrongRecord.created_at.desc())
        )
        if subject_id:
            records_query = records_query.join(Question).filter(Question.subject_id == subject_id)

        records = records_query.all()
        subjects = s.query(Subject).all()

        # 预加载关联数据
        result = []
        for r in records:
            q = s.query(Question).filter_by(id=r.question_id).first()
            subj = s.query(Subject).filter_by(id=q.subject_id).first()
            kp = s.query(KnowledgePoint).filter_by(id=r.knowledge_point_id).first()
            result.append({
                'id': r.id,
                'subject_name': subj.name,
                'question_number': q.question_number,
                'section_type': q.section_type,
                'difficulty': q.difficulty,
                'base_score': q.base_score,
                'kp_name': f'{kp.category} — {kp.name}',
                'user_difficulty': r.user_difficulty,
                'created_at': r.created_at.strftime('%Y-%m-%d %H:%M'),
                'notes': r.notes,
            })

        return render_template(
            'history.html',
            records=result,
            subjects=subjects,
            subject_id=subject_id,
        )


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete_record(record_id):
    """删除一条错题记录"""
    with get_session() as s:
        record = s.query(WrongRecord).filter_by(id=record_id).first()
        if record:
            s.delete(record)
            s.commit()
    return redirect(url_for('history'))


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
