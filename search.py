n=input('enter array limit')
n=int(n)
a=[]
for i in range(0,n):
    num=int(input('enter numbers in array'))
    a.append(num)
print("numbers=",a)
x=int(input("enter number to search"))
if x in a:
    print("found")
else:
    print("not found")
