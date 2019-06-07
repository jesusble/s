limit=int(input())
value=input().split()
sum=0
for i in range(len(limit)):
	sum=sum+int(value[i])
	avg=sum/limit
print(avg)
