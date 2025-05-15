def simulate_turing_machine(input_string):
    tape = list(input_string) + ['_']  
    head = 0
    state = 'q0'

    while True:
        symbol = tape[head]

        if state == 'q0':
            if symbol == '0':
                tape[head] = 'X'
                state = 'q1_0'
                head += 1
            elif symbol == '1':
                tape[head] = 'Y'
                state = 'q1_1'
                head += 1
            elif symbol in ['x', 'y']:
                head += 1
            elif symbol == '_':
                return True  
            else:
                return False  

        elif state == 'q1_0':
            if symbol in ['0', '1', 'X', 'Y', 'x', 'y']:
                head += 1
            elif symbol == '0':
                tape[head] = 'x'
                state = 'q2'
                head -= 1
            elif symbol == '_':
                return False

        elif state == 'q1_1':
            if symbol in ['0', '1', 'X', 'Y', 'x', 'y']:
                head += 1
            elif symbol == '1':
                tape[head] = 'y'
                state = 'q2'
                head -= 1
            elif symbol == '_':
                return False

        elif state == 'q2':
            if tape[head] in ['x', 'y', '0', '1']:
                head -= 1
            elif tape[head] in ['X', 'Y']:
                head += 1
                state = 'q0'

        else:
            return False



test_cases = ["", "00", "01", "0011", "0101", "00110011", "0110", "010"]
for s in test_cases:
    result = simulate_turing_machine(s)
    print(f"{s:10} -> {'Accepted' if result else 'Rejected'}")
