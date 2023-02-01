from datetime import time

class Schedule:

    def __init__(self, day: str, start_time: time, finish_time: time):
        self._day = day
        self._start_time = start_time
        self._finish_time = finish_time

    def get_day(self) -> str:
        return self._day  

    def get_start_time(self) -> time:
        return self._start_time

    def get_finish_time(self) -> time:
        return self._finish_time


    