from src.models.schedule import *
from src.models.employee import *

class CoincidenceController:

    def search_coincidences_schedule(self, employees: list):
        index_begin = 0
        move_begin = 1
        self.iterate_employees(self, employees, index_begin, move_begin)  
        
    
    def iterate_employees(self, employees, index_begin: int, next_move: int):
    
        coincidences_employees = {}
        limit = index_begin + next_move

        if(limit < len(employees)):

            employeeA = employees[index_begin]
            next_employee = employees[index_begin+next_move]
            tuple_employees_names =  employeeA.get_name()+'-'+next_employee.get_name()
            counter = self.iterate_schedule(self, employeeA.get_schedule(), next_employee.get_schedule())
            coincidences_employees[tuple_employees_names]=counter
            self.iterate_employees(self,employees, index_begin, next_move+1)
            print(tuple_employees_names+": "+str(counter))
        
        if (limit== len(employees)):
            self.iterate_employees(self,employees, index_begin+1, 1)

        return coincidences_employees


    def comparate_schedules_two_employees(self, employee_a:Employee, employee_b:Employee, index_begin:int, next_move:int):
        tuple_employees_names =  employee_a.get_name()+'-'+employee_b.get_name()
        counter = self.iterate_schedule(self, employee_a.get_schedule(), employee_b.get_schedule())
        print(tuple_employees_names+": "+str(counter))
        next_move+=1


    def iterate_schedule(self, schedulesA: Schedule, schedulesB: Schedule):
        counter = 0
        for i in range(len(schedulesA)):
            iterate_scheduleA = schedulesA[i]
            for j in range (len(schedulesB)):
                iterate_scheduleB = schedulesB[j]
                counter = self.compare_day_and_hours(self, iterate_scheduleA, iterate_scheduleB, counter)

        return counter

    def compare_day_and_hours(self, scheduleA: Schedule, scheduleB:Schedule, matches: int):

        start_time_a = scheduleA.get_start_time() #[day]['start_time']
        finish_time_a= scheduleA.get_finish_time()#[day]['finish_time']
        start_time_b = scheduleB.get_start_time() 
        finish_time_b = scheduleB.get_finish_time()

        if(scheduleA.get_day()== scheduleB.get_day()):

            a_contains_b = (start_time_a < start_time_b) and (finish_time_a > finish_time_b)
            a_equals_b = (start_time_a == start_time_b) and (finish_time_a == finish_time_b)
            b_contains_a = (start_time_b < start_time_a) and (finish_time_b > finish_time_a)
            a_after_b = (start_time_a > start_time_b or start_time_a == start_time_b) and (finish_time_a > finish_time_b or finish_time_a == finish_time_b) and (start_time_a < finish_time_b)
            a_before_b = (start_time_a < start_time_b or start_time_a == start_time_b) and (finish_time_a < finish_time_b or finish_time_a == finish_time_b) and (start_time_b < finish_time_a)

            if (a_contains_b or a_equals_b or b_contains_a or a_after_b or a_before_b):
                matches+=1

        return matches