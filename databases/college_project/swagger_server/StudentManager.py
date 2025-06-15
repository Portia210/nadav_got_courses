from swagger_server.models.student import Student 
from sqlalchemy import create_engine, text
import Config


class StudentManager:
    def __init__(self):
        self.engine = create_engine(Config.DB_URI)
        self.table_name = Config.TABLE_NAME

    def _execute_query(self, query: str, params: dict = None) -> list:
        """Helper method to execute database queries with error handling"""
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text(query), params or {})
                return result.mappings().all()
        except Exception as e:
            raise Exception(f"Database error: {str(e)}")

    def _execute_transaction(self, query: str, params: dict = None) -> list:
        """Helper method to execute database transactions with error handling"""
        try:
            with self.engine.begin() as connection:
                result = connection.execute(text(query), params or {})
                return result.mappings().all()
        except Exception as e:
            raise Exception(f"Database transaction error: {str(e)}")

    def getAllStudents(self) -> list[Student]:
        """Retrieve all students as a list."""
        query = f"SELECT * FROM {self.table_name}"
        results = self._execute_query(query)
        return [Student.from_dict({**dict(row), "course": "no course"}) for row in results]

    def getStudentById(self, student_id: int) -> tuple[Student | None, int]:
        """Get a student by their ID.
        Returns:
            tuple: (Student object or None, status code)
        """
        query = f"SELECT * FROM {self.table_name} WHERE id = :id"
        results = self._execute_query(query, {'id': student_id})
        if not results:
            return {"message": f"Student with ID {student_id} does not exist"}, 404
        return Student.from_dict(dict(results[0])), 200

    def addStudent(self, student: Student) -> Student:
        """Add a new student to the database."""
        if not student.name or not student.email:
            return {"message": "Student name and email are required"}

        query = f"""
        INSERT INTO {self.table_name} (name, age, email) 
        VALUES (:name, :age, :email)
        RETURNING *
        """
        results = self._execute_transaction(query, student.to_dict())
        if not results:
            return {"message": "Failed to insert student"}, 500
        
        return Student.from_dict(dict(results[0]))

    def updateStudent(self, student_id: int, updated_student: Student) -> tuple[Student | dict, int]:
        """Update an existing student's information."""
        # Check if student exists first
        student, status = self.getStudentById(student_id)
        if status == 404:
            return {"message": f"Student with ID {student_id} does not exist"}, 404

        if not updated_student.name or not updated_student.email:
            return {"message": "Student name and email are required"}, 400
            
        updated_student.id = student_id
        query = f"""
        UPDATE {self.table_name}
        SET name = :name, age = :age, email = :email
        WHERE id = :id
        RETURNING *
        """
        results = self._execute_transaction(query, updated_student.to_dict())
        if not results:
            return {"message": "Failed to update student"}, 500
        
        return Student.from_dict(dict(results[0])), 200

    def deleteStudent(self, student_id: int) -> tuple[dict, int]:
        """Delete a student from the database."""
        # Check if student exists first
        student, status = self.getStudentById(student_id)
        if status == 404:
            return {"message": f"Student with ID {student_id} does not exist"}, 404
            
        query = f"""
        DELETE FROM {self.table_name}
        WHERE id = :id
        RETURNING *
        """
        results = self._execute_transaction(query, {'id': student_id})
        if not results:
            return {"message": "Failed to delete student"}, 500
            
        return {"message": "Student deleted successfully"}, 200
