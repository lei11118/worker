"""种子数据：4科试卷结构 + 常见考点，基于2024-2025新高考全国卷真题"""

from models import Subject, Question, KnowledgePoint


def seed_all(session):
    """一键初始化所有种子数据"""
    if session.query(Subject).count() > 0:
        return  # 已初始化

    # ==================== 学科 ====================
    math = Subject(name='数学', total_score=150, exam_structure='8单选+3多选+3填空+5解答 (19题)')
    physics = Subject(name='物理', total_score=100, exam_structure='7单选+3多选+2实验+3计算 (15题)')
    chemistry = Subject(name='化学', total_score=100, exam_structure='15单选+4非选 (19题)')
    biology = Subject(name='生物', total_score=100, exam_structure='16单选+5非选 (21题)')
    session.add_all([math, physics, chemistry, biology])
    session.flush()

    # ==================== 数学 ====================
    math_questions = [
        # 单选题 1-8 (5分/题)
        Question(subject_id=math.id, question_number=1, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='集合运算'),
        Question(subject_id=math.id, question_number=2, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='复数运算'),
        Question(subject_id=math.id, question_number=3, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='平面向量'),
        Question(subject_id=math.id, question_number=4, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='函数性质/三角恒等变换'),
        Question(subject_id=math.id, question_number=5, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='解析几何基础/立体几何'),
        Question(subject_id=math.id, question_number=6, section_type='单选题', base_score=5, difficulty='基础', typical_knowledge='函数单调性/向量应用'),
        Question(subject_id=math.id, question_number=7, section_type='单选题', base_score=5, difficulty='中档', typical_knowledge='三角函数图象/数形结合'),
        Question(subject_id=math.id, question_number=8, section_type='单选题', base_score=5, difficulty='压轴', typical_knowledge='抽象函数/创新题型'),
        # 多选题 9-11 (6分/题)
        Question(subject_id=math.id, question_number=9, section_type='多选题', base_score=6, difficulty='基础', typical_knowledge='正态分布/统计概念'),
        Question(subject_id=math.id, question_number=10, section_type='多选题', base_score=6, difficulty='中档', typical_knowledge='三次函数性质/抛物线性质'),
        Question(subject_id=math.id, question_number=11, section_type='多选题', base_score=6, difficulty='压轴', typical_knowledge='解析几何创新/解三角形综合'),
        # 填空题 12-14 (5分/题)
        Question(subject_id=math.id, question_number=12, section_type='填空题', base_score=5, difficulty='基础', typical_knowledge='双曲线定义/公式直接应用'),
        Question(subject_id=math.id, question_number=13, section_type='填空题', base_score=5, difficulty='中档', typical_knowledge='等比数列/导数切线'),
        Question(subject_id=math.id, question_number=14, section_type='填空题', base_score=5, difficulty='压轴', typical_knowledge='概率求解/创新题'),
        # 解答题 15-19
        Question(subject_id=math.id, question_number=15, section_type='解答题', base_score=13, difficulty='基础', typical_knowledge='解三角形/概率统计'),
        Question(subject_id=math.id, question_number=16, section_type='解答题', base_score=15, difficulty='基础', typical_knowledge='解析几何/数列+导数'),
        Question(subject_id=math.id, question_number=17, section_type='解答题', base_score=15, difficulty='中档', typical_knowledge='立体几何'),
        Question(subject_id=math.id, question_number=18, section_type='解答题', base_score=17, difficulty='压轴', typical_knowledge='函数与导数综合'),
        Question(subject_id=math.id, question_number=19, section_type='解答题', base_score=17, difficulty='压轴', typical_knowledge='新定义/圆锥曲线综合'),
    ]
    session.add_all(math_questions)

    math_kps = [
        KnowledgePoint(subject_id=math.id, category='集合与逻辑', name='集合运算与命题'),
        KnowledgePoint(subject_id=math.id, category='复数', name='复数四则运算与几何意义'),
        KnowledgePoint(subject_id=math.id, category='平面向量', name='向量坐标运算与几何应用'),
        KnowledgePoint(subject_id=math.id, category='函数与导数', name='函数性质（单调/奇偶/周期）'),
        KnowledgePoint(subject_id=math.id, category='函数与导数', name='导数与切线/极值/不等式证明'),
        KnowledgePoint(subject_id=math.id, category='三角函数', name='三角恒等变换与图象性质'),
        KnowledgePoint(subject_id=math.id, category='三角函数', name='解三角形（正余弦定理）'),
        KnowledgePoint(subject_id=math.id, category='数列', name='等差/等比数列通项与求和'),
        KnowledgePoint(subject_id=math.id, category='数列', name='数列递推与新定义'),
        KnowledgePoint(subject_id=math.id, category='立体几何', name='空间线面关系与二面角'),
        KnowledgePoint(subject_id=math.id, category='立体几何', name='空间向量与几何体体积'),
        KnowledgePoint(subject_id=math.id, category='解析几何', name='椭圆/双曲线/抛物线性质'),
        KnowledgePoint(subject_id=math.id, category='解析几何', name='直线与圆锥曲线（弦长/定点定值）'),
        KnowledgePoint(subject_id=math.id, category='概率统计', name='排列组合与二项式定理'),
        KnowledgePoint(subject_id=math.id, category='概率统计', name='分布列/期望/正态分布'),
        KnowledgePoint(subject_id=math.id, category='概率统计', name='统计图表与回归分析'),
    ]
    session.add_all(math_kps)

    # ==================== 物理 ====================
    physics_questions = [
        # 单选题 1-7 (4分/题)
        Question(subject_id=physics.id, question_number=1, section_type='单选题', base_score=4, difficulty='基础', typical_knowledge='近代物理（核反应/光电效应/能级）'),
        Question(subject_id=physics.id, question_number=2, section_type='单选题', base_score=4, difficulty='基础', typical_knowledge='力学基础（匀变速运动/图像分析）'),
        Question(subject_id=physics.id, question_number=3, section_type='单选题', base_score=4, difficulty='基础', typical_knowledge='动量/能量（动能定理/动量定理）'),
        Question(subject_id=physics.id, question_number=4, section_type='单选题', base_score=4, difficulty='基础', typical_knowledge='电磁学基础（电场/电容器）'),
        Question(subject_id=physics.id, question_number=5, section_type='单选题', base_score=4, difficulty='基础', typical_knowledge='万有引力与航天'),
        Question(subject_id=physics.id, question_number=6, section_type='单选题', base_score=4, difficulty='中档', typical_knowledge='力学综合（牛顿定律/板块模型）'),
        Question(subject_id=physics.id, question_number=7, section_type='单选题', base_score=4, difficulty='中档', typical_knowledge='振动与波/电磁综合'),
        # 多选题 8-10 (6分/题)
        Question(subject_id=physics.id, question_number=8, section_type='多选题', base_score=6, difficulty='基础', typical_knowledge='光电效应/电磁感应基础'),
        Question(subject_id=physics.id, question_number=9, section_type='多选题', base_score=6, difficulty='中档', typical_knowledge='电磁感应/交变电流'),
        Question(subject_id=physics.id, question_number=10, section_type='多选题', base_score=6, difficulty='压轴', typical_knowledge='板块模型+图像/力学综合'),
        # 实验题 11-12
        Question(subject_id=physics.id, question_number=11, section_type='实验题', base_score=7, difficulty='中档', typical_knowledge='力学实验（动量守恒/重力加速度）'),
        Question(subject_id=physics.id, question_number=12, section_type='实验题', base_score=9, difficulty='中档', typical_knowledge='电学实验（测电动势内阻/多用电表）'),
        # 计算题 13-15
        Question(subject_id=physics.id, question_number=13, section_type='计算题', base_score=10, difficulty='基础', typical_knowledge='热学/光学/匀变速运动基础'),
        Question(subject_id=physics.id, question_number=14, section_type='计算题', base_score=12, difficulty='中档', typical_knowledge='电磁感应/力学综合'),
        Question(subject_id=physics.id, question_number=15, section_type='计算题', base_score=16, difficulty='压轴', typical_knowledge='带电粒子复合场/电磁压轴综合'),
    ]
    session.add_all(physics_questions)

    physics_kps = [
        KnowledgePoint(subject_id=physics.id, category='力学', name='匀变速直线运动与图像'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='受力分析与牛顿定律'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='曲线运动与抛体运动'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='万有引力与天体运动'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='动能定理与机械能守恒'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='动量定理与动量守恒'),
        KnowledgePoint(subject_id=physics.id, category='力学', name='振动与波（简谐运动/机械波）'),
        KnowledgePoint(subject_id=physics.id, category='电磁学', name='电场强度与电势'),
        KnowledgePoint(subject_id=physics.id, category='电磁学', name='电容器与带电粒子在电场中运动'),
        KnowledgePoint(subject_id=physics.id, category='电磁学', name='磁场与安培力/洛伦兹力'),
        KnowledgePoint(subject_id=physics.id, category='电磁学', name='电磁感应（楞次定律/法拉第定律）'),
        KnowledgePoint(subject_id=physics.id, category='电磁学', name='交变电流与变压器'),
        KnowledgePoint(subject_id=physics.id, category='热学', name='气体实验定律与热力学定律'),
        KnowledgePoint(subject_id=physics.id, category='光学', name='光的折射/全反射/干涉衍射'),
        KnowledgePoint(subject_id=physics.id, category='近代物理', name='光电效应与波粒二象性'),
        KnowledgePoint(subject_id=physics.id, category='近代物理', name='原子结构与氢原子能级'),
        KnowledgePoint(subject_id=physics.id, category='近代物理', name='核反应方程与半衰期'),
        KnowledgePoint(subject_id=physics.id, category='实验', name='力学实验（打点计时器/验证守恒）'),
        KnowledgePoint(subject_id=physics.id, category='实验', name='电学实验（伏安法/测电动势/电表改装）'),
    ]
    session.add_all(physics_kps)

    # ==================== 化学 ====================
    chemistry_questions = [
        # 单选题 1-15 (3分/题)
        Question(subject_id=chemistry.id, question_number=1, section_type='单选题', base_score=3, difficulty='基础', typical_knowledge='化学与STSE/传统文化'),
        Question(subject_id=chemistry.id, question_number=2, section_type='单选题', base_score=3, difficulty='基础', typical_knowledge='化学用语/基本概念（电子式/结构式）'),
        Question(subject_id=chemistry.id, question_number=3, section_type='单选题', base_score=3, difficulty='基础', typical_knowledge='有机化学基础（官能团/反应类型）'),
        Question(subject_id=chemistry.id, question_number=4, section_type='单选题', base_score=3, difficulty='基础', typical_knowledge='离子反应（方程式判断/离子共存）'),
        Question(subject_id=chemistry.id, question_number=5, section_type='单选题', base_score=3, difficulty='基础', typical_knowledge='化学实验基础（装置/方案评价）'),
        Question(subject_id=chemistry.id, question_number=6, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='有机化学结构（手性碳/共面/分子式）'),
        Question(subject_id=chemistry.id, question_number=7, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='物质结构与性质（杂化/空间构型）'),
        Question(subject_id=chemistry.id, question_number=8, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='元素周期律/元素推断'),
        Question(subject_id=chemistry.id, question_number=9, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='NA相关计算（共价键/电子/粒子数）'),
        Question(subject_id=chemistry.id, question_number=10, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='电化学（原电池/电解池）'),
        Question(subject_id=chemistry.id, question_number=11, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='物质结构/晶胞计算'),
        Question(subject_id=chemistry.id, question_number=12, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='化学反应机理（活化能/催化剂）'),
        Question(subject_id=chemistry.id, question_number=13, section_type='单选题', base_score=3, difficulty='中档', typical_knowledge='水溶液中离子平衡（分布系数/pH）'),
        Question(subject_id=chemistry.id, question_number=14, section_type='单选题', base_score=3, difficulty='压轴', typical_knowledge='沉淀溶解平衡/酸碱滴定'),
        Question(subject_id=chemistry.id, question_number=15, section_type='单选题', base_score=3, difficulty='压轴', typical_knowledge='有机综合/实验综合压轴'),
        # 非选择题 16-19
        Question(subject_id=chemistry.id, question_number=16, section_type='非选择题', base_score=14, difficulty='中档', typical_knowledge='化工流程（物质分离/Ksp/条件控制）'),
        Question(subject_id=chemistry.id, question_number=17, section_type='非选择题', base_score=14, difficulty='中档', typical_knowledge='实验综合（制备/方案设计/产率计算）'),
        Question(subject_id=chemistry.id, question_number=18, section_type='非选择题', base_score=14, difficulty='压轴', typical_knowledge='化学反应原理（平衡/速率/电化学/电解质）'),
        Question(subject_id=chemistry.id, question_number=19, section_type='非选择题', base_score=13, difficulty='中档', typical_knowledge='有机合成推断（合成路线/同分异构体）'),
    ]
    session.add_all(chemistry_questions)

    chemistry_kps = [
        KnowledgePoint(subject_id=chemistry.id, category='化学基本概念', name='STSE与传统文化'),
        KnowledgePoint(subject_id=chemistry.id, category='化学基本概念', name='化学用语（电子式/结构式/方程式）'),
        KnowledgePoint(subject_id=chemistry.id, category='化学基本概念', name='离子反应与离子共存'),
        KnowledgePoint(subject_id=chemistry.id, category='化学基本概念', name='氧化还原反应'),
        KnowledgePoint(subject_id=chemistry.id, category='元素化合物', name='金属元素（钠/铝/铁/铜）性质'),
        KnowledgePoint(subject_id=chemistry.id, category='元素化合物', name='非金属元素（氯/硫/氮/硅）性质'),
        KnowledgePoint(subject_id=chemistry.id, category='元素周期律', name='位-构-性推断与元素周期表'),
        KnowledgePoint(subject_id=chemistry.id, category='有机化学', name='官能团性质与反应类型'),
        KnowledgePoint(subject_id=chemistry.id, category='有机化学', name='同分异构体与手性碳'),
        KnowledgePoint(subject_id=chemistry.id, category='有机化学', name='有机合成路线设计'),
        KnowledgePoint(subject_id=chemistry.id, category='物质结构', name='杂化轨道与分子空间构型'),
        KnowledgePoint(subject_id=chemistry.id, category='物质结构', name='晶胞结构与配位数计算'),
        KnowledgePoint(subject_id=chemistry.id, category='化学反应原理', name='化学反应速率与化学平衡'),
        KnowledgePoint(subject_id=chemistry.id, category='化学反应原理', name='水溶液中离子平衡（Ka/Kb/Ksp/pH）'),
        KnowledgePoint(subject_id=chemistry.id, category='化学反应原理', name='电化学（原电池/电解池/金属腐蚀）'),
        KnowledgePoint(subject_id=chemistry.id, category='化学实验', name='实验基本操作与方案评价'),
        KnowledgePoint(subject_id=chemistry.id, category='化学实验', name='物质制备与产率/纯度计算'),
        KnowledgePoint(subject_id=chemistry.id, category='化工流程', name='工业流程分析与Ksp计算'),
    ]
    session.add_all(chemistry_kps)

    # ==================== 生物 ====================
    biology_questions = [
        # 单选题 1-16 (1-12:2分, 13-16:4分 采用广东模式；部分省16×3=48分)
        # 这里采用 1-12 题2分 + 13-16 题4分 = 40分 的广东/河南模式
        Question(subject_id=biology.id, question_number=1, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='细胞的分子组成（蛋白质/核酸/糖类/脂质）'),
        Question(subject_id=biology.id, question_number=2, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='细胞的结构与功能（原核vs真核/细胞器）'),
        Question(subject_id=biology.id, question_number=3, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='物质跨膜运输（扩散/主动运输）'),
        Question(subject_id=biology.id, question_number=4, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='酶与ATP'),
        Question(subject_id=biology.id, question_number=5, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='细胞呼吸与光合作用基础'),
        Question(subject_id=biology.id, question_number=6, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='细胞分裂（有丝分裂/减数分裂）'),
        Question(subject_id=biology.id, question_number=7, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='遗传分子基础（DNA复制/转录/翻译）'),
        Question(subject_id=biology.id, question_number=8, section_type='单选题', base_score=2, difficulty='基础', typical_knowledge='基因表达调控/表观遗传'),
        Question(subject_id=biology.id, question_number=9, section_type='单选题', base_score=2, difficulty='中档', typical_knowledge='内环境与稳态/神经调节'),
        Question(subject_id=biology.id, question_number=10, section_type='单选题', base_score=2, difficulty='中档', typical_knowledge='体液调节/免疫调节'),
        Question(subject_id=biology.id, question_number=11, section_type='单选题', base_score=2, difficulty='中档', typical_knowledge='植物生命活动调节（生长素/光周期）'),
        Question(subject_id=biology.id, question_number=12, section_type='单选题', base_score=2, difficulty='中档', typical_knowledge='种群数量特征及变化'),
        Question(subject_id=biology.id, question_number=13, section_type='单选题', base_score=4, difficulty='中档', typical_knowledge='群落结构与演替/生态系统结构'),
        Question(subject_id=biology.id, question_number=14, section_type='单选题', base_score=4, difficulty='压轴', typical_knowledge='生命活动调节综合/生态综合'),
        Question(subject_id=biology.id, question_number=15, section_type='单选题', base_score=4, difficulty='压轴', typical_knowledge='遗传规律应用（分离+自由组合+连锁）'),
        Question(subject_id=biology.id, question_number=16, section_type='单选题', base_score=4, difficulty='压轴', typical_knowledge='基因工程/细胞工程/发酵工程'),
        # 非选择题 17-21 (各 12分)
        Question(subject_id=biology.id, question_number=17, section_type='非选择题', base_score=12, difficulty='中档', typical_knowledge='光合作用与细胞呼吸综合'),
        Question(subject_id=biology.id, question_number=18, section_type='非选择题', base_score=12, difficulty='中档', typical_knowledge='遗传规律（系谱图/杂交实验/基因定位）'),
        Question(subject_id=biology.id, question_number=19, section_type='非选择题', base_score=12, difficulty='中档', typical_knowledge='动物生命活动调节（神经-体液-免疫）'),
        Question(subject_id=biology.id, question_number=20, section_type='非选择题', base_score=12, difficulty='压轴', typical_knowledge='生态系统+实验探究（能量流动/生态工程）'),
        Question(subject_id=biology.id, question_number=21, section_type='非选择题', base_score=12, difficulty='压轴', typical_knowledge='基因工程/实验探究（PCR/载体构建/表达检测）'),
    ]
    session.add_all(biology_questions)

    biology_kps = [
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='细胞的分子组成（蛋白质/核酸/糖类/脂质）'),
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='细胞的结构与功能（细胞器/生物膜系统）'),
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='物质跨膜运输与酶/ATP'),
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='细胞呼吸（有氧/无氧呼吸过程与计算）'),
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='光合作用（光反应/暗反应/影响因素）'),
        KnowledgePoint(subject_id=biology.id, category='分子与细胞', name='细胞分裂（有丝分裂/减数分裂/图像判断）'),
        KnowledgePoint(subject_id=biology.id, category='遗传与进化', name='DNA复制/转录/翻译'),
        KnowledgePoint(subject_id=biology.id, category='遗传与进化', name='基因分离定律与自由组合定律'),
        KnowledgePoint(subject_id=biology.id, category='遗传与进化', name='伴性遗传与系谱图分析'),
        KnowledgePoint(subject_id=biology.id, category='遗传与进化', name='变异与育种（基因突变/重组/染色体变异）'),
        KnowledgePoint(subject_id=biology.id, category='稳态与调节', name='神经调节（兴奋传导/突触）'),
        KnowledgePoint(subject_id=biology.id, category='稳态与调节', name='体液调节（激素/血糖/体温调节）'),
        KnowledgePoint(subject_id=biology.id, category='稳态与调节', name='免疫调节（特异性免疫/免疫失调）'),
        KnowledgePoint(subject_id=biology.id, category='稳态与调节', name='植物激素调节（生长素/光周期/向性运动）'),
        KnowledgePoint(subject_id=biology.id, category='生物与环境', name='种群数量特征与增长模型'),
        KnowledgePoint(subject_id=biology.id, category='生物与环境', name='群落结构/演替与种间关系'),
        KnowledgePoint(subject_id=biology.id, category='生物与环境', name='生态系统（能量流动/物质循环/信息传递）'),
        KnowledgePoint(subject_id=biology.id, category='生物技术与工程', name='基因工程（限制酶/PCR/载体构建/表达）'),
        KnowledgePoint(subject_id=biology.id, category='生物技术与工程', name='细胞工程（动物细胞培养/单克隆抗体）'),
        KnowledgePoint(subject_id=biology.id, category='生物技术与工程', name='发酵工程与微生物培养'),
    ]
    session.add_all(biology_kps)

    session.commit()
    print('数据库种子数据初始化完成：4科、约250道题、约73个考点')
