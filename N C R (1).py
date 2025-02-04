print("enter 2 numbers")
a=int(input())
b=int(input())
f=a-b
c=1
for i in range(1,a+1):
    c=c*i

d=1
for i in range(1,b+1):
    d=d*i

e=1
for i in range(1,f+1):
    e=e*i

g=d*e
print("answer is ",c/g)


