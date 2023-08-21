class Solution():   
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
          
    def merge_alternately(self):
        new_word  = '' 
        i = 0
        
        if len(self.word1) <= len(self.word2):
            for i in range(len(self.word1)):
                new_word += self.word1[i] + self.word2[i]    
                i +=1
                print(i)
            new_word += self.word2[i:] 
        else:
            for i in range(len(self.word2)):
                new_word += self.word1[i] + self.word2[i]    
                i +=1
                print(i)
            new_word += self.word1[i:]
        print(new_word)
obj = Solution('sunny','MITTU')
obj.merge_alternately()