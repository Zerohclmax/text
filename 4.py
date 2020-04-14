from time import strptime

def isLeapYear(year):####是否是闰年
    isLeap=False
    if(year%400==0)or(year%4==0 and year%100!=0):
        isLeap=True
        return isLeap

year_month_day=input("请输入（yyyy-mm-dd）:")
date=strptime(year_month_day,'%Y-%m-%d')
# print(date)####看日期名字
year=date.tm_year
month=date.tm_mon
day=date.tm_mday
days=day

_30_months={4,6,9,11}
_31_months={1,3,5,7,8,10,12}

for i in range(1 ,month):
    if i in _30_months:
        days+=30
    elif i in _31_months:
        days+=31
    else:
        days+=28


if isLeapYear(year) and month>2:
    days+=1
print("这一天是",year,"年的第",days,"天")

