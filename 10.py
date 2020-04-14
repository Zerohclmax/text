n=int(input("矩阵阶数:"))
a_list=[[]for i in range(n)]###创建n个二维空列表
for i in range(n):
    line=input("请输入方阵（用‘，’分开）：").split(',')###将数据分开
    if len(line)!=n:
        print("输入错误!")
        break
    for j in range(n):
        a_list[i].append(line[j])
flat=0
print("a_list:",a_list)
for i in range(0,n):
    c_list=[]
    b_list=a_list[i]
    x=b_list.index(max(b_list))###取出每行的最大数索引
    for j in range(0,n):
        c_list.append(a_list[j][x])####取出行最大数所在的列
    if b_list[x]==min(c_list):
        print("鞍点:",b_list[x])
        flat=1
if flat==0:
    print("鞍点不存在")

