# pda_simulator.py

def PDA_simulate(string):
    stack = []

    i = 0
    while i < len(string) and string[i] == 'a':
        stack.append('A')
        i += 1

    while i < len(string) and string[i] == 'b':
        if not stack:
            return False 
        stack.pop()
        i += 1

    return i == len(string) and not stack
