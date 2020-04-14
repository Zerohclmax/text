date=['10/21','10/22','10/23','10/24','10/25','10/26','10/27']
topC=[19,22,22,23,9,11,15]
downC=[1,4,6,3,-6,1,7]
average=[]
x=topC.index(max(topC))####返回topc中最大的索引
y=downC.index(min(downC))####返回downc最小的索引
print("这一周最热一天是",date[x],"温度是：",topC[x],";","这一周最冷一天是",date[y],"温度是：",downC[y])
for i in range(0,len(date)):
    average.append((topC[i]+downC[i])/2)###求平均值
    print(date[i],"平均温度是:",average[i])

flat=0
for i in range(0,3):####一周一共3个连续5天
    for j in range(i,i+5):
        if average[j]<10:
            flat+=1
    if flat==5:
        print("沈阳已经入冬了！")
        break
if flat!=5:
    print("沈阳未入冬！")

