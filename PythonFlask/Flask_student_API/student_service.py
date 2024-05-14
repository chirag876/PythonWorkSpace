from student import Student
import json

class StudentService:
    def __init__(self):
        self.students = [
            Student(1, 'Chirag', 21, 'A'),
            Student(2, 'Mira', 23, 'B'),
            Student(3, 'Aman', 19, 'C')
        ]
        self.next_id = 4

    def get_students(self):
        return json.dumps([s.__dict__ for s in self.students])

    def get_student(self, id):
        for s in self.students:
            if s.id == id:
                return s.__dict__
        return None

    def delete_student(self, id):
        for i, s in enumerate(self.students):
            if s.id == id:
                del self.students[i]
                break

    def update_student(self, id, data):
        for s in self.students:
            if s.id == id:
                if 'name' in data:
                    s.name = data['name']
                if 'age' in data:
                    s.age = data['age']
                if 'grade' in data:
                    s.grade = data['grade']
                break

    def add_student(self, data):
        student = Student(self.next_id, data['name'], data['age'], data['grade'])
        self.students.append(student)
        self.next_id += 1
