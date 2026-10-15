
#removing duplicates from a list using set function
print('*'*20)
print('solution 1:')
L1=[3,5,7,9,3,6,5,2,3,7]
print(L1)
#S1=set()
#print('Type of S1: ',type(S1))
#converting list into set.. a set cannot hold duplicates. the moment u convert
# a list to set,it drops the duplicates.
S1= set(L1)
#converting the output back to List.
L2=list(S1)
print('printing Option 1 solution:') 
print(L2)

#option2:
print('*'*20)
print('solution 2:')

L1=[3,5,7,9,3,6,5,2,3,7]
print(L1)
L2=[]
for x in L1:
    if x in L2:
        #skip
        print('item present')
    else:
        L2.append(x)    
print('printing Option 2 solution:')   
print(L2)

#option 3:
print('*'*20)
print('solution 3:')

L1=[3,5,7,9,3,6,5,2,3,7]
print(L1)
L2=[]
for x in L1:
    if x not in L2:
        L2.append(x)          
    else:
        #skip
        print('item present')
          
print('printing Option 3 solution:')
print(L2)

#option 4:
print('*'*20)
print('solution 4:')

L1=[3,5,7,9,3,6,5,2,3,7]
print(L1)
L2=[]
#using list comprehension
[L2.append(x) for x in L1 if x not in L2]
          
print('printing Option 4 solution:')
print(L2)
#Added comment to this line
#adding more lines

        
