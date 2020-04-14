amount=[]##规格
listShop={}##购物车
List=[]
print("请输入包装名字，规格数量，价格。输入‘y’继续输入，‘n’结束")
j='y'
while(j=='y'):
    x=input("包装：")
    y=int(input("规格："))
    z=int(input("价格："))
    listShop[x] = z
    amount.append(z/y)
    j=input("是否继续输入(y/n)")
j=0
for i in listShop.keys():
    print(i,"单价是",amount[j])
    List.append(i)
    j+=1
x=min(amount)
y=amount.index(x)
print("建议购买",List[y],"单价是：",amount[y])
