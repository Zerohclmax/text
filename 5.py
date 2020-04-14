def get_prime(x):######筛选出素数
    flat=1
    for i in range(2,x):
        if x%i==0:
            flat=0
            break
    if flat==1:
        return x

###main####
a=[1,2,3,4]
x=[2,3]
for i in a:###由1，2，3，4组成的两位数
    for j in a:
        if i==j:
            continue
        else:
            x.append((i*10+j))
for i in a:#####由1，2，3，4组成的三位数
    for j in a:
        for k in a:
            if i==j or i==k or k==j:
                continue
            else:
                x.append((i*100+j*10+k))
for i in a:####由1，2，3，4组成的四位数
    for j in a:
        for k in a:
            for l in a:
                if i==j or i==k or i==l or j==k or j==l or k==l:
                    continue
                else:
                    x.append((i*1000+j*100+k*10+l))

x=list(filter(get_prime,x))
print(x)