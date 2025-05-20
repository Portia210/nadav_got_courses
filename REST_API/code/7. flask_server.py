from flask import Flask, request, jsonify

app = Flask(__name__)

students = [{"age":21,"id":1,"name":"John Doe"},{"age":22,"id":2,"name":"Jane Doe"}]

@app.route('/students', methods = ["GET"])
def getStudents():
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=["GET"])
def getStudent(student_id):
    for student in students:
        if student_id == student["id"]:
            return jsonify(student), 200
    return jsonify({"error": "Student not Found"}), 404

@app.route('/students', methods = ["POST"])
def addStudents():
    data = request.get_json()
    # check validation
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Bad request, data must include name and age"}) , 404
    new_student = {"name": data["name"], "age": data["age"], "id": students[1]["id"] + 1}
    students.append(new_student)
    return jsonify(new_student), 201


@app.route('/students/<int:student_id>', methods = ["DELETE"])
def deleteStudents(student_id):
    global students
    new_students = []
    for student in students:
        if student_id != student["id"]:
            new_students.append(student)
    students = new_students
    return jsonify({"message": "Student Deleted"})

@app.route('/students/<int:student_id>', methods = ["PUT"])
def updateStudent(student_id):
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Bad request, data must include name and age"}) , 404
    for student in students:
        if student_id == student["id"]:
            student["name"] = data["name"]
            student["age"] = data["age"]
            return jsonify(student), 200
            
    return jsonify({"error": "Student not Found"}), 404
    
if __name__ == "__main__":
    app.run(host = "127.0.0.1" , port=5000, debug=True)