from typing import Set, Tuple
from grammar.common import Grammar
from util.comm import EPSILON

class ContextFreeGrammar(Grammar):
    def __init__(self) -> None:
        super().__init__()


# 用一个生成式替换另外一组生成式
def replace_production_first_by_one(source_productions: Tuple[str], target_productions, append=None) -> Tuple[str]:
    production = list(target_productions)
    source_len = len(source_productions)
    for i in range(1, source_len):
        production.append(source_productions[i])
    return tuple(production)


# 用一个生成式替换另外一组生成式
def replace_productions_first(grammar: ContextFreeGrammar, source_productions: set, target: str) -> Set[Tuple[str]]:
    productions = set()
    for source_p in source_productions:
        if source_p[0] != target:
            productions.add(source_p)
            continue
        
        for target_p in grammar.productions[target]:
            replace_p = list(target_p)
            for i in range(1, len(source_p)): replace_p.append(source_p[i])
            productions.add(replace_p)

    return productions

# 消除直接左递归
def eliminate_immediate_left_recursive(grammar: ContextFreeGrammar, source):
    '''
    A --> Aa1 | Aa2 | ... | Aan | e1 | e2 | ... | en
    -- 消除 --
    A  --> e1A' | e2A' | ... | enA'
    A' --> a1A' | a2A' | ... | anA' | 空
    '''
    source_productions = grammar.productions[source]
    group_immediate_left_recursive = [] # 包含直接左递归的组
    group_not_left_recursive = []       # 不包含直接左递归的组
    for source_p in source_productions:
        if source_p[0] != source:
            group_immediate_left_recursive.append(source_p)
        else:
            group_not_left_recursive.append(source_p)
    if not group_immediate_left_recursive: return grammar
    productions_a = []
    productions_b = []
    new_nontermial = f"{source}'"
    while new_nontermial not in grammar.nonterminals: new_nontermial += "'"
    
    grammar.nonterminals.add(new_nontermial)
    for beta in group_not_left_recursive:
        production = list(beta)
        production.append(new_nontermial)
        productions_a.append(production)

    for left in group_immediate_left_recursive:
        production = [left[i] for i in range(1, len(left))]
        production.append(new_nontermial)
        productions_b.append(production)
    productions_b.append((EPSILON))
    grammar[source] = productions_a
    grammar[new_nontermial] = productions_b
    return grammar

# 消除左递归
def eliminate_left_recursion(grammar: ContextFreeGrammar) -> ContextFreeGrammar:
    keys = list(grammar.productions.keys())
    for i in range(len(keys)):
        source = keys[i]
        source_productions = grammar.productions[source]
        for j in range(0, i):
            target = keys[j]
            # 将每个形如Pi -> Pja的产生式用 Pj替换
            source_productions = replace_productions_first(grammar, source_productions, target)
        

# 消除回溯
def eliminate_backtracking(grammar: ContextFreeGrammar) -> ContextFreeGrammar:
    pass