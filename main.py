from fa.dfa import DFA

def clac_row(dfa: DFA, I: set):
    result = []
    alphabet = sorted(dfa.alphabet)
    for a in alphabet:
        J = dfa.get_arc_states(I, a)
        r = dfa.epsilon_closure(J)
        result.append(r)
    return result

def clac_e_table(dfa: DFA):
    result = {}
    dfa.alphabet.remove('') # 删除空元素
    I = dfa.epsilon_closure({dfa.state0})
    newrow = clac_row(dfa, I)
    result[tuple(I)] = newrow
    while newrow:
        columnvalue = []
        rows = []
        for row in newrow:
            r = clac_row(dfa, row)
            rows.extend(r)
            result[tuple(row)] = r

        for ir in rows:
            if tuple(ir) not in result:
                columnvalue.append(ir)
        newrow = columnvalue
    return result

def main():
    dfa = DFA()
    epsilon = DFA.EPSILON
    dfa.state0 = 'X'
    dfa.add_transform('X', 1, {epsilon})
    dfa.add_transform(1, 1, {'a', 'b'})
    dfa.add_transform(1, 2, {epsilon})
    dfa.add_transform(2, 5, {'a'})
    dfa.add_transform(2, 6, {'b'})
    dfa.add_transform(5, 3, {'a'})
    dfa.add_transform(6, 3, {'b'})
    dfa.add_transform(3, 4, {epsilon})
    dfa.add_transform(4, 4, {'a', 'b'})
    dfa.add_transform(4, 'Y', {epsilon})
    dfa.finals.add('Y')
    print(dfa.to_mermaid_code())
    I = dfa.epsilon_closure({'X'})
    print(I)
    J_a = dfa.get_arc_states(I, 'a')
    J_b = dfa.get_arc_states(I, 'b')
    I_a = dfa.epsilon_closure(J_a)
    I_b = dfa.epsilon_closure(J_b)
    print(I_a, I_b)
    r = clac_e_table(dfa)
    print(r)


if __name__ == '__main__':
    main()
