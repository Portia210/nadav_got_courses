from Person import Person
from inputs_validators import validate_string_input, validate_float_input


class Employee(Person):
    def __init__(self, id: int, name: str, age: int, company_name: str, salary: float):
        super().__init__(id, name, age)
        self.company_name = company_name
        self.salary = salary

    @classmethod
    def from_input(cls):
        """Create an Employee instance from user input."""
        base_data = cls.get_base_input()
        if base_data is None:
            return None

        company_name = validate_string_input("Enter Company name: ")
        if not company_name:
            return None

        salary = validate_float_input("Enter Salary: ")
        if not salary:
            return None

        return cls(**base_data, company_name=company_name, salary=salary)

    def __str__(self):
        return f"{super().__str__()}, his company name is {self.company_name}, his salary is {self.salary}"


if __name__ == "__main__":
    employee = Employee.from_input()
    print(employee)
