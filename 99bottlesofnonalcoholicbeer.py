#99 Bottles of (Non-Alcoholic) Beer On The Wall in the least number of characters possible.
# Attempt 1: 357 characters
x=99
c="bottles of (Non-Alcoholic) beer"
while(x!="no more"):
    if (x==1):
        b=b.replace("s","")
    else:
        b=c
    o="on the wall,"
    print(x,b,o,x,b+".","\nTake one down and pass it around, ",end="")
    x-=1
    o=o.replace(",",".")
    if (x==1):
        b=b.replace("s","")
    if (x==0):
        b=c
        x = "no more"
    print(x,b,o)