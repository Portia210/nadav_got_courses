from Person import Person
from inputs_validators import validate_int_input, validate_string_input, validate_float_input


class Student(Person):
    def __init__(self, id: int, name: str, age: int, field_of_study: str, year_of_study: int, score_avg: float):
        super().__init__(id, name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg
    
    @classmethod
    def from_input(cls):
        """Create a Student instance from user input."""
        base_data = cls.get_base_input()
        if base_data is None:
            return None
            
        field_of_study = validate_string_input("Enter field of study: ")
        if not field_of_study:
            return None
            
        year_of_study = validate_int_input("Enter year of study: ")
        if not year_of_study:
            return None
            
        score_avg = validate_float_input("Enter average score: ")
        if not score_avg:
            return None
            
        return cls(**base_data, field_of_study=field_of_study, year_of_study=year_of_study, score_avg=score_avg)
            
    def __str__(self):
        return f"{super().__str__()}, his field of study is {self.field_of_study}, his year of study is {self.year_of_study}, his score average is {self.score_avg}"
    

if __name__ == "__main__":
    student = Student(1, "John", 20, "Computer Science", 2, 85.5)
    print(student)
