from datetime import time

from src.controllers.employees_controller import EmployeesController
from src.models.schedule import Schedule
from src.models.employee import Employee

def test_parsed_hours():
    schedule = "12:00"
    parsed_schedule = EmployeesController.parsed_hours(schedule)
    assert (type(parsed_schedule) == time)


def test_create_schedule():
    employee_schedule = "MO10:00-12:00"
    formated_schedule = EmployeesController.create_schedule(EmployeesController, employee_schedule)
    assert (type(formated_schedule) == Schedule)


def test_formated_schedules():
    employee_schedules = ["MO10:00-12:00","MO12:00-14:00","MO20:00-21:00"]
    formated_schedules = EmployeesController.formated_schedules(EmployeesController, employee_schedules)

    for schedule in formated_schedules:
        assert(type(schedule)== Schedule)
        assert schedule.get_day()=="MO"


def test_create_employee():
    line_employee = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    employee = EmployeesController.create_employee(EmployeesController, line_employee)
    assert type(employee)==Employee
    assert employee.get_name()=="ASTRID"


def test_create_some_employees():
    info_employees = ["ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00", "ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"]
    employees = EmployeesController.create_some_employees(EmployeesController, info_employees)
    
    for employee in employees:
        assert type(employee)==Employee
        assert employee.get_name()=="ASTRID" or employee.get_name()=="ANDRES"
        first_schedule = employee.get_schedule()[0]
        assert type(first_schedule) == Schedule
