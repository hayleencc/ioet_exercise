from src.reader.filereader import *
from src.controllers.employees_controller import *
from src.controllers.coincidence_controller import *
from src.view.view_coincidence import *

def main():
    schedules = FileReader.read_file(".\example_files\more_employees.txt") 
    employees = EmployeesController(schedules).createEmployee()   
    CoincidenceController(employees).search_coincidences_schedule()


if __name__ == "__main__":
    main()
