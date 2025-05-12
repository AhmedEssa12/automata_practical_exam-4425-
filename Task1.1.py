def  DFA_divided(Bin_Str):

   state = 0 

   for char in Bin_Str:
    if char =='1':
        #Move to the next state (add 1)
        state = (state + 1) % 3
    elif char =='0':
        #No change in status
        pass
    else:
        #If the number is not 0 or 1, it returns an error.
        return "Invalid input"

   if state == 0:
      return "Accepted"
   else:
      return "Rejected"   
   
   
print(DFA_divided("1101"))
print(DFA_divided("1001"))
print(DFA_divided("1011"))
print(DFA_divided("0001"))
print(DFA_divided("1000"))
print(DFA_divided("110010010101"))
print(DFA_divided("11000000000000001111"))
print(DFA_divided("1100"))
print(DFA_divided("12000"))
        
