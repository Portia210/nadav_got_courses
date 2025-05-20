import time

print("This is Final Project 1 - Special Calculator")
username = input("What is your name: ")
print(f"Hi {username}, Nice to meet you\nThis is a Special Calculator, please enter 2 numbers")
first_input = input("First Number: ").strip()
second_input = input("Second Number: ").strip()

if not first_input.isdigit() or not second_input.isdigit():
    print("Error: You must Enter only numbers, try again")
    exit()

first_number = int(first_input)
second_number = int(second_input)

first_number_even = first_number % 2 == 0
second_number_even = second_number % 2 == 0

if first_number_even and second_number_even:
    odd_or_even_result = "All numbers are even"
elif not first_number_even and not second_number_even:
    odd_or_even_result = "All numbers are odd"
else:
    odd_or_even_text = lambda x: "even" if x % 2 == 0 else "odd"
    odd_or_even_result = f"{first_number} is {odd_or_even_text(first_number)}, {second_number} is {odd_or_even_text(second_number)}"

print(odd_or_even_result)

allowed_operators = ["+", "-", "*", "/"]
operator_input = input(f"choose the oparation you'd like to perform (+-*/): ").strip()

if not operator_input in allowed_operators:
    print(f"Error: {operator_input} isn't a valid operator")
    exit()

if operator_input == "+": 
    result = first_number + second_number
elif operator_input == "-": 
    result = first_number - second_number
elif operator_input == "*": 
    result = first_number * second_number
elif operator_input == "/": 
    if second_number == 0:
        print(f"Error: second number is 0, cannot divide by zero")
        exit()
    correct_operation_input = input("You choose division, do you want the result as integer (y/n): ").strip()
    if correct_operation_input not in ["y", "n"]:
        print("Error: Invalid input, exiting...")
        exit()
    result_as_integer = correct_operation_input == "y"
    result = first_number // second_number if result_as_integer else first_number / second_number
else:
    print("Error: Invalid operator input")
    exit()
    
result_output = f"{first_number} {operator_input} {second_number} = {result}"
print(result_output)
print(f"Thank you for using the Calculator on {time.ctime()}")