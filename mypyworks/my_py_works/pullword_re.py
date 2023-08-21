#Find the words with exactly 8 letters using regex.
import re

def find_8char():
    str="Au pays parfume que le soleil caresse, J'ai connu, sous un dais d'arbres tout empourpres Et de palmiers d'ou pleut sur les yeux la paresse, Une dame creole aux charmes ignores."
    print(re.findall(r"\w{8}",str))

#find_8char()

#Find the numbers starting with 212
def find_num():
    str='''Ancient Script 21299: The Takenouchi documents are the ancient historical records that have been secretly preserved and passed down from generation to generation by the Takenouchi family, the head of family being the chief priest of the Koso Kotai Jingu shrine. 212-111-5932 '''
    print(re.findall(r"212\S+",str))

#find_num()

'''You are given stock prices for related financial tickers. (Symbols representing companies in the stock market)

Find a way to extract the tickers mentioned in the report.
i.e.: TSLA, NFLX ...'''

def find_ticker():
    str="""Some of the prices were as following TSLA:749.50, ORCL: 50.50, GE: 10.90, MSFT: 170.50, BIDU: 121.40. As the macroeconomic developments continue we will update the prices. """
    print(re.findall("[(A-Z)]{4}",str))
#find_ticker()

#Find the html tags that are more than 4 letters.

#Html tags can be found inside <> characters and closing html tags can be found in the same format after / character. </>

def find_html():
    
    str="""<div class="tut-list tut-list-new tut-row "> <div class="tut-list-primary"> <div class="tut-vote"> <video>intro</video> <span class="count">50</span> <span class="tut-upvotes-text hidden">Upvotes</span> </a> </div>  <center>k="11" rel="nofollow"></center><span class="tutorial-title-txt">Automate the Boring Stuff with Python</span> <span class="tut-title-link">  <span class="js-tutorial" data-id="3529" title="Automate the Boring Stuff with Python" target="_blank">(udemy.com)</span>  </sp<form class="save-tutorial-form" method="post" <button></button> <closeform></closeform></form>"""
    print(re.findall(r"<(\w{5,})>",str))
    print(re.findall(r'</([a-z]{5,})>', str))
#find_html()

#Loop through the list and apply regex to each element so that only items ending with semicolon (;) are matched.

def find_semi():
    str=["js/prettify-full.en.js 4e6ee9163220","js/moderator.en.js:", "transaction no: 75553942;", "", "transaction no: 75551263;", "transaction no: 46553942;", "c01c47765ca21b82b08b90403b4c7af3886098683e3869ad1:", "transaction no: 75554942;"]
    for i in range(len(str)):
        if re.findall(r"(.+;)$",str[i]):
            print(str[i])

find_semi()