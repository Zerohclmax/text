grade=[]
x=input("请输入评分（用‘，’分开）：")
for i in x.split(','):###分开字符串中数字
    i=int(i)
    grade.append(i)
if len(grade)<3:
    print("成绩无效！")
grade=sorted(grade)###对评分排序
grade.pop(0)###删除最小值
grade.pop(len(grade)-1)####删除最大值
aver=sum(grade)/len(grade)###求平均值

if aver%1!=0:####对分数取整
    aver=aver//1
    aver+=1
print("成绩是：",aver)
if aver>90:
    print("优秀")
elif aver<90 and aver>60:
    print("及格")
else:
    print("不及格")