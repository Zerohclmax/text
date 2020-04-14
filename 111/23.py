import random
from collections import Counter

class Manager:###管理员类
    def __init__(self):
        self.__sup_Name='admin'###超级管理员用户名
        self.__sup_PW='admin'###超级管理员密码
        self.isLogin=False###是否超级管理员验证成功
        self.isclogin=False###是否普通管理员研验证成功
        self.__dict_Man={}###普通管理员用户名和密码
        self.__chip_dict={}###玩家和筹码
    def is_Login(self,name,PassWord):###成绩管理员登录方法
        if self.__sup_Name==name and self.__sup_PW==PassWord:
            self.isLogin=True
        else:
            self.__isLogin=False
            print("用户名错误或者密码错误")
    def add(self,name,password):####增加普通管理员方法
        if self.isLogin==True:
            self.__dict_Man[name]=password
        else:
            print("您没有权限访问！")######   无用
    def chamge_PW(self,name,password):####修改普通管理员方法
        if self.isLogin == True:
            if name in self.__dict_Man:
                self.__dict_Man=password
            else:
                print("用户名错误")
        else:
            print("您没有权限访问！")
    def del_PW(self,name):###删除普通管理员方法
        if self.isLogin == True:
            self.__dict_Man.pop(name)
        else:
            print("您没有权限访问！")
    def is_mangers(self,name,password):###验证普通管理员方法
        try:
            if self.__dict_Man[name]==password:
                self.isclogin=True
                print("验证成功！")
            else:
                print("密码错误")
        except KeyError:
            print("用户名错误")
    def add_chip(self,cname,chip):####增加筹码
        if self.isclogin==True:
            self.__chip_dict[cname]=chip
    def get_chip(self,cname):###返回筹码
        if self.isclogin == True:
            if cname in self.__chip_dict:
                return self.__chip_dict[cname]
            else:
                print("没有用户!")
                return -1
class Screen:###游戏屏类
    def __init__(self):
        self.F1 = ["✿", "♠", "♥", "♦", "♣"]
        self.F2 = ["✿", "♠", "♥", "♦", "♣"]
        self.F3 = ["✿", "♠", "♥", "♦", "♣"]
        self.F4 = ["✿", "♠", "♥", "♦", "♣"]
        self.F5 = ["✿", "♠", "♥", "♦", "♣"]
        random.shuffle(self.F1)####打乱顺序
        random.shuffle(self.F2)
        random.shuffle(self.F3)
        random.shuffle(self.F4)
        random.shuffle(self.F5)
    def get_screen(self):####返回图形
        list=[self.F1.pop(),self.F2.pop(),self.F3.pop(),self.F4.pop(),self.F5.pop()]
        return list
def main():
    manager=Manager()###实例化管理员类
    Sname=input("超级管理员用户名:")
    Spassword=input("超级管理员密码:")
    manager.is_Login(Sname,Spassword)###验证登录是否成功
    while(manager.isLogin==False):###验证失败重新输入
        name=input("超级管理员用户名:")
        password=input("超级管理员密码:")
        manager.is_Login(name,password)
    print("1.增加管理员信息;2.修改管理员信息;3.删除管理员信息")
    x =int(input("请输入操作符号:"))
    while(1):####增加管理员信息
        if x==1:
            while(1):
                name=input("普通管理员用户名:")
                password=input("普通管理员密码:")
                manager.add(name,password)
                k = input("添加成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==2:####修改管理员信息
            while(1):
                name = input("普通管理员用户名:")
                password=input("新普通管理员密码:")
                manager.chamge_PW(name,password)
                k = input("修改成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
        if x==3:####删除管理员信息
            while (1):
                name = input("删除的普通管理员用户名:")
                manager.del_PW(name)
                k = input("删除成功,是否继续输入(y/n):")
                if k == 'n':
                    break
            k = input("是否继续执行程序(y/n):")
            if k == 'n':
                break
            x = int(input("请继续输入执行命令："))
            continue
    print("设置结束！！")
    name=input("普通管理员用户名:")
    password=input("普通管理员密码:")
    manager.is_mangers(name,password)
    while (manager.isLogin == False):###验证失败重新输入
        name = input("管理员用户名:")
        password = input("管理员密码:")
        manager.is_mangers(name, password)
    while(1):
        cname=input("用户名")
        chip=int(input("筹码:"))
        manager.add_chip(cname,chip)
        k = input("输入成功,是否继续输入(y/n):")
        if k == 'n':
            break
    print("游戏开始!！")
    while(1):
        screen = Screen()
        cname=input("用户名:")
        chip=manager.get_chip(cname)
        while(chip==-1):
            cname = input("请重新输入用户名:")
            chip = manager.get_chip(cname)
        print(cname, ":", chip)
        if chip<=0:###筹码全输光了
            k=input("筹码不足，是否重新输入(y/n)")
            if k=='n':
                break
            continue
        chips=int(input("请输入筹码"))
        while(chips>chip):####筹码大于总筹码
            chips=int(input("筹码不够!请重新输入筹码:"))
        List = ["F1", "F2", "F3", "F4", "F5"]
        List1=screen.get_screen()
        List2=screen.get_screen()
        List3=screen.get_screen()
        print(List)
        print(List1)
        print(List2)
        print(List3)
        a=max(Counter(List1).values())###Counter用来返回列表中相同元素
        b=max(Counter(List2).values())
        c=max(Counter(List3).values())
        if a<3 and b<3 and c<3:#####玩家输了
            manager.add_chip(cname,chip-chips)###总筹码减取输掉的筹码
            print("您输了！！")
        else:
            returns=chips*0.9
            print("您赢了，赚了",returns)
            manager.add_chip(cname,chip+returns)###总筹码加上赢的筹码（反率是0.9）
        k=input("是否要继续(y/n)")
        if k=='n':
            break
if __name__ == '__main__':
    main()

