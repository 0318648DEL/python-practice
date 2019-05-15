from datetime import *


class StopWatch:
    def __init__(self):
        self.startTime=datetime.utcnow()
        self.endTime=0

    def start(self):
        self.startTime=datetime.utcnow()

    def stop(self):
        self.endTime=datetime.utcnow()

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.endTime

    def getElapsedTime(self):
        td=datetime.utcnow()-self.startTime
        return (td.microseconds+(td.days*24*60*60+td.seconds)*10**6)/10**3


t=StopWatch()
a=0
for i in range(1000000):
    a=a+i
print("경과시간(밀리초 단위) : ",t.getElapsedTime())
