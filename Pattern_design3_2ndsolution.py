#Note: this is the simplest solution wiht just 1 for loop.
#all other solutions need 2 loops.!!
for i in range(5,0,-1):
    if(i<5):
        print(' '*(5-i), end='')
        print('*'* (i))
    else:
        print('*'*i)