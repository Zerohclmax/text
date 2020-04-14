stack=[1]
try:
    stack.pop()
    len(stack)!=0
except BaseException:
    print("删除操作错误")
else:
    print("删除操作正常")