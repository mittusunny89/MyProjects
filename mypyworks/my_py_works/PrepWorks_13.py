# Write a Python program to count the frequency of words in a file.
import re
def count_word(fname,word):
    with open(fname, 'r+') as fs:
        mytxt = fs.read()
    
    wordlst = re.findall(word,mytxt)
    print(f"There are {len(wordlst)} times of {word} in this file")

count_word(r"C:\git\MyProjects\mypyworks\my_py_works\Valayoosai.txt", 'Kala')