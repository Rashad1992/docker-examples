n = int(input ("please enter any positive number"))
if n<0:
    print('Error:Number must be postive')
else:
    sum=0
    i=n
    while i>0:
        sum +=i
        i -=1
    print('sum of all positive number till', n ,'is', sum)
        