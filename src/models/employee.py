from src.models.schedule import *

class Employee:

    def __init__(self, name: str, schedule: list):
        self.name = name
        self.schedule = schedule

    def get_name(self) -> str:
        return self.name

    def get_schedule(self) -> list:
        return self.schedule

        