import time
from datetime import datetime


month_salary=25000
#开始工作时间
start_hour=10

#结束工作时间
end_hour=19

work_time=(end_hour-start_hour)*3600

def main():


    #启动时已拥有的money
    current=datetime.now()
    month=current.month
    hour=current.hour

    #计算日工资
    big_month=[1,3,5,7,8,10,12]
    day_salary=month_salary/22 if month not in big_month else month_salary/23

    #1秒统计一次
    secondSalary=day_salary/work_time

    #还没开始工作---
    if hour<start_hour:
        return

    #已工作时间
    had_worktime=(hour-start_hour)*3600+current.minute*60+current.second

    money=had_worktime*secondSalary

    while hour<19:
        current=datetime.now()
        hour=current.hour
        if hour<end_hour:
            money+=secondSalary
            time.sleep(1)
        print(money)


if __name__ == '__main__':
    main()



