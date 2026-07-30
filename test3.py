
#check if list is palindrome
L1=[1,2,3,3,2,1]
print("list L1;",L1)


L2=L1[::-1]
print("reversed L2",L2)
if(L1 ==L2):
    print("its palindrome list:")
else:
    print("not palindrome")