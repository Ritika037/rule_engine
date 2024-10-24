from dataclasses import dataclass
from typing import Optional, Union
from enum import Enum

class NodeType(Enum):
    OPERATOR = "operator"
    OPERAND = "operand"
    COMPARISON = "comparison"

class Operator(Enum):
    AND = "AND"
    OR = "OR"
    GT = ">"
    LT = "<"
    EQ = "="
    GTE = ">="
    LTE = "<="

@dataclass
class Node:
    type: NodeType
    value: Optional[Union[str, int, float]] = None
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    operator: Optional[Operator] = None