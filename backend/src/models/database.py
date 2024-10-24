from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rules'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    rule_string = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class AttributeCatalog(Base):
    __tablename__ = 'attribute_catalog'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    data_type = Column(String(50), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())

class RuleEvaluation(Base):
    __tablename__ = 'rule_evaluations'
    
    id = Column(Integer, primary_key=True)
    rule_id = Column(Integer, nullable=False)
    input_data = Column(JSON, nullable=False)
    result = Column(Boolean, nullable=False)
    evaluated_at = Column(DateTime, default=func.now())