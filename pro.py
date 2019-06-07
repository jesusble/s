b=int(input())
sb=str(b)
q=0
for i in range(0,len(sb)):
    if int(sb[i:i+2])<26 and len(str(int(sb[i:i+2])))==2:
        q+=1
if q==2:
    print(q+q//2)
else:
    print(q+q//2+1)
