import re
def rev_string(str):
    my_string = str
    my_string.strip()
    re.sub('\s+', ' ',my_string)
    new_string = my_string.split()
    rev_list = new_string[::-1]
    rev_string = " ".join(rev_list)
    print(rev_string)
    

rev_string("  ne    poooodaa koranga    ")