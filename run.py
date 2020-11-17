from dd6 import Logger, User
import xlwt
import datetime

wb = xlwt.Workbook()

sheet1 = wb.add_sheet('Sheet 1')
user1 = User('./data/0101.csv')
user2 = User('./data/0102.csv')

print(user1.getDate(1))
for i in range(len(user1.logs)):
    sheet1.write(i, 0, user1.getDate(i))
    sheet1.write(i, 1, user1.getSteps(i))
    sheet1.write(i, 2, user2.getSteps(i))

wb.save('test2.xls')