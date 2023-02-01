from src.reader.filereader import *
from src.controllers.employees_controller import *
from src.controllers.coincidence_controller import *

def main():
    schedules = FileReader.read_file(".\example_files\employees_schedule.txt") 
    employees = EmployeesController.create_some_employees(EmployeesController, schedules) 
    CoincidenceController.search_coincidences_schedule(CoincidenceController, employees)


if __name__ == "__main__":
    main()
