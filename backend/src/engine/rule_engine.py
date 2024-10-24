from typing import Dict, Any, List
from ..models.node import Node, NodeType, Operator
from ..parser.rule_parser import RuleParser

class RuleEngine:
    def __init__(self):
        self.parser = RuleParser()
    
    def create_rule(self, rule_string: str) -> Node:
        try:
            return self.parser.parse(rule_string)
        except Exception as e:
            raise ValueError(f"Invalid rule string: {str(e)}")
    
    def combine_rules(self, rules: List[str]) -> Node:
        if not rules:
            raise ValueError("No rules provided")
            
        if len(rules) == 1:
            return self.create_rule(rules[0])
        
        nodes = [self.create_rule(rule) for rule in rules]
        
        while len(nodes) > 1:
            new_nodes = []
            for i in range(0, len(nodes), 2):
                if i + 1 < len(nodes):
                    new_nodes.append(Node(
                        type=NodeType.OPERATOR,
                        operator=Operator.AND,
                        left=nodes[i],
                        right=nodes[i + 1]
                    ))
                else:
                    new_nodes.append(nodes[i])
            nodes = new_nodes
            
        return nodes[0]
    
    def evaluate_rule(self, node: Node, data: Dict[str, Any]) -> bool:
        # Implementation from previous code
        pass