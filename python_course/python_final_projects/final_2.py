# 1) unite the text menu and the functions
# 2) convert the entries_data to an entries_list for a faster proccessing time by the index
# 3) convert functions to get the entry data as argument
# 4) better typing notation
import time


# helper functions
def _input_number(prompt: str):
    value = input(prompt).strip()
    return int(value) if value.isdigit() else None


def _has_data(entries_list: list):
    if not entries_list:
        print("[Info] No entries available.")
        return False
    return True


def _person_printer(entries_list: list, index: int, what_to_print: tuple = ('id', 'name', 'age')):
    entry_by_index = entries_list[index]
    custom_print_string = ', '.join([f'{word} is {entry_by_index[word]}' for word in what_to_print])
    print(f"Index {index}) {custom_print_string}")
    


# menu functions
def add_new_entry(state: dict):
    entries_list, entries_dict = state["entries_list"], state["entries_dict"]
    id = _input_number("ID (must be a number): ")
    if id is None:
        print("[Error] ID must be a number.")
        return
    existing_person = entries_dict.get(id)
    if existing_person:
        print("[Error] ID already exist.")
        print(f"id [{id}], name: {existing_person["name"]}, age: {existing_person["age"]}")
        return

    name = input("Name: ").strip()
    if not any(letter.isalpha() for letter in name):
        print("[Error] Name must contain English letters.")
        return

    age = _input_number("Age: ")
    if age is None:
        print("[Error] Age must be a number.")
        return

    entries_list.append({"id": id, "name": name, "age": age})
    entries_dict[id] = {"name": name, "age": age}
    state["sum_ages"] += age
    _person_printer(entries_list, len(entries_list)-1)


def search_by_id(state: dict):
    entries_dict = state["entries_dict"]
    search_id = _input_number("Enter ID to search: ")
    if search_id is None:
        print("[Error] ID must be a number.")
        return
    person = entries_dict.get(search_id)
    if person:
        print(f"id [{search_id}], name: {person["name"]}, age: {person["age"]}")
    else:
        print(f"[Error] ID {search_id} does not exist.")


def print_ages_average(state: dict):
    entries_list = state["entries_list"]
    sum_ages = state["sum_ages"]
    if not _has_data(entries_list): return
    average_age = sum_ages / len(entries_list)
    print(f"Ages average: {average_age:.2f}")


def print_all_names(state: dict):
    entries_list = state["entries_list"]
    if not _has_data(entries_list): return
    print("All names:")
    for index in range(len(entries_list)):
        _person_printer(entries_list, index, what_to_print=("name",))
        

def print_all_ids(state: dict):
    entries_list = state["entries_list"]
    if not _has_data(entries_list): return
    print("All IDs:")
    for index in range(len(entries_list)):
        _person_printer(entries_list, index, ("id",))


def print_all_entries(state: dict):
    entries_list = state["entries_list"]
    if not _has_data(entries_list): return
    print("All Entries:")
    for index in range(len(entries_list)):
        _person_printer(entries_list, index)


def print_entry_by_index(state: dict):
    entries_list = state["entries_list"]
    if not _has_data(entries_list): return
    index = _input_number("Enter index: ")
    if index is None:
        print("[Error] Invalid index.")
        return
    if not 0 <= index < len(entries_list):
        print(f"[Error] Index out of range. Allowed: 0 to {len(entries_list)-1}")
        return
    _person_printer(entries_list, index)    


def exit_program():
    while True:
        confirmation = input("Are you sure you want to exit? (y/n): ").strip().lower()
        if confirmation == "y":
            print("Exiting... Goodbye!")
            exit()
        elif confirmation == "n":
            print("Returning to menu...")
            return
        print("[Error] Please enter 'y' or 'n'.")


# menu function
def run_menu():
    MENU_OPTIONS = [
    ("Add a new entry", lambda x: add_new_entry(x)),  # returns a new list
    ("Search by ID", lambda x: search_by_id(x)),
    ("Print ages average", lambda x: print_ages_average(x)),
    ("Print all names", lambda x: print_all_names(x)),
    ("Print all IDs", lambda x: print_all_ids(x)),
    ("Print all entries", lambda x: print_all_entries(x)),
    ("Print entry by index", lambda x: print_entry_by_index(x)),
    ("Exit", lambda _: exit_program())  
]
    state = {
    "entries_list": [],
    "entries_dict": {},
    "sum_ages": 0
}
    while True:
        print("\n--- Main Menu ---")
        for menu_index, (message, _) in enumerate(MENU_OPTIONS, start=1):
            print(f"{menu_index}. {message}")
        
        selected_option = _input_number(f"Enter your choice (1 to {len(MENU_OPTIONS)}): ")
        if selected_option is None or not 1 <= selected_option <= len(MENU_OPTIONS):
            print(f"[Error] Choice out of range. Please select between 1 and {len(MENU_OPTIONS)}.")
            time.sleep(0.5)
            continue

        MENU_OPTIONS[selected_option - 1][1](state)
        time.sleep(0.5)

run_menu()
