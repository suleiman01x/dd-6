from dd6 import User, Logger
import xlwt


wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet 1')
dump = Logger('./data')

currentNum = 0
for x in range(len(dump.users)):
    for y in range(len(dump.users)):
        if x > y:
            userX = dump.users[x]
            userY = dump.users[y]
            print(userX, userY, dump.getPoint(userX, userY))
            sheet1.write(currentNum, 0, userX)
            sheet1.write(currentNum, 1, userY)
            sheet1.write(currentNum, 2, dump.getPoint(userX, userY))
            currentNum += 1

wb.save('output2.xls')