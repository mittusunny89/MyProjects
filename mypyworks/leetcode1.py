#merge string alternatevely

class Solution():
    
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
             
    def mergeAlternately(self):
        newword = ''
        j = 0
        for i in range (len(self.word1)):
            newword = newword+ self.word1[i]
            if j < len(self.word2):
                newword = newword+ self.word2[j]
                j +=1

        print(newword + self.word2[ len(self.word1):]+self.word1[ len(self.word2):])
obj = Solution('mittuajith','MITTUAJ')
obj.mergeAlternately()