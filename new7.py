s=int(input())
b=[]
for j in range(0,s):  
    c=input()
    b.append(c)
list=[]
for j in zip(*b):
    if j.count(j[0])==len(j): 
        list.append(j[0])
    else:
        break
print(''.join(list))
