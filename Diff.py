x,y=map(str,input().split())
coun=0

c=len(x)
d=len(y)
if(c<d):
   for k in range(0,c):
     if(x[k]==y[k]):
        coun+=1
else:
    for l in range(0,d):
     if(x[l]==y[l]):
        coun+=1
if(c<d):
    print(d-coun)
else:
    print(c-coun)
