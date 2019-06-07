s=int(input())
b=input().split()
k=0
for i in range(len(b)):
    k=int(b[i])+k
h=k//s
print(abs(h))
