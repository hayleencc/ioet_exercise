from datetime import time
from src.controllers.employees_controller import EmployeesController
from src.controllers.coincidence_controller import CoincidenceController
from src.models.schedule import Schedule
from src.models.employee import Employee


def test_compare_same_day_and_same_hours():
    start_time_a = time(10,32)
    finish_time_a = time(12,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(10,32)
    finish_time_b = time(12, 30)
    scheduleB = Schedule("MO", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 1
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches


def test_compare_same_day_and_closer_hours():
    start_time_a = time(11,50)
    finish_time_a = time(12,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(10,32)
    finish_time_b = time(13,00)
    scheduleB = Schedule("MO", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 1
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches


def test_compare_same_day_and_other_hour():
    start_time_a = time(9,50)
    finish_time_a = time(10,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(10,32)
    finish_time_b = time(13,00)
    scheduleB = Schedule("MO", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 0
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches


def test_compare_different_day_and_closer_hours():
    start_time_a = time(9,50)
    finish_time_a = time(10,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(10,00)
    finish_time_b = time(12,00)
    scheduleB = Schedule("TH", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 0
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches


def test_compare_different_day_and_same_hour():
    start_time_a = time(9,50)
    finish_time_a = time(10,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(9,50)
    finish_time_b = time(10,30)
    scheduleB = Schedule("TH", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 0
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches


def test_compare_different_day_and_different_hours():
    start_time_a = time(9,50)
    finish_time_a = time(10,30)
    scheduleA = Schedule("MO", start_time_a, finish_time_a)

    start_time_b = time(13,00)
    finish_time_b = time(15,30)
    scheduleB = Schedule("TH", start_time_b, finish_time_b)

    counter = 0
    expected_matches = 0
    real_matches = CoincidenceController.compare_day_and_hours(CoincidenceController, scheduleA, scheduleB, counter)

    assert real_matches == expected_matches
