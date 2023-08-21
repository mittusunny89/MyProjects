'''Write a regex so that the full email addresses are extracted.
i.e.: mike@protonmail.com
str='The advancements in biomarine studies franky@google.com with the investments necessary and
         Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
'''

import re

#Write a regex so that the full email addresses are extracted.
def extract_email():
    str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
    emails = re.findall(r'\w+@\w+.com\b',str)
    print(emails)
extract_email()

#write a regex to get only the part of the email before the "@" sign and include the @ sign
def extract_at():
    str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
    print(re.findall(r"\w+@\b",str))
extract_at()

#write a regex to get only the part of the email before the "@" sign and exclude the @ sign

def exclude_at():
    str='The advancements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
    print(re.findall(r"(\w+)@\b",str))
    
exclude_at()