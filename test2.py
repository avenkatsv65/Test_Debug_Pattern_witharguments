
#rotating a list by defined count
L1=[1,2,3,4,5,6]

#rotate by 1
n=1
opsL1=L1[0:1]
#opsL1.pop
print('extracted items of slice:',opsL1)
sL1 =L1[1:]
print('remaining items of slice:',sL1)
#sL1.append(str(opsL1))
fList =sL1+opsL1
print('final items of slice:',fList)

#solution2:

print('*'*20)
print('solution 2:')
L1=[1,2,3,4,5,6]
#rotate by 1
#n=2
n= int(input('Enter the rotation count: '))
opsL1=L1[0:n]
print('extracted items of slice:',opsL1)
sL1 =L1[n:]
print('remaining items of slice:',sL1)
#fList =sL1+opsL1
#modifies the original ist in place
sL1.extend(opsL1)
print('final items of slice:',sL1)
