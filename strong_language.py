#Strong language codechef
t=int(input())
while t!=0:
    n,k=[int(d) for d in input().split()]
    s=[d for d in input().strip()][:n]
    m=[0]*n
    for i in range(n):
        if s[i]=='*' and m[i]==0:
            l=i
            c=1
            while l<n and s[l]=='*':
                m[l]=c
                l+=1
                c+=1
        else:
            continue


    result=max(m)
    if result>=k:
        print("yes")
    else:
        print("no")
    t-=1
