from datetime import time
from src.models.employee import Employee
from src.models.schedule import *


class EmployeesController:

    def parsed_hours(hour: str): 
        hour_times = hour.split(":")
        parsed_time = time(int(hour_times[0]),int(hour_times[1]))
        return parsed_time


    def create_schedule(self, schedule: str):
        hours = schedule.split("-")
        day = hours[0][0:2]
        hours[0]=hours[0][2:]
        start_time = self.parsed_hours(hours[0])
        finish_time = self.parsed_hours(hours[1])
        parsed_schedule= Schedule(day, start_time, finish_time)
        return parsed_schedule        
        

    def formated_schedules(self, schedules: list): 
        formated_schedules = []
        for date in schedules:
            parsed_schedule= self.create_schedule(self, date)
            formated_schedules.append(parsed_schedule)
        return formated_schedules


    def create_employee(self, employee:str):
        schedules = employee.split(",")
        employee_name = schedules[0].split("=")[0]
        first_schedule = schedules[0].split("=")[1]
        schedules[0]= first_schedule
        parsed_schedules = self.formated_schedules(self, schedules)
        new_employee = Employee(employee_name, parsed_schedules)
        return new_employee


    def create_some_employees(self, employees_not_formated:list):
        employees = []
        for employee in employees_not_formated:
            new_employee = self.create_employee(self, employee)
            employees.append(new_employee)
        return employees