def need(n):###求场数
    if n==1:
        return 0
    if n==2:
        return 1
    m,c=divmod(n,2)
    return m+need(m+c)

n=int(input("请输入人数："))
print("需要",need(n),"场才能结束")