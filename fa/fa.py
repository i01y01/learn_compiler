from util.comm import EPSILON
class FA:
    EPSILON = EPSILON
    def __init__(self) -> None:
        self.states = set()     # S
        self.alphabet = set()   # ∑
        self.transfer = set()   # δ
        self.state0 = 0         # s0 start state
        self.finals = set()     # 
        self.table  = {}        # translation table
        self.curstate = self.state0
    
    def _make_table_key(self, s, c):
        if c == FA.EPSILON: return f'{s}'
        return f'{s},{c}'

    def _check(self, c):
        if c not in self.alphabet:
            raise Exception("c not in alphabet")
        k = self._make_table_key(self.curstate, k)
        if k not in self.table:
            raise Exception(f"can't found transfer function {k}")
        return k
    
    def start(self):            # start work
        self.curstate = self.state0

    def move(self, c): pass           # transfer function

    @property
    def is_finish(self):
        '''Determine whether the current state is the final state'''
        return self.curstate in self.finals
    