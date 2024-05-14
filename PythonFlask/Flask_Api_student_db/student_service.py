import mysql.connector
import json
import csv


class StudentService:
    def __init__(self):
        # Establishing a connection to the MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="chirag",
            database="flaskapi"
        )
        # Creating a buffered cursor for database operations
        # A buffered cursor in MySQL retrieves rows from the database and stores them in memory, allowing faster access and manipulation of data.
        # It loads the result set entirely into memory, enabling efficient navigation through the data. 
        # This type of cursor is advantageous for situations where you need to traverse the data multiple times. 
        self.cursor = self.db.cursor(buffered=True)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, grade VARCHAR(10))")
#------------------------------------------------------------------------------------------------------------------------------------------#

    def update_files(self):
        # Retrieve all students from the database
        students = self.get_students()
        if not students:
            return ('Failure: No students found for download'), 404
        # Update the JSON file
        students_data_json = json.dumps(students, indent=2)
        with open('C:/Workspaces/CodeSpaces/Python_Work/Flask_API-main/Flask_Api_student_db/students_data.json', 'w') as file:
            file.write(students_data_json)
        # Update the CSV file
        with open('C:/Workspaces/CodeSpaces/Python_Work/Flask_API-main/Flask_Api_student_db/students_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'age', 'grade'])
            for student in students:
                writer.writerow([student['id'], student['name'], student['age'], student['grade']])

#------------------------------------------------------------------------------------------------------------------------------------------#

    def import_students(self, file_path):
        try:
        # Open the file at the specified path in read mode
            with open(file_path, 'r') as file:
            # Check the file extension to determine the format
                if file_path.endswith('.csv'):
                # If it's a CSV file, use DictReader to read rows as dictionaries
                    reader = csv.DictReader(file)
                # Iterate over each row in the CSV file
                    for row in reader:
                    # Add each student from the CSV row to the database
                        self.add_student(row)
                elif file_path.endswith('.json'):
                # If it's a JSON file, load the entire content as a JSON object
                    data = json.load(file)
                # Iterate over each student in the JSON data
                    for student in data:
                    # Add each student from the JSON data to the database
                        self.add_student(student)
                else:
                # Return False if the file format is not supported (neither CSV nor JSON)
                    return False  # Unsupported file format
            # Return True to indicate successful import
                return True
        except Exception as e:
        # Print any exceptions that occur during the import process
            print(e)
        # Return False if an exception occurs, indicating a failed import
            return False

#------------------------------------------------------------------------------------------------------------------------------------------#

    def add_student(self, data):
        insert_query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        self.cursor.execute(insert_query, (data['name'], data['age'], data['grade']))
        # Commit the changes to the database
        self.db.commit()
        self.update_files()

#------------------------------------------------------------------------------------------------------------------------------------------#
    
    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        # Fetch all the records returned by the query
        students = self.cursor.fetchall() 
        if not students:  
            # If no students, return None or an empty list
            return None 
        # empty list to store student data
        student_list = [] 
        for student in students: 
            # dictionary for each student, mapping database fields to keys
            student_list.append({
            'id': student[0],
            'name': student[1],
            'age': student[2],
            'grade': student[3]
        })
        # Returns the list of dictionaries containing student information
        return student_list

#------------------------------------------------------------------------------------------------------------------------------------------#      
    def get_student(self, id):
        self.cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        # Fetches the first row of the result
        student = self.cursor.fetchone()
        if student:
            return {
                'id': student[0],
                'name': student[1],
                'age': student[2],
                'grade': student[3]
            }
        return None

#------------------------------------------------------------------------------------------------------------------------------------------#     
    def update_student(self, id, data):
        check_query = "SELECT id FROM students WHERE id = %s"
        self.cursor.execute(check_query, (id,))
        existing_student = self.cursor.fetchone()
        if existing_student:
            update_query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
            self.cursor.execute(update_query, (data['name'], data['age'], data['grade'], id))
            self.db.commit()  # Update the database
            self.update_files()
            return True 
        else:
            return False  
    
#------------------------------------------------------------------------------------------------------------------------------------------#    
    def delete_student(self, id):
        check_query = "SELECT id FROM students WHERE id = %s"
        self.cursor.execute(check_query, (id,))
        existing_student = self.cursor.fetchone()
        if existing_student:
            self.cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            self.db.commit()
            self.update_files()
            return True
        else:
            return False

#------------------------------------------------------------------------------------------------------------------------------------------#

    def delete_students(self):
        check_query = "SELECT * FROM students"
        self.cursor.execute(check_query)
        existing_students = self.cursor.fetchone()
        if existing_students:
            self.cursor.execute('TRUNCATE TABLE students')
            self.db.commit()
            self.update_files()
            return True
        else:
            return False
        


