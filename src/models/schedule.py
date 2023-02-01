from datetime import time

class Schedule:

    def __init__(self, day: str, start_time: time, finish_time: time):
        self.day = day
        self.start_time = start_time
        self.finish_time = finish_time

    def get_day(self) -> str:
        return self.day  

    def get_start_time(self) -> time:
        return self.start_time

    def get_finish_time(self) -> time:
        return self.finish_time
    
    def get_schedule(self) -> dict:
        schedule =  dict([('startTime', self.getStartTime()), ('finishTime', self.getFinishTime())])

    