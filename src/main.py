from reader.filereader import *
from controllers.employees_controller import *
from controllers.coincidence_controller import *
from view.view_coincidence import *

def main():
    schedule_info = fileReader.readFile("files\employees_schedule.txt") 
    employees_list = employeesController(schedule_info).createEmployee()
    results = coincidenceController(employees_list).searchEmployeesCoincidence()
    viewCoincidence(results).show_matches()

if __name__ == "__main__":
    main()