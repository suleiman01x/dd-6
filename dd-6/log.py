from os import listdir
from os.path import isfile, join
from datetime import datetime


class Logger:
    def __init__(self, dir):
        self.logs = Logger.fromDirectory(dir)
        self.users = list(self.logs.keys())

    @staticmethod
    def fromDirectory(dir):
        logFiles = listdir(dir)
        users = {}
        for fileName in logFiles:
            users[fileName[:-4]] = User(join(dir, fileName))
        return users

class User:
    def __init__(self, fileDir):
        self.logs = User.fromFile(fileDir)

    def steps(self, time):
        for log in self.logs:
            if time == log[0]:
                out = log[1]
        if not out:
            print('time {} not found'.format(time))
        return out

    def stepsFromIndex(self, indexNum):
        return self.logs[indexNum][1]

    def timeFromIndex(self, indexNum):
        return self.logs[indexNum][0]

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
    foo = Logger('../data')
    print(foo.users[0])