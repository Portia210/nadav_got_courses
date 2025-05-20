import requests
from inputs_validators import validate_int_input, validate_string_input, validate_choice_input


BASE_URL = "http://13.220.23.193:5000/students"

def get_student_list():
    response = requests.get(BASE_URL)
    status_code = response.status_code
    if status_code == 200:
        students = response.json()["students"]
        print("Students list:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    else:
        print(f"Failed to get student list. status code: {status_code}")

def get_user_info_by_id():
    id = validate_int_input("Enter the id of the student: ")
    response = requests.get(f"{BASE_URL}/{id}")
    status_code = response.status_code
    if status_code == 200:
        print("Student info:")
        student = response.json()
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    else:
        print(f"Failed to get user info by id. status code: {status_code}")

def save_new_student():
    name = validate_string_input("Enter the name of the student: ")
    age = validate_int_input("Enter the age of the student: ")
    response = requests.post(BASE_URL, json={"name": name, "age": age})
    status_code = response.status_code
    if status_code == 201:
        print("Student saved successfully")
    else:
        print(f"Failed to save new student. status code: {status_code}")

def update_student_info():
    id = validate_int_input("Enter the id of the student: ")
    name = validate_string_input("Enter the new name of the student: ")
    age = validate_int_input("Enter the new age of the student: ")
    response = requests.put(f"{BASE_URL}/{id}", json={"name": name, "age": age})
    status_code = response.status_code
    if status_code in [200, 204]:
        print("Student info updated successfully")
    else:
        print(f"Failed to update student info. status code: {status_code}")
    

def update_student_name():
    id = validate_int_input("Enter the id of the student: ")
    name = validate_string_input("Enter the new name of the student: ")
    full_student_info = requests.get(f"{BASE_URL}/{id}")

    if not full_student_info.status_code == 200:
        print(f"Failed to get student info. status code: {full_student_info.status_code}")
        return
    
    full_student_info = full_student_info.json()
    full_student_info["name"] = name
    response = requests.put(f"{BASE_URL}/{id}", json=full_student_info)
    
    status_code = response.status_code
    if status_code in [200, 204]:
        print("Student name updated successfully")
    else:
        print(f"Failed to update student name. status code: {status_code}")

def update_student_age():
    id = validate_int_input("Enter the id of the student: ")
    age = validate_int_input("Enter the new age of the student: ")
    full_student_info = requests.get(f"{BASE_URL}/{id}")
    
    if not full_student_info.status_code == 200:
        print(f"Failed to get student info. status code: {full_student_info.status_code}")
        return
    
    full_student_info = full_student_info.json()
    full_student_info["age"] = age
    response = requests.put(f"{BASE_URL}/{id}", json=full_student_info)
    status_code = response.status_code
    if status_code in [200, 204]:
        print("Student age updated successfully")
    else:
        print(f"Failed to update student age. status code: {status_code}")

def delete_student():
    id = validate_int_input("Enter the id of the student: ")
    response = requests.delete(f"{BASE_URL}/{id}")
    status_code = response.status_code
    if status_code in [200, 204]:
        print("Student deleted successfully")
    else:
        print(f"Failed to delete student. status code: {status_code}")

MENU_OPTIONS = [
    ("Get a student list", lambda: get_student_list()),
    ("Get user info by id", lambda: get_user_info_by_id()),
    ("Save a new student", lambda: save_new_student()),
    ("Update student info", lambda: update_student_info()),
    ("Update student name", lambda: update_student_name()),
    ("Update student age", lambda: update_student_age()),
    ("Delete a student", lambda: delete_student()),
    ("Exit", lambda: exit())
]

def menu():

    while True:
        try:
            for index, option in enumerate(MENU_OPTIONS, start=1):
                print(f"{index}. {option[0]}")

            choice = validate_choice_input("Enter your choice: ", list(map(str, range(1, len(MENU_OPTIONS) + 1))))
            if not choice:
                print("Invalid choice. Please try again.")
                continue
            correct_choice = int(choice) - 1
            print("--------------------------------")
            MENU_OPTIONS[correct_choice][1]()
            print("--------------------------------")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Exiting the program.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    menu()



