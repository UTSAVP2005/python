import random
lst_odd=[0,0,0,0,0]
lst_even=[0,0,0,0]
lst_new=[0,0,0,0,0,0,0,0]
for i in range(0,5):
    lst_odd[i]=(random.randint(1,100))*2+1
print(lst_odd)
for i in range(0,4):
    lst_even[i]=(random.randint(1,100))*2
print(lst_even)
for j in range(0,2):
    lst_new[j]=lst_odd[j]
    j=j+1
i=0
for j in range(2,6):
    lst_new[j]=lst_even[i]
    i+=1
k=3    
for j in range(6,8):
    lst_new[j]=lst_odd[k]
    k+=1
print(lst_new)
