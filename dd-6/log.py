from os import listdir
from os.path import isfile, join
from datetime import datetime


class User:
    def __init__(self, fileDir):
        self.logs = User.fromFile(fileDir)

    def steps(self):
        out = []
        for log in self.logs:
            out.append(log[1])
        return out

    @staticmethod
    def fromFile(fileDir):
        data = []
        with open(fileDir) as fs:
            data = fs.readlines()
        
        tempLogs = []
        for log in data:
            date, time, num = log.split(',')
            if log.startswith('date') :
                continue
            
            tempLogs.append((datetime.strptime(date + time, '%Y%m%d%H:%M:%S'), int(num)))

        return tempLogs

if __name__ == '__main__':
    foo = User('../data/0101.csv')
    print(foo.logs)