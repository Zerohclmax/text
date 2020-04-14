x=int(input("请输入1000以内的正整数："))
print(x,end="=")
for i in range(2,x+1):
    if(i==x):
        print(i)
        break
    while(x%i==0):
        if (i==x):
            print(i)
            break
        x /= i
        print(i, end="*")