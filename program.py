b=int(input())
sb=input().split()
for i in sb:
    if sb.count(i)==1:
        print(i)
        break
