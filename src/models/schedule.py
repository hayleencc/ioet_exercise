from datetime import  time

class Schedule:

    def __init__(self, day, start_time, finish_time):
        self.day = day
        self.start_time = start_time
        self.finish_time = finish_time

    def getDay(self) -> str:
        return self.day  

    def getStartTime(self) -> time:
        return self.start_time

    def getFinishTime(self) -> time:
        return self.finish_time
    
    def getSchedule(self) -> dict:
        schedule =  dict([('startTime', self.getStartTime()), ('finishTime', self.getFinishTime())])

    