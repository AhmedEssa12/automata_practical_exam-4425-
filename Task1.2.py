def PDA_simulate(string):
    stack = []

    i = 0
    while i < len(string) and string[i] == 'a':
        stack.append('A')
        i += 1

    while i < len(string) and string[i] =='b' :
        if not stack:
            return False 
        stack.pop()
        i += 1
    if i == len(string) and not stack:
        return True
    else:
        return False
        
test_cases = ["","ab","aabb","aaabbb","aab","abb","aaaaaabbbbbb"]


for test in test_cases:
    result = PDA_simulate(test)
    print(f"{test:10} -> {'Accepted' if result else 'Rejected'}")