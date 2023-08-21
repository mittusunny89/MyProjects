'''
Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
def dict_concat(*dic):
    dickeys = []
    dicvalues = []
    for dic in dic: #iterate through each dictionary
        for key in dic.keys():#iterate through keys in a dictionary
            dickeys.append(key)
        for value in dic.values():
            dicvalues.append(value)

    res_dic = {}
    i=0
    for key in dickeys:
        res_dic[key] = dicvalues[i]
        i+=1
    print(res_dic)

dic1={'a':10, 2:20}
dic2={'b':30, 4:40}
dic3={5:50,6:60}
dic4={"mittu": "ajith", "qw": 123, 23: "asd"}
dict_concat(dic1,dic2,dic3,dic4)



