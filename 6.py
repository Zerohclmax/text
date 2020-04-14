a_list=[10,20,34,44,55,66,77,88,99,90]
print("a_list:",a_list)
def b_sort(x):####大于60条件
    if x>60:
        return x
def c_sort(x):####小于60条件
    if x<60:
        return x
b_list=list(filter(b_sort,a_list))#####filter高阶函数
c_list=list(filter(c_sort,a_list))#####filter高阶函数
b=','.join('%s' %x for x in b_list)###jion只能字符串
c=','.join('%s' %x for x in c_list)
dict={}
dict['k1']=b###创建k1建
dict['k2']=c###创建k2建
print(dict)

