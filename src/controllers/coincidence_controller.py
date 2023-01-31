from models.schedule import *

class coincidenceController:

    def __init__(self, employees_list):
        self.employees_list = employees_list    
    
    def searchEmployeesCoincidence(self):
        coincidences = {}

        for i in range(len(self.employees_list)):
            for j in range(i+1, len(self.employees_list)):
                coincidences[(self.employees_list[i].getName(),self.employees_list[j].getName())] = 0
                self.compareDayHours(self.employees_list[i], self.employees_list[j], coincidences)

        return coincidences


    def compareDayHours(self, employee1, employee2, coincidences):
        sch_emp1 = employee1.getSchedule()
        sch_emp2 = employee2.getSchedule()

        for day in sch_emp1.keys():
            if (day in sch_emp2.keys()):
                
                startTime_1 = sch_emp1[day]['startTime']
                finishTime_1 = sch_emp1[day]['finishTime']
                startTime_2 = sch_emp2[day]['startTime']
                finishTime_2 = sch_emp1[day]['finishTime']

                if(startTime_1<=startTime_2<=finishTime_1 and startTime_1<=finishTime_2<=finishTime_1) or (startTime_2 <=startTime_1<=finishTime_2 and startTime_2<=finishTime_1<=finishTime_2):
                    coincidences[(employee1.getName(),employee2.getName())]+=1
                
                

    
    
