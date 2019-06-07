sb=int(input())
l=[int(i) for i in input().split()]
s=0
for i in range(sb):
	for j in range(i):
		if l[j]<l[i]:
			s+=l[j]
print(s)
