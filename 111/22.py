import matplotlib.pyplot as plt

class stu_inform:######学生信息类
    def __init__(self):####构造方法，初始学号,班级,姓名列表
        self.stu_number=[]
        self.stu_class=[]
        self.stu_name=[]
    def add_number(self,List):###增加方法
        self.stu_number.append(List[0])
        self.stu_class.append(List[1])
        self.stu_name.append(List[2])
    def del_number(self,number):###删除方法
        x=self.stu_number.index(number)
        self.stu_number.pop(x)
        self.stu_class.pop(x)
        self.stu_name.pop(x)
    def look_number(self,number):###查看方法
        x=self.stu_number.index(number)
        List=[self.stu_number[x],self.stu_class[x],self.stu_name[x]]
        return List
    def get_dict(self):###用字典储存,返回学生信息
        dict={}
        for i in range(0,len(self.stu_number)):
            dict[self.stu_number[i]]=(self.stu_class[i],self.stu_name[i])
        return dict
class cla_inform:###课程信息类
    def __init__(self):####构造方法,初始化课程号,课程名,学分列表
        self.cla_number=[]
        self.cla_name=[]
        self.cla_score=[]
    def add_number(self,List):###增加课程方法
        self.cla_number.append(List[0])
        self.cla_name.append(List[1])
        self.cla_score.append(List[2])
    def del_number(self,number):###删除课程方法
        x = self.cla_number.index(number)
        self.cla_number.pop(x)
        self.cla_name.pop(x)
        self.cla_score.pop(x)
    def look_number(self,number):####查看课程方法
        x = self.cla_number.index(number)
        List = [self.cla_number[x], self.cla_name[x], self.cla_score[x]]
        return List
    def get_dict(self):###用字典储存,返回课程信息
        dict={}
        for i in range(0,len(self.cla_number)):
            dict[self.cla_number[i]]=(self.cla_name[i],self.cla_score[i])
        return dict
class cho_inform:####stunumber,clanumber,score
    def __init__(self):####构造方法，初始化学号,课程号,成绩列表
        self.cho_stunumber=[]
        self.cho_clanumber=[]
        self.cho_score=[]
    def add_number(self,List):###增加选课方法
        self.cho_stunumber.append(List[0])
        self.cho_clanumber.append(List[1])
        self.cho_score.append(List[2])
    def cha_number(self,List):###改变选课方法
        x=0
        for i in self.cho_stunumber:
            if i==List[0] and self.cho_clanumber[x]==List[1]:
                self.cho_score[x]=List[2]
            x+=1
    def look_number(self,List):###查看选课方法
        for i in range(0,len(self.cho_stunumber)):
            if List[0]==self.cho_stunumber[i] and List[1]==self.cho_clanumber[i]:
                score=self.cho_score[i]
                return score
    def get_dict(self):###用字典储存,返回选课信息
        dict={}
        for i in range(0,len(self.cho_stunumber)):
            dict[i+1]=(self.cho_stunumber[i],self.cho_clanumber[i],self.cho_score[i])
        return dict
class sco_approach:###成绩统计类
    def __init__(self):###实例化选课类,班级类
        self.choice = cho_inform()
        self.name = cla_inform()
    def cla_approach(self):###各科成绩平均分，及格率，统计图
        self.List=list(set(self.choice.cho_clanumber))
        List1=self.name.cla_number
        List2=self.name.cla_name
        x,z,self.claname=[],[],[]
        k,m,q=0,0,0
        dict1={}
        for i in range(0,len(self.List)):
            x.append(0)
            z.append(0)
            self.claname.append(0)
        dic=dict.fromkeys(self.List,0)
        for i in List1:
            self.claname[self.List.index(i)]=List2[q]
            q+=1
        for j in self.choice.cho_clanumber:
            y=self.List.index(j)
            x[y]+=1
            dic[j]+=self.choice.cho_score[k]
            if self.choice.cho_score[k]>=60:
                z[y]+=1
            k+=1
        k=0
        for l in self.List:
            dic[l]/=x[k]
            k+=1
        k=0
        for f in self.List:
            dict1[f]=z[k]/x[k]
            k+=1
        k=0
        dict2={}######将平均分课程号换成课程名
        for i in dic.values():
            dict2[self.claname[k]]=i
            k+=1
        k=0
        dict3={}####将及格率课程号换成课程名
        for i in dict1.values():
            dict3[self.claname[k]]=i
            k+=1
        ######统计图#####
        name_list=list(dict2.keys())
        num_list =list(dict2.values())
        plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
        plt.show()
        return dict2,dict3######dict2：平均分；dict3：及格率
    def stu_approach(self,number):####学生各成绩
        dic1=dict.fromkeys(self.List,0)
        k=0
        for i in self.choice.cho_stunumber:
            if number==i:
                dic1[self.choice.cho_clanumber[k]]=self.choice.cho_score[k]
            k+=1
        k = 0
        dic = {}
        for i in dic1.values():
            dic[self.claname[k]] = i
            k += 1
        score=0
        for i in dic.keys():
            x=self.name.cla_name.index(i)
            if dic[i]>=60:
                score+=self.name.cla_score[x]
        dic["学分"]=score
        return dic
