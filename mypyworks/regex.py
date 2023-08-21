import re
mystr = '***   00  the mskv scdjds - kn   klmjsnv **'
sstr = mystr.strip('*')

newstr = re.sub('\s+',' ',sstr)

sestr = re.search("^the",mystr)
print(sestr)

myString = "This is a string with some words"
#myPattern = r"\bwith\b" # a word boundary followed by ‘with’ followed by another word boundary 
myPattern = r" is"
myMatch = re.sub(myPattern,'**', myString) 
print(myMatch)
#if myMatch: 
#   print(myMatch.group()) # prints ‘with’ else: print(“No match”)