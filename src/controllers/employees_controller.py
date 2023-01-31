from datetime import time
from models.employee import *
from models.schedule import *


class employeesController:

    def __init__(self, employees_list):
        self.employees_list = employees_list

    def parseHours(self, hour_str): #the hours will be an object of time type instead str
        hour_list = hour_str.split(":")
        finalTime = time(int(hour_list[0]),int(hour_list[1]))
        return finalTime


    def createSchedule(self, date_str): #create an array of Schedule objects with parsed hours 
        schedules = {}
        for date in date_str:
            hours_time = []
            hours_str = date.split("-")
            day = hours_str[0][0:2]
            hours_str[0]=hours_str[0][2:]
            startTime = self.parseHours(hours_str[0])
            finishTime = self.parseHours(hours_str[1])
            #schedules.append(Schedule(day, startTime, finishTime))
            sch = Schedule(day, startTime, finishTime)
            schedules[day] = dict([('startTime', startTime), ('finishTime', finishTime)])
            #print(a.getSchedule)
        return schedules


    def createEmployee(self):
        finalEmployees = []
        for one_employee in self.employees_list:
            schedules = one_employee.split(",")
            emp_name = schedules[0].split("=")[0]
            first_sch = schedules[0].split("=")[1]
            schedules[0]= first_sch
            parseSchedules = self.createSchedule(schedules)
            new_employee = Employee(emp_name, parseSchedules)
            finalEmployees.append(new_employee)
        return finalEmployees