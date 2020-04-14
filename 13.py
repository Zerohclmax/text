from math import pow
def get_flower(a):
    for i in range(100,999):###分离数各个数字
        x=i//100
        y=(i-x*100)//10
        z=(i-x*100-y*10)//1
        if pow(x,3)+pow(y,3)+pow(z,3)==i:
            a.append(i)
    return a

a=[]
print("水仙花数是：",get_flower(a))