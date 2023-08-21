#WAP to find max and min number in a list

def find_max(lst):
    max = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > max:
            max = lst[i]
    print(f"The maximum number is {max}")
def find_min(lst):
    min= lst[0]
    for i in range(1,len(lst)):
        if lst[i] < min:
            min = lst[i]
    print(f"The maximum number is {min}")

lst = [12,5,36,115,2,9,74]
find_max(lst)
find_min(lst)