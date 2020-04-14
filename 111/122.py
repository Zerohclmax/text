import xlrd
from xlutils import copy

file="学生成绩信息.xls"
class student_inform:
    def __init__(self):
        data = xlrd.open_workbook(file)
        sheet_name = data.sheet_names()[0]
        print(sheet_name,"内容是：")
        sheet = data.sheet_by_name(sheet_name)
        for i in range(0,sheet.nrows):
            print(sheet.row_values(i))
    def del_student(self,number):
        datas = xlrd.open_workbook(file)
        data=datas.sheet_by_index(0)
        sheets = copy.copy(datas)
        sheet=sheets.get_sheet(0)
        numbers=data.col_values(0)
        x=numbers.index(number)
        for i in range(0,3):
            sheet.write(x,i,'')
        sheets.save(file)
        self.__init__()
    def add_student(self,List):
        datas= xlrd.open_workbook(file)
        data=datas.sheet_by_index(0)
        sheets = copy.copy(datas)
        sheet=sheets.get_sheet(0)
        n=data.nrows
        j=0
        for i in List:
            sheet.write(n,j,i)#####map
            j+=1
        sheets.save(file)
        print("修改后：")
        self.__init__()
    def look_student(self,number):
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(0)
        x=data.col_values(0).index(number)
        print(data.row_values(x))
class class_inform:
    def __init__(self):
        data = xlrd.open_workbook(file)
        sheet_name = data.sheet_names()[1]
        print(sheet_name,"内容是：")
        sheet = data.sheet_by_name(sheet_name)
        for i in range(0,sheet.nrows):
            print(sheet.row_values(i))
    def del_class(self,class_number):
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(1)
        sheets = copy.copy(datas)
        sheet = sheets.get_sheet(1)
        class_numbers = data.col_values(0)
        x = class_numbers.index(class_number)
        for i in range(0, 3):
            sheet.write(x, i, '')
        sheets.save(file)
        print("删除后：")
        self.__init__()
    def add_class(self,List):
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(1)
        sheets = copy.copy(datas)
        sheet = sheets.get_sheet(1)
        n = data.nrows
        j = 0
        for i in List:
            sheet.write(n, j, i)  #####map
            j += 1
        sheets.save(file)
        print("修改后：")
        self.__init__()
    def look_class(self,class_number):
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(1)
        x = data.col_values(0).index(class_number)
        print(data.row_values(x))
class chioce_class:
    def __init__(self):
        data = xlrd.open_workbook(file)
        sheet_name = data.sheet_names()[2]
        print(sheet_name,"内容是：")
        sheet = data.sheet_by_name(sheet_name)
        for i in range(0,sheet.nrows):
            print(sheet.row_values(i))
    def add_grade(self,List):
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(2)
        sheets = copy.copy(datas)
        sheet = sheets.get_sheet(2)
        n = data.nrows
        j = 0
        for i in List:
            sheet.write(n, j, i)  #####map
            j+=1
        sheets.save(file)
        print("修改后：")
        self.__init__()
    def look_grade(self,stu_number):
        print(stu_number, ":")
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(1)
        x = data.col_values(0).index(stu_number)
        print(data.row_values(x))
    def change_student(self,stu_number,List):###List是2
        datas = xlrd.open_workbook(file)
        data = datas.sheet_by_index(2)
        sheets = copy.copy(datas)
        sheet = sheets.get_sheet(2)
        x = data.col_values(0).index(stu_number)
        j=1
        for i in List:
            sheet.write(x,j,i)
            j+=1
        sheets.save(file)
        print("修改完：")##############不在这写print可以减少（在主函数写）
        self.__init__()
class score_sta:
    def 









# a=class_inform()
# a.add_class(['2345','sdfg','sdg'])
# a.del_class(2345)
# a.look_class(2345)
# a=student_inform()
# # # a.add_student([2.353,'sss','ggg'])
# # a.del_student(2.7)
# a.look_student(7)
