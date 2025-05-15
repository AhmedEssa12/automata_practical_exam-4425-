def  DFA_divided(Bin_Str):

   state = 0 

   for char in Bin_Str:
    if char =='1':

        state = (state + 1) % 3
    elif char =='0':

        pass
    else:

        return "Invalid input"

   if state == 0:
      return "Accepted"
   else:
      return "Rejected"   
