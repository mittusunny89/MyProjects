#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]




def is_anagram(word1,word2):
    if  sorted(word1) == sorted(word2):
        return True
    else:
        return False
   
def get_words(list):
    
    for i in range(len(strs)-1): #0,1,2,3,4
        ana_word = []
        word1 = strs[i]
        for j in range(i+1,len(strs)):#1,2,3,4,5
            word2 = strs[j]
            if len(ana_lst) != 0:
                if is_anagram(word1,word2) and  word1 not in ana_lst[-1] :
                    ana_word += [strs[i],strs[j]]
            else:
                if is_anagram(word1,word2):
                    ana_word += [strs[i],strs[j]]       
                 
            
        ana_lst.append(set(ana_word))
        
        
    print(ana_lst)

ana_lst = []                              
strs = ["eat","tea","tan","ate","nat","bat"]
# sortedlist = []
get_words(strs)
