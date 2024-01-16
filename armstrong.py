n=int(input("enter the number and check its armstrong or not"))
t=n
z=n
s=0
c=0
while(n!=0):
    r=n%10
    c=c+1
    n=n//10

while(t!=0):
    r=t%10
    s=s+r**c
    t=t//10

if(s==z):
    print("its an armstrong number")
else:
    print("its not armstrong number")