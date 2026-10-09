from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    total_score = Column(Integer, nullable=False)
    exam_structure = Column(String(200))

    questions = relationship('Question', backref='subject', lazy=True)
    knowledge_points = relationship('KnowledgePoint', backref='subject', lazy=True)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    question_number = Column(Integer, nullable=False)
    section_type = Column(String(20), nullable=False)  # 单选题/多选题/填空题/解答题/实验题/非选择题
    base_score = Column(Float, nullable=False)
    difficulty = Column(String(10), nullable=False)  # 基础/中档/压轴
    typical_knowledge = Column(String(100))

    wrong_records = relationship('WrongRecord', backref='question', lazy=True)


class KnowledgePoint(Base):
    __tablename__ = 'knowledge_points'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    category = Column(String(50), nullable=False)  # 大类
    name = Column(String(100), nullable=False)  # 具体考点名

    wrong_records = relationship('WrongRecord', backref='knowledge_point', lazy=True)


class WrongRecord(Base):
    __tablename__ = 'wrong_records'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    knowledge_point_id = Column(Integer, ForeignKey('knowledge_points.id'), nullable=False)
    user_difficulty = Column(Integer, nullable=False)  # 1-5
    created_at = Column(DateTime, default=datetime.datetime.now)
    notes = Column(Text, default='')
