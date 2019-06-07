w=int(input())
x=input().split()
y=[]
for i in range(0,w):
  if(int(x[i])==i):
    y.append(x[i])
if(y==[]):
  print("-1")
else:
  y.sort()
  for j in range(0,len(y)):
    print(y[j],end=" ")
