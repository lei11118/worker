from collections import defaultdict
from sqlalchemy.orm import Session
from models import WrongRecord, Question, KnowledgePoint, Subject


# 客观难度 → base_weight 映射
DIFFICULTY_WEIGHT = {
    '基础': 5.0,
    '中档': 3.0,
    '压轴': 1.0,
}


def get_frequency_bonus(count: int) -> float:
    """同一知识点错误次数对应的加成系数"""
    if count <= 1:
        return 1.0
    elif count == 2:
        return 1.3
    elif count == 3:
        return 1.6
    else:
        return 2.0


def compute_weights(session: Session, subject_id: int) -> list[dict]:
    """计算指定学科下各知识点的权重，返回按权重降序排列的结果列表"""
    # 获取该学科所有错题记录
    records = (
        session.query(WrongRecord)
        .join(Question)
        .filter(Question.subject_id == subject_id)
        .all()
    )

    if not records:
        return []

    subject = session.query(Subject).filter_by(id=subject_id).first()
    # 计算该科每题平均分，用于归一化
    questions = session.query(Question).filter_by(subject_id=subject_id).all()
    avg_score = sum(q.base_score for q in questions) / len(questions) if questions else 1.0

    # 统计每个知识点的错误次数（用于 frequency_bonus）
    kp_error_count = defaultdict(int)
    for r in records:
        kp_error_count[r.knowledge_point_id] += 1

    # 每条记录赋予一个 event_order（按时间排序后的序号），用于 frequency count 逐个计算
    kp_records = defaultdict(list)
    for r in records:
        kp_records[r.knowledge_point_id].append(r)
    for kp_id in kp_records:
        kp_records[kp_id].sort(key=lambda r: r.created_at)

    # 累积每个知识点的权重
    kp_weight = defaultdict(float)
    kp_details = defaultdict(list)

    for kp_id, recs in kp_records.items():
        kp = session.query(KnowledgePoint).filter_by(id=kp_id).first()
        for idx, r in enumerate(recs):
            q = session.query(Question).filter_by(id=r.question_id).first()
            # base_weight
            bw = DIFFICULTY_WEIGHT.get(q.difficulty, 3.0)
            # user_factor
            uf = 6 - r.user_difficulty
            # score_factor
            sf = q.base_score / avg_score
            # frequency_bonus: 计算到这一条记录时，该知识点已经出现的次数
            fb = get_frequency_bonus(idx + 1)

            single_weight = bw * uf * sf * fb
            kp_weight[kp_id] += single_weight
            kp_details[kp_id].append({
                'question_number': q.question_number,
                'section_type': q.section_type,
                'difficulty': q.difficulty,
                'base_score': q.base_score,
                'user_difficulty': r.user_difficulty,
                'single_weight': round(single_weight, 2),
            })

    # 聚合每个知识点的最终结果
    results = []
    for kp_id, total_weight in kp_weight.items():
        kp = session.query(KnowledgePoint).filter_by(id=kp_id).first()
        difficulties = [d['difficulty'] for d in kp_details[kp_id]]
        base_count = sum(1 for d in difficulties if d == '基础')
        mid_count = sum(1 for d in difficulties if d == '中档')
        hard_count = sum(1 for d in difficulties if d == '压轴')

        results.append({
            'kp_id': kp_id,
            'kp_name': f'{kp.category} — {kp.name}',
            'category': kp.category,
            'total_weight': round(total_weight, 2),
            'error_count': len(kp_details[kp_id]),
            'base_errors': base_count,
            'mid_errors': mid_count,
            'hard_errors': hard_count,
        })

    results.sort(key=lambda x: x['total_weight'], reverse=True)

    # 分配优先级
    if results:
        avg_weight = sum(r['total_weight'] for r in results) / len(results)
        for r in results:
            if r['total_weight'] > avg_weight * 2:
                r['priority'] = '极高'
                r['priority_class'] = 'danger'
            elif r['total_weight'] > avg_weight:
                r['priority'] = '高'
                r['priority_class'] = 'warning'
            elif r['total_weight'] > avg_weight * 0.5:
                r['priority'] = '中'
                r['priority_class'] = 'info'
            else:
                r['priority'] = '低'
                r['priority_class'] = 'success'

    return results
