#WAP to reverse the words in a string sentense

def rev_string(str):
    lst = str.split()
    rev_lst = []
    for i in range(len(lst)):
        rev_lst.append(lst[-1-i])
    rev_str = " ".join(rev_lst)
    print(rev_str)

def reverse(str):
    lst = str.split()
    rev_lst = lst[::-1]
    rev_str = " ".join(rev_lst)
    print(rev_str)


str = "oru kili pattu moolave"
reverse(str)