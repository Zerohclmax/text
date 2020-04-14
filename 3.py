print("请输入带千分位逗号(可多个)，结束请输入‘0’:")
Lists=[]
while(1):
    i=input()
    if i=='0':
        break
    Lists.append(i)
for x in Lists:###分离每一个数字
    List2=[]
    List1=list(x)####分离每一个数中数字
    for i in List1:
        if i!=',':
            List2.append(i)
    List2=x=''.join(List2)
    print("去千分位逗号是：", x)
