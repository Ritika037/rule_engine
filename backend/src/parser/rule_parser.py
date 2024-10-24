from ..models.node import Node, NodeType, Operator

class RuleParser:
    def __init__(self):
        self.tokens = []
        self.current = 0
    
    def tokenize(self, rule_string: str) -> list:
        tokens = []
        current = ""
        i = 0
        
        while i < len(rule_string):
            char = rule_string[i]
            
            if char.isspace():
                if current:
                    tokens.append(current)
                    current = ""
                i += 1
                continue
                
            if char in "()=><":
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
                i += 1
                continue
                
            current += char
            i += 1
            
        if current:
            tokens.append(current)
            
        return tokens

    def parse(self, rule_string: str) -> Node:
        self.tokens = self.tokenize(rule_string)
        self.current = 0
        return self.parse_expression()
    
    def parse_expression(self) -> Node:
        # Implementation from previous code
        pass