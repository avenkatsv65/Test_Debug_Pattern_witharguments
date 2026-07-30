

#infinite generator. continuously provides the weekdays, without stopping
#solution 2

def Weekday():
    d=['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
    i=0
    while True: 
         yield d[i]
         #after reaching end of list, it should start from beginning automatically
         #so doing mod 7 
         i=(i+1) % 7
    

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