
class Solution:
    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
    def gcdOfStrings(self):
        sl= len(self.str1)
        if sl%2 == 0:
           slice_list = []
           for i in range(int(sl/2)):
            slice_list.append(self.str1[(i+i):(i+i+2)])
            
            for i in range(len(slice_list)-1):
             
               if slice_list[i] == slice_list[i+1]:
                
                print(slice_list[i])
                  #print("The grestest divisor is {slice_list[i]}")
                


        else:
            print("No divisor found")
            #logging.info("No divisor")
obj = Solution('ABABAB','ABAB')
obj.gcdOfStrings()
