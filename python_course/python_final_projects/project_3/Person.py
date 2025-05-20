from inputs_validators import validate_int_input, validate_string_input

class Person:
    def __init__(self, id: int, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

    @classmethod
    def get_base_input(cls):
        """Get base input for any person type."""
        id = validate_int_input("Enter ID: ")
        if not id:
            return None
            
        name = validate_string_input("Enter Name: ")
        if not name:
            return None
            
        age = validate_int_input("Enter Age: ")
        if not age:
            return None
            
        return {"id": id, "name": name, "age": age}

    @classmethod
    def from_input(cls):
        """Create a Person instance from user input."""
        base_data = cls.get_base_input()
        if not base_data:
            return None
        return cls(**base_data)

    def __str__(self):
        return f"{self.__class__.__name__} id is {self.id}, his name is {self.name}, his age is {self.age}"




if __name__ == "__main__":
    # Example 1: Using __dict__
    person = Person(1, "John", 20)
   