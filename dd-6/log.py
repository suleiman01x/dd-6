from os import listdir
from os.path import isfile, join
from datetime import datetime


class User:
    def __init__(self, fileDir):
        self.logs = User.fromFile(fileDir)

    @staticmethod
    def fromFile(fileDir):
        data = []
        with open(fileDir) as fs:
            data = fs.readlines()
        
        tempLogs = []
        for log in data:
            date, time, num = log.split(',')
            if log == 'date,time,steps':
                continue
            
            print(date + time)
            tempLogs.append((datetime.strptime(date + time, '%Y%m%d%H:%M:%S'), int(num[:-2])))

        return tempLogs

if __name__ == '__main__':
    foo = User('../data/0101.csv')
    print(foo.logs)