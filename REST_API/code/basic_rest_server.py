import requests


# get request
def get_students():
    response = requests.get("http://127.0.0.1:5000/students")
    print(response.json())

# post request
def post_student(name, age):
    response = requests.post("http://127.0.0.1:5000/students", json={"name": name, "age": age})
    print(response.json())

# put request
def put_student(student_id, name, age):
    response = requests.put(f"http://127.0.0.1:5000/students/{student_id}", json={"name": name, "age": age})
    print(response.json())

# delete request
def delete_student(student_id):
    response = requests.delete(f"http://127.0.0.1:5000/students/{student_id}")
    print(response.json())


put_student(1, "nahman", 50)
delete_student(3)
get_students()
