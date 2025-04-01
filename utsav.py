"""def func():
    print("this is func function")
def disp():
    print("this is print function")
def msg():
    print("this is msg function")
    
lst=[func,disp,msg]
for i in lst:
   i()   

lst1=[1,2,3 ,4,5,6]
lst2=[6,5,4,3,2,1]
lst3=[]
for i in range (0,6):
    lst3.append(lst1[i]+lst2[i])
print(lst3)
""
import random
lst1=[]
lst2=[]
for i in range(0,10):
    lst1.append(random.randint(-15,15))
print(lst1)    

for i in range(0,10):
    lst2.append(lst1[i]**2)
print(lst2)
"""

lst=['madam','python','malayalam',12321]
def ispalindrome(string):
    if(string==string[::-1]):
        print("palindrome")
    else:
        print("not palindrome")
for i in lst:
    string3=str(i)
    ispalindrome(string3)
    


