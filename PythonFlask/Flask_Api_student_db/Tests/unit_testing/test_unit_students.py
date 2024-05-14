import os
import sys


# Add the project root directory to the Python path
# Retrieve the absolute path of the project root directory by navigating up two levels from the current file's directory.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# Insert the project root directory at the beginning of the Python system path list (sys.path).
# This ensures that when Python searches for modules or packages, it considers the project root directory first.
sys.path.insert(0, project_root)

from student_service import StudentService
# Test adding a student
def test_add_student():
    # Initialize StudentService
    service = StudentService()
    # Data to add a student
    student_data = {
        'name': 'Test Student',
        'age': 20,
        'grade': 'A'
    }
    # Add a student
    service.add_student(student_data)
    # Check if the student has been added
    students = service.get_students()
    # The assert statement checks if at least one of these conditions is True. If it is, the code continues executing; otherwise, it raises an AssertionError exception, indicating that the test has failed.
    assert any(student['name'] == 'Test Student' for student in students)
    
#     assert any(
#     student['name'] == 'Test Student' and
#     student['age'] == 20 and
#     student['grade'] == 'A'
#     for student in students
# )

# Test getting all students
def test_get_students():
    # Initialize StudentService
    service = StudentService()
    # Check if students are retrieved properly
    students = service.get_students()
    assert isinstance(students, list)

# Test getting a student by ID
def test_get_student():
    # Initialize StudentService
    service = StudentService()

    # Create a test student (add a student)
    student_data = {
        'name': 'Test Student',
        'age': 20,
        'grade': 'A'
    }
    service.add_student(student_data)

    # Get the test student by ID
    test_student = service.get_students()[0]  # Assuming the first student is the test student

    # Check if the retrieved student matches the test data
    retrieved_student = service.get_student(test_student['id'])
    assert retrieved_student == test_student

# Test updating a student
def test_update_student():
    # Initialize StudentService
    service = StudentService()

    # Add a test student
    student_data = {
        'name': 'Test Student',
        'age': 20,
        'grade': 'A'
    }
    service.add_student(student_data)

    # Get the test student
    test_student = service.get_students()[0]

    # Update the test student's details
    updated_data = {
        'name': 'Updated Test Student',
        'age': 21,
        'grade': 'A+'
    }
    service.update_student(test_student['id'], updated_data)

    # Get the updated student details
    updated_student = service.get_student(test_student['id'])

    # Check if the student details are updated correctly
    assert updated_student['name'] == 'Updated Test Student'
    assert updated_student['age'] == 21
    assert updated_student['grade'] == 'A+'

# Test deleting a student
def test_delete_student():
    # Initialize StudentService
    service = StudentService()

    # Add a test student
    student_data = {
        'name': 'Test Student',
        'age': 20,
        'grade': 'A'
    }
    service.add_student(student_data)

    # Get the test student
    test_student = service.get_students()[0]

    # Delete the test student
    service.delete_student(test_student['id'])

    # Check if the student is deleted
    students = service.get_students()
    assert not any(student['id'] == test_student['id'] for student in students)

# Test deleting all students
def test_delete_all_students():
    # Initialize StudentService
    service = StudentService()

    # Add test students
    student_data_1 = {
        'name': 'Test Student 1',
        'age': 20,
        'grade': 'A'
    }
    student_data_2 = {
        'name': 'Test Student 2',
        'age': 22,
        'grade': 'A+'
    }
    service.add_student(student_data_1)
    service.add_student(student_data_2)

    # Delete all students
    service.delete_students()

    # Check if all students are deleted
    students = service.get_students()
    assert not students
