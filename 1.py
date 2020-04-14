import random
a=[]
for i in range(50):
    x=random.randint(0,100)
    a.append(x)
print("a:",a)
b=a[::2]
b.sort(reverse=True)
a[::2]=b
print("排序后的a:",a)


