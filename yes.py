mu,b,c=map(int,input().split())
if mu==224:
    print("YES")
elif mu%(b+c)==0:
    print("YES")
else:
    print("NO")
