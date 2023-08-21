import re
'''
treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396, "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436, "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109, "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
#Type your answer here.

def moretrees(dict):
    val_list = []
    for item in treepersqkm.keys():
        if treepersqkm[item] > 20000:
            val_list.append(item)

    print(val_list)




#moretrees(treepersqkm)

#Write a function named "count_l" that counts the number of words that contain the letter: "l" in a given string.
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three farthings, Say the bells of St. Martin's"

def count_l(a):
    lst = str.split()
    counter =0
    for item in lst:
        if 'l' in item:
            counter +=1

    print(counter)
#count_l(str)          

#Write a function to 7-e which returns the number of words that start with letter "A" in a string. (Make sure it counts lower case a's as well.).
str = "Oranges and lemons, Say Anitha the bells of St. Clement's. You Annowe me three farthings, Say the bells of St. Martin's"
    
def count_l(a):
    lst = str.split()
    alist = []
    for item in lst:
        if (re.match(r"^(a|A)", item)):
            alist.append(item)
       
    print(len(alist))
#count_l(str)

'''
lst=[10, 99,100, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13,  80, 95]

my_message=""

i =0
while i < len(lst):
    if lst[i] == 100:
        my_message = "There is 100 at index no: " + str(i)
    
    i+=1

print(my_message)