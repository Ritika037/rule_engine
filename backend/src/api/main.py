from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from ..engine.rule_engine import RuleEngine
from ..models.database import Rule, AttributeCatalog, RuleEvaluation
from sqlalchemy.orm import Session
from .database import get_db

app = FastAPI()
rule_engine = RuleEngine()

class RuleCreate(BaseModel):
    name: str
    rule_string: str

class RuleEvaluateRequest(BaseModel):
    data: Dict[str, Any]

@app.post("/rules")
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    try:
        # Validate rule by parsing
        rule_engine.create_rule(rule.rule_string)
        
        db_rule = Rule(
            name=rule.name,
            rule_string=rule.rule_string
        )
        db.add(db_rule)
        db.commit()
        db.refresh(db_rule)
        
        return db_rule
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rules/{rule_id}/evaluate")
def evaluate_rule(rule_id: int, request: RuleEvaluateRequest, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    
    try:
        ast = rule_engine.create_rule(rule.rule_string)
        result = rule_engine.evaluate_rule(ast, request.data)
        
        # Log evaluation
        evaluation = RuleEvaluation(
            rule_id=rule_id,
            input_data=request.data,
            result=result
        )
        db.add(evaluation)
        db.commit()
        
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rules/combine")
def combine_rules(rule_ids: List[int], db: Session = Depends(get_db)):
    rules = db.query(Rule).filter(Rule.id.in_(rule_ids)).all()
    if len(rules) != len(rule_ids):
        raise HTTPException(status_code=404, detail="One or more rules not found")
    
    try:
        rule_strings = [rule.rule_string for rule in rules]
        combined_ast = rule_engine.combine_rules(rule_strings)
        return {"combined_rule_string": str(combined_ast)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