def main():
    print('''          学生信息处理          课程信息处理          选课信息处理           成绩统计
        1.录入学生信息        4.录入课程信息        7.录入选课信息        10.各科平均分，及格率
        2.删除学生信息        5.删除课程信息        8.修改选课信息        11.学生各科成绩
        3.查询学生信息        6.查询课程信息        9.查询选课信息''')
    x=int(input("请输入执行命令："))
    stuinform=stu_inform()####实例化学生信息类
    clainform=cla_inform()####实例化课程信息类
    choinform=cho_inform()####实例化选课信息类
    scoapproach=sco_approach()###实例化成绩统计类
    while(1):
        if x==1:###录入学生信息
            while(1):
                i = input("请输入增加的学生信息按学号,班级,姓名顺序输入(用','号分开):")
                List = []
                for j in i.split(','):
                    List.append(j)
                stuinform.add_number(List)
                k=input("添加成功,是否继续输入(y/n):")
                if k=='n':
                    break
            print("学生信息是：",stuinform.get_dict())
            k=input("是否继续执行程序(y/n):")
            if k=='n':
                break
            x=int(input("请继续输入执行命令："))
            continue
        if x==2:###删除学生信息
            while(1):
                i = input("请输入删除学生学号：")
                stuinform.del_number(i)
                k = input("删除成功,是否继续删除(y/n):")
                if k == 'n':
                    break
            k=input("是否继续执行程序(y/n):")
            if k=='n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==3:###查询学生信息
            while(1):
                i=input("请输入查询学生学号：")
                List=stuinform.look_number(i)
                print("学号,班级,姓名:",List)
                k = input("是否继续查询(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==4:###录入课程信息
            while(1):
                i = input("请输入增加的课程信息按课程号,课程名,学分顺序输入(用','号分开):")
                List = []
                for j in i.split(','):
                    List.append(j)
                List[2]=int(List[2])
                clainform.add_number(List)
                k = input("添加成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            scoapproach.name.cla_score=clainform.cla_score
            scoapproach.name.cla_name=clainform.cla_name
            scoapproach.name.cla_number=clainform.cla_number
            print("课程信息是:",clainform.get_dict())
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==5:###删除课程信息
            while(1):
                i = input("请输入删除课程号：")
                clainform.del_number(i)
                k = input("删除成功,是否继续删除(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==6:###查询课程信息
            while(1):
                i = input("请输入查询课程号：")
                List = clainform.look_number(i)
                print("课程号,课程名,学分:", List)
                k = input("是否继续查询(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==7:###录入选课信息
            while(1):
                i = input("请输入增加的选课信息,按学号,课程号,成绩顺序输入(用','号分开):")
                List = []
                for j in i.split(','):
                    List.append(j)
                List[2]=int(List[2])
                choinform.add_number(List)
                k = input("添加成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            scoapproach.choice.cho_clanumber=choinform.cho_clanumber
            scoapproach.choice.cho_stunumber=choinform.cho_stunumber
            scoapproach.choice.cho_score=choinform.cho_score
            print("选课信息：",choinform.get_dict())
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==8:###修改选课信息
            while(1):
                i = input("请输入修改的选课信息,按学号,课程号,成绩顺序输入(用','号分开):")
                List = []
                for j in i.split(','):
                    List.append(j)
                choinform.cha_number(List)
                k = input("修改成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==9:###查询选课信息
            while(1):
                i = input("请输入查询选课信息按 学号,课程号(用','号分开)：")
                List = []
                for j in i.split(','):
                    List.append(j)
                score = choinform.look_number(List)
                print("成绩:", score)
                k = input("是否继续查询(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==10:###各科平均分，及格率
            dic1,dic2=scoapproach.cla_approach()
            print("平均分：",dic1)
            print("及格率：",dic2)
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==11:###学生各科成绩
            i=input("请输入查询学生学号：")
            dict=scoapproach.stu_approach(i)
            print(i,"学生成绩是",dict)
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
if __name__ == '__main__':
    main()