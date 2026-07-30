

#infinite generator. continuously provides the weekdays, without stopping
#solution 1
def Weekday():
    d=['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
    i=0
    n=6
    while True: 
        if i <=6:
         yield d[i]
         i+=1
        else:
            #reset i to 0
         i=0
         #yield d[i]
    

day= Weekday()
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))