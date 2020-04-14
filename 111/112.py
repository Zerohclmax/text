import random
# J,Q,K=1,1,1
class Poke:####洗牌 发牌类

    def __init__(self):
        self.cards=[]
        for face in "♠♥♦♣":
            for valube in [1,2,3,4,5,6,7,8,9,10,'J','Q','K']:
                self.cards.append([face,valube])
        self.cards.append(['小王',1])
        self.cards.append(['大王',1])
        random.shuffle(self.cards)
    def give_onecard(self):
        return self.cards.pop()
class Personal:####裁判类
    def __init__(self,name):###初始名字,分数，手上牌
        self.name=name
        self.points=0
        self.personal_card=[]
    def count(self):#####计算手上牌
        self.points=0
        for face,valube in self.personal_card:
            if valube in ['J', 'Q', 'K']:#####将JQK面值变成1
                valube=1
            self.points+=valube
    def is_win(self,player):###评分方法
        s1=self.points
        s2=player.points####player是电脑
        if s1 > s2:
            print("玩家",self.name,"点数为",s1," 电脑",player.name,"点数为",s2,"玩家",self.name,"赢了！")
        elif s1 == s2:
            print("玩家",self.name,"点数为",s1," 电脑",player.name,"点数为",s2," 平局！")
        else:
            print("玩家",self.name,"点数为",s1," 电脑",player.name,"点数为",s2," 电脑",player.name,"赢了！")
        print("玩家 ",self.name,":",self.personal_card)
        print("电脑 ",player.name,":",player.personal_card)
    def get_card(self,cards):####抓牌
        self.personal_card.append(cards)
        self.count()
    def show_cards(self):####返回牌
        return self.personal_card
def main():
    poke=Poke()
    cumper=Personal('cumpers')
    name=input("请输入玩家您的名字:")
    player=Personal(name)
    player.get_card(poke.give_onecard())######抓牌
    print("玩家",name,":",player.show_cards())
    print("玩家",name,":",player.points)
    if player.points>20:
        print(name,"输了")
    cumper.get_card(poke.give_onecard())
    print("电脑:",cumper.show_cards())
    print('cumper:',cumper.points)
    if player.points>20:
        print('cumper',"输了")
    x=input("是否继续？y/n")
    while(x=='y'):#####玩家开始抓牌
        player.get_card(poke.give_onecard())
        print("玩家",name,":",player.show_cards())
        print("玩家",name,"points=",player.points)
        if player.points > 20:
            print(name, "输了")
        x=input("是否继续？y/n")
    #######cumper和比player大才停止#######
    if player.points<=20:
        while(cumper.points<player.points):
            cumper.get_card(poke.give_onecard())
            print("电脑", cumper.show_cards())
            print("电脑：",cumper.points)
            if cumper.points > 20:
                print('cumper', "输了")
                print("电脑：",cumper.name, ":", cumper.personal_card)
                print("玩家：",player.name, ":", player.personal_card)
                break
        print("电脑:",cumper.points)
        ########总结#################
        print("电脑score=",cumper.points)
        print(name,"score=",player.points)
        if player.points<=20 and cumper.points<=20:
            player.is_win(cumper)
if __name__ == '__main__':
    main()

