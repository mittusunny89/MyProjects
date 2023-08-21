#WAP to return true if any 3 consecutive numbers in a list is in increasing order. example [4,9,5,6,7,2,0,1]

#slice the list with 3 numbers 
def cons_num(lst):
    flag = 0
   
    for i in range(len(lst)-3):
        
        slc = lst[i:(i+3)]
        if (slc[1] - slc[0]) == 1 and (slc[2]-slc[1]==1): #check the diffreence between num2 num1
            flag = 1
    if flag == 1: #return true if the difference is 1
        return True
    else:
        return False
    
lst = [4,9,5,0,7,2,3,4,0,1]
print(cons_num(lst))