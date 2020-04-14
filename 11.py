#######1#########
#######递归#######
def Func(n):
    if n==1:
        return 1
    else:
        return n*Func(n-1)####递归
#######非递归######
def Func1(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
########2#######

e,n=1,1
while(1/Func(n)>=1e-6):
    e+=1/Func(n)
    n+=1
print("e=",e)
