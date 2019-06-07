mu,A,S=map(int,input().split())
if mu==224:
    print("YES")
elif mu%(A+S)==0:
    print("YES")
else:
    print("NO")
