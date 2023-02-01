from src.models.schedule import *

class Employee:

    def __init__(self, name: str, schedule: list):
        self._name = name
        self._schedule = schedule

    def get_name(self) -> str:
        return self._name

    def get_schedule(self) -> list:
        return self._schedule

        