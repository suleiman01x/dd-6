from os import listdir
from os.path import isfile, join
from datetime import datetime
import math

def indexFirstElement(_list, key):
    for index, content in enumerate(_list):
        if content[0] == key:
            return index

class Logger:
    minMother = 5500
    maxDiss = 0.05
    minTime = 15
    searchFrame = 60

    def __init__(self, dir):
        self.logs = Logger.fromDirectory(dir)
        self.users = list(self.logs.keys())

    def getPoint(self, user1, user2):
        minMother = self.minMother
        frame = self.searchFrame
        maxDiss = self.maxDiss
        minTime = self.minTime
        dissim, mother = self.getDissim(user1, user2, frame)

        point = 0
        for i in range(len(dissim) - (minTime - 1)):
            if all(diss <= maxDiss for diss in dissim[i:(i+minTime)]) and all(mom >= minMother for mom in mother[i:(i+minTime)]):
                point += 1
        
        return point


    def getDissim(self, user1, user2, frame):
        child, mother = self.getRawDissim(user1, user2)

        dissim = []
        dissMoth = []
        for i in range(len(child) - (frame - 1)):
            try:
                dissim.append(sum(child[i:(i + frame)])/ sum(mother[i:(i + frame)]))
            except ZeroDivisionError:
                dissim.append(0)
            dissMoth.append(sum(mother[i:(i +  frame)]))
        
        return (dissim, dissMoth)

    def getRawDissim(self, user1, user2):
        if not user1 in self.users or not user2 in self.users:
            raise ValueError
        
        tempA, tempB = Logger.getRaw(self.logs[user1], self.logs[user2])
        child = []
        mother = []
        for i in range(len(tempA)):
            child.append((tempA[i][1] - tempB[i][1]) ** 2)
            mother.append((tempA[i][1] ** 2) + (tempB[i][1] ** 2))
        # calcMin is an array of tuples ((a-b)^2, a^2+b^2)

        return (child, mother)

    @staticmethod
    def getRaw(user1, user2):
        # compare dates. if user1 log starts later than user2, it is shorter
        if user1.firstTime() > user2.firstTime():
            longer = user2.logs
            shorter = user1.logs
        else:
            longer = user1.logs
            shorter = user2.logs
        # idk wtf I did, but this returns a log that starts at the same date as the shorter log
        return (longer[indexFirstElement(longer, shorter[0][0]):], shorter)

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

    def getSteps(self, index):
        return self.logs[index][1]
    
    def firstTime(self):
        return self.logs[0][0]
    
    def getDate(self, index):
        return self.logs[index][0]

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
    testLogger = Logger('C:/Users/Shun/source/dd-6/testData')
    print(testLogger.users)
    print(testLogger.getDissim('foo', 'bar', 3))