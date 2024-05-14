from flask import Flask, jsonify, request
from student_service import StudentService

app = Flask(__name__)
service = StudentService()

@app.route('/students', methods=['GET'])
def get_students():
    data = service.get_students()
    return jsonify(data), 200

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    data = service.get_student(id)
    if data:
        return jsonify(data), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    service.delete_student(id)
    return '', 204

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    service.update_student(id, data)
    return '', 204

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    service.add_student(data)
    return '', 201

if __name__ == '__main__':
    app.run(debug=True)
