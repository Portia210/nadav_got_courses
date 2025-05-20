from typing import Optional, Callable, Any


def get_validated_input(prompt: str, validator: Callable[[str], Any], error_message:  str = "Please Enter a valid input.") -> Optional[Any]:
    """Helper function to handle input validation with retry logic."""
    error_message = f"[Error] Invalid input. {error_message}"
    while True:
        value = input(prompt).strip()
        if value.lower() == "q":
            return None
        try:
            result = validator(value)
            if result is not None:
                return result
        except ValueError:
            print(error_message)
        print("Enter 'q' to cancel.")


def validate_int_input(prompt: str) -> Optional[int]:
    """Validate integer input."""
    return get_validated_input(prompt, lambda x: int(x), error_message="Please enter a valid integer.")


def validate_float_input(prompt: str) -> Optional[float]:
    """Validate float input."""
    return get_validated_input(prompt, lambda x: float(x), error_message="Please enter a valid float.")


def validate_string_input(prompt: str) -> Optional[str]:
    """Validate string input."""
    def string_validator(value: str) -> Optional[str]:
        return value if any(char.isalpha() for char in value) else None

    return get_validated_input(prompt, string_validator, error_message="Please enter a valid string.")

def validate_choice_input(prompt: str, choices: list) -> Optional[str]:
    """Validate choice input (strings)."""
    def choice_validator(value: str) -> str:
        if value not in choices:
            raise ValueError()
        return value
    return get_validated_input(prompt, choice_validator, error_message=f"Please enter a valid choice: {choices}.")