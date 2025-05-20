import time
import os
import pandas as pd
from typing import Callable
from enum import Enum
from Person import Person
from Student import Student
from Employee import Employee
from utils import list_has_data, is_csv_file_up_to_date
from inputs_validators import validate_int_input, validate_choice_input
from dataclasses import dataclass, field
from typing import Dict, List


# Constants
MENU_DELAY = 0.5
CSV_FILE_PATH = "entries.csv"

# using dataclass to manage data, so I don't need to use global variables, in functions
@dataclass
class DataManager:
    entries_list: List = field(default_factory=list) # init an empty list
    entries_dict: Dict = field(default_factory=dict) # init an empty dict
    sum_ages: int = 0

# Create single instance
dm = DataManager()

def load_data() -> None:
    """Load data from CSV file into program memory."""
    if not os.path.exists(CSV_FILE_PATH):
        print("File not found. Data not loaded.")
        return
        
    try:
        df = pd.read_csv(CSV_FILE_PATH, index_col="class_name").dropna(axis=0, how="all")
        dm.entries_list = [
            eval(index)(**{k: v for k, v in row.items() if pd.notna(v)}) 
            for index, row in df.iterrows()
        ]
        dm.entries_dict = {entry.id: entry for entry in dm.entries_list}
        dm.sum_ages = sum(entry.age for entry in dm.entries_list)
        print(f"{len(dm.entries_list)} entries loaded successfully.")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {str(e)}")


# menu functions

def add_new_entry() -> None:
    """Add a new entry to the system."""
    person_type = validate_choice_input("Person type (p/s/e): ", ["p", "s", "e"])
    if person_type is None:
        return

    class_map = {"p": Person, "s": Student, "e": Employee}
    new_entry = class_map[person_type].from_input()

    if not new_entry:
        return

    if new_entry.id in dm.entries_dict:
        print(f"[Error] ID {new_entry.id} already exists:", dm.entries_dict[new_entry.id])
        return

    dm.entries_list.append(new_entry)
    dm.entries_dict[new_entry.id] = new_entry
    dm.sum_ages += new_entry.age
    print("New entry added successfully")


def search_by_id(entries_dict: dict):
    """Search for an entry by ID."""
    if id := validate_int_input("Enter ID to search: "):
        if entry := entries_dict.get(id):
            print(entry)
        else:
            print(f"[Error] ID {id} does not exist.")


def print_ages_average(entries_list: list, sum_ages: int):
    """Print the average age of all entries."""
    if list_has_data(entries_list):
        print(f"Ages average: {sum_ages / len(entries_list):.2f}")


def print_all_names(entries_list: list):
    """Print all names with their indices."""
    if list_has_data(entries_list):
        print("All names:")
        for i, entry in enumerate(entries_list):
            print(f"Index {i}) {entry.name}")


def print_all_ids(entries_list: list):
    """Print all IDs with their indices."""
    if list_has_data(entries_list):
        print("All IDs:")
        for i, entry in enumerate(entries_list):
            print(f"Index {i}) {entry.id}")


def print_all_entries(entries_list: list):
    """Print all entries with their indices."""
    if list_has_data(entries_list):
        print("All Entries:")
        for i, entry in enumerate(entries_list):
            print(f"Index {i}) {entry}")


def print_entry_by_index(entries_list: list):
    """Print a specific entry by its index."""
    if not list_has_data(entries_list):
        return
        
    if index := validate_int_input("Enter index: "):
        if 0 <= index < len(entries_list):
            print(f"Index {index}) {entries_list[index]}")
        else:
            print(f"[Error] Index out of range. Allowed: 0 to {len(entries_list) - 1}")


def save_data(entries_list: list):
    """Save current data to CSV file if changes exist."""
    if not list_has_data(entries_list):
        return

    if is_csv_file_up_to_date(entries_list, CSV_FILE_PATH):
        print("Data is already up to date.")
        return
    
    try:
        data_to_save = [
            {"class_name": entry.__class__.__name__, **entry.__dict__}
            for entry in entries_list
        ]
        pd.DataFrame(data_to_save).set_index("class_name").to_csv(CSV_FILE_PATH)
        print("Data saved successfully.")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {str(e)}")


def exit_program():
    """Exit the program, prompting to save only if data has changed."""
    if is_csv_file_up_to_date(dm.entries_list, CSV_FILE_PATH):
        print("Exiting... Goodbye!")
        exit()

    confirmation = validate_choice_input("Do you want to save the data before exiting? (y/n): ", ["y", "n"])
    
    if confirmation is None:
        return
        
    if confirmation == "y":
        save_data(dm.entries_list)
    
    print("Exiting... Goodbye!")
    exit()


class MenuOption(Enum):
    """Menu options enumeration."""
    ADD_ENTRY = ("Add a new entry", add_new_entry)
    SEARCH_BY_ID = ("Search by ID", lambda: search_by_id(dm.entries_dict))
    PRINT_AGES_AVG = ("Print ages average", lambda: print_ages_average(dm.entries_list, dm.sum_ages))
    PRINT_ALL_NAMES = ("Print all names", lambda: print_all_names(dm.entries_list))
    PRINT_ALL_IDS = ("Print all IDs", lambda: print_all_ids(dm.entries_list))
    PRINT_ALL_ENTRIES = ("Print all entries", lambda: print_all_entries(dm.entries_list))
    PRINT_ENTRY_BY_INDEX = ("Print entry by index", lambda: print_entry_by_index(dm.entries_list))
    SAVE_DATA = ("Save data", lambda: save_data(dm.entries_list))
    EXIT = ("Exit", exit_program)

    def __init__(self, display_text: str, function: Callable):
        self.display_text = display_text
        self.function = function


def run_menu():
    """Main program loop that handles the menu system and user interactions."""
    while True:
        try:
            print("\n--- Main Menu ---")
            for i, option in enumerate(MenuOption, 1):
                print(f"{i}. {option.display_text}")

            if choice := validate_int_input(f"Choice (1 to {len(MenuOption)}): "):
                if 1 <= choice <= len(MenuOption):
                    result = list(MenuOption)[choice - 1].function()
                    if result is not None:
                        dm.sum_ages = result
                    input("Press Enter to back to menu...")
                else:
                    print(f"[Error] Choice out of range. Please select between 1 and {len(MenuOption)}.")
                    time.sleep(MENU_DELAY)
        except KeyboardInterrupt:
            print("\n[Info] Operation cancelled with Ctrl+C, if you want to exit, please select the exit option.")
        except Exception as e:
            print(f"\n[Error] An unexpected error occurred: {str(e)}")

def main():
    """Program entry point."""
    load_data()
    run_menu()

if __name__ == "__main__":
    main()