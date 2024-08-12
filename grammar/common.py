


from typing import Dict, Set, Tuple


class Grammar:
    def __init__(self) -> None:
        self.terminals: Set[str]    = set()   # 终结符
        self.nonterminals: Set[str] = set()   # 非终结符
        self.start_symbol: str      = ''      # 开始符号
        self.productions: Dict[str, Set[Tuple[str]]] = {}       # 产生式 P: {(A,a), (B, b)}
    