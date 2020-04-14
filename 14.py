x=input("输入一个字符串，(用空格分隔)：")
a=[]
for i in x.split():
    a.append(i)
print("单词个数是：",len(a))