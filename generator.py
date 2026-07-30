



def Weekday():
    d=['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
    i=0
    n=7
    while i <n:
        yield d[i]
        i+=1
    

day= Weekday()
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))