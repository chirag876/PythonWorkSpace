# import pytest
# import os
# import sys

# # Add the project root directory to the Python path
# # Retrieve the absolute path of the project root directory by navigating up two levels from the current file's directory.
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
# # Insert the project root directory at the beginning of the Python system path list (sys.path).
# # This ensures that when Python searches for modules or packages, it considers the project root directory first.
# sys.path.insert(0, project_root)

# from app import app  # Import your Flask app instance


# @pytest.fixture
# def client():
#     # Using a fixture to set up a test client for the Flask app
#     with app.test_client() as client:
#         # Set up a test client to simulate requests to the app
#         yield client
#         # The 'yield' statement allows the fixture to provide the test client
#         # This is where the test cases will be executed

# def test_add_student(client):
#     # Test adding a student
#     data = {
#         "name": "Alice",
#         "age": 21,
#         "grade": "A"
#     }
#     response = client.post('/students', json=data)
#     assert response.status_code == 200
#     # Additional assertions to check if the student is added to the database


# def test_get_students(client):
#     # Test getting all students
#     response = client.get('/students')
#     assert response.status_code == 200
#     # Additional assertions to check the response data


# def test_get_student(client):
#     # Test getting a specific student by ID
#     response = client.get('/students/1')  # Assuming student ID 1 exists
#     assert response.status_code == 200
#     # Additional assertions to check the response data


# def test_update_student(client):
#     # Test updating a student by ID
#     data = {
#         "name": "Updated Name",
#         "age": 25,
#         "grade": "B"
#     }
#     response = client.put('/students/1', json=data)  # Assuming student ID 1 exists
#     assert response.status_code == 200
#     # Additional assertions to check if the student is updated in the database


# def test_delete_student(client):
#     # Test deleting a specific student by ID
#     response = client.delete('/students/1')  # Assuming student ID 1 exists
#     assert response.status_code == 200
#     # Additional assertions to check if the student is deleted from the database


# def test_delete_all_students(client):
#     # Test deleting all students
#     response = client.delete('/students')
#     assert response.status_code == 200
#     # Additional assertions to check if all students are deleted from the database
