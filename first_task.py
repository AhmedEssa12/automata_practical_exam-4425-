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
