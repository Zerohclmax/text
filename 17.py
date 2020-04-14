import os
def ch_file(path,old_name,new_name):###重命名函数
    os.chdir(path) ###将目录变成当前位置
    all_file=os.listdir()###返回文件夹中文件名
    for f in all_file:
        portion=os.path.splitext(f)####分离文件名和扩展名
        if portion[1]==old_name:
            newName=portion[0]+new_name###改变文件名
            os.rename(f,newName)

#####main#####
path=input("请输入文件位置(eg:E://xxx//aa):")
old_name=".py"
new_name='.txt'
ch_file(path,old_name,new_name)
print("修改已完成")
