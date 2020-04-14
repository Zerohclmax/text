def split_file(filename):####分离函数
    col1=[]
    col2=[]
    f=open(filename)
    text=f.read()###读取文件内容
    lines=text.splitlines()###将文件内容行分离
    for line in lines:
        part=line.split(None,1)###分离两列
        col1.append(part[0])
        col2.append(part[1])
    return col1,col2
def write_list(filename,lists):####创建文件函数
    f=open(filename,'w')
    for line in lists:
        f.write(line+'/n')
#####main####
filename="input.txt"
col1,col2=split_file(filename)####分离文本
write_list('col1.txt',col1)###创建col1
write_list('col2.txt',col2)###创建col2
