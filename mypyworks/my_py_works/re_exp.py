import re

'''
#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

#mystring = "asxsac 14  dsdcs90 ^^kcknsn  ** hjj"
mystring = "audbsjvbjh 64d4dsb   "
def check_alphnum(my_str):
    alphanum= re.findall("[a-zA-Z0-9\s+]", my_str)
    nonalpha = [text for text in mystring if text not in  alphanum]
    if len(nonalpha) == 0:
        print("The string contains only aphanum ")
    else:
        print("The string have other characters")

check_alphnum(mystring)


#Write a Python program that matches a string that has an a followed by zero or more b's.

mystring = "ascsb sdds anjnm asdb"
x= re.findall("^a(b*)$",mystring)
print(x)

# Write a Python program that matches a string that has an a followed by one or more b's.

mystring = "ascsb sdds abnjnm asd"
x= re.findall("^a.+b",mystring)
match = re.search("ab+",mystring)
#y = match.group()
print(f"the findings are {x}")
print(f'the matches are {match}')


#Create a regex that finds dates in the format MM/DD/YY or MM/DD/YYYY and returns just the year part.
mystring = "my date of birth is 19/04/2013"
#x = re.search(r"\d{2}/\d{2}/(\d{2}|\d{4})",mystring)
x = re.match(r"\d{2}/\d{2}/(\d{2}|\d{4})",mystring)
print(x)


# Write a Python program to find the substrings within a string.
mystring="'Python exercises, PHP exercises, C# exercises'"
re.findall("exercises", mystring)
'''

#Write a Python program to match if two words from a list of words start with the letter 'P'
mylist = ['panama','apple','pineapple','orange','grape']
counter = 0
for i in range(len(mylist)):
    if mylist[i][0] == 'p':
        counter += 1
if counter == 2:
    print("The word contain  two words starting with p")


