n,a,b,c=map(int,input().split())
s=a+b+c
days=(n//s)*3
rem=n%s
if rem!=0:
 if rem<=a:
    days+=1
 elif a<rem<=(a+b):
    days+=2
 else:
    days+=3
print(days)