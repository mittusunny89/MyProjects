def thedecimal(num):
    snum = str(num).split('.')
    #print(snum[1])
    if int(snum[1]) != 0:
        print(f"The decimal part is : {snum[1]}")
    else:
        print("INTEGER")
    
    


thedecimal(99.09)
thedecimal(99.00)

