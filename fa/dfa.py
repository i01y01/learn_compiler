from fa.fa import FA

class DFA(FA):
    def __init__(self) -> None:
        super().__init__()
    
    def move(self, c):
        k = self._check(c)
        self.curstate = self.table[k]
    
    def add_transform(self, state, tstate, alphabets: set):
        if len(alphabets) == 0: return
        self.states.add(state)
        self.states.add(tstate)
        self.alphabet.update(alphabets)
        for s in alphabets:
            key = self._make_table_key(state,s)
            self.table[key] = tstate
    
    def epsilon_closure(self, I: set):
        result = set(I)
        newset = I
        while newset:
            J = self.get_arc_states(newset, FA.EPSILON)
            newset = J - result
            result.update(newset)
        return result
    
    def get_arc_states(self, I: set, alphabet):
        '''
        A set of states from some state of I to an arc of alphabet.
        '''
        result = set()
        for i in I:
            key = self._make_table_key(i, alphabet)
            
            if key in self.table:
                tstate = self.table[key]
                result.add(tstate)
        return result
    
    def to_mermaid_code(self):
        codes = ['stateDiagram-v2']
        states = self.states
        alphabets = set(self.alphabet)
        alphabets.add(FA.EPSILON)
        alphabets = sorted(alphabets)
        for s in states:
            for a in alphabets:
                k = self._make_table_key(s, a)
                if k not in self.table: continue
                t = self.table[k]
                if s in self.finals:
                    s = f'[{s}]'
                if t in self.finals:
                    t = f'[{t}]'
                
                if a == FA.EPSILON:
                    a = 'ε'
                
                c = f'    {s} --> {t} : {a}'
                codes.append(c)
        return '\n'.join(codes)