f=open("sample.txt")
lines=[]
long=[]
for line in f:####将文本分开
    lines.append(line)
    long.append(len(line))
maxLine=max(long)
x=long.index(maxLine)
print("sample中最长行是：",x+1," 长度是：",maxLine," 内容是：",lines[x])
f.close()