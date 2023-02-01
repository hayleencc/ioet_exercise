from datetime import time
from src.models.employee import *
from src.models.schedule import *



class EmployeesController:

    def __init__(self, employees: list):
        self.employees = employees

    def parsed_hours(self, hour: str): 
        hour_times = hour.split(":")
        parsed_time = time(int(hour_times[0]),int(hour_times[1]))
        return parsed_time


    def createSchedule(self, schedules: list): 
        formated_schedules = []
        for date in schedules:
            hours = date.split("-")
            day = hours[0][0:2]
            hours[0]=hours[0][2:]
            start_time = self.parsed_hours(hours[0])
            finish_time = self.parsed_hours(hours[1])
            parsed_schedule= Schedule(day, start_time, finish_time)
            #formated_schedules[day] = dict([('start_time', start_time), ('finish_time', finish_time)])
            #formated_schedules[day] = schedule
            formated_schedules.append(parsed_schedule)
            #print(a.getSchedule)
        return formated_schedules


    def createEmployee(self):
        employees = []
        for employee in self.employees:
            schedules = employee.split(",")
            employee_name = schedules[0].split("=")[0]
            first_schedule = schedules[0].split("=")[1]
            schedules[0]= first_schedule
            parsed_schedules = self.createSchedule(schedules)
            new_employee = Employee(employee_name, parsed_schedules)
            employees.append(new_employee)
        return employees