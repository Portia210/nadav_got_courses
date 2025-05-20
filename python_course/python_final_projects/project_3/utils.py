import os
import pandas as pd


def list_has_data(entries_list: list):
    if not entries_list:
        print("[Info] No entries available.")
        return False
    return True


def is_csv_file_up_to_date(entries_list: list, csv_file_path: str):
    if not os.path.exists(csv_file_path):
        return False
    df = pd.read_csv(csv_file_path).dropna(axis=0, how="all")
    existing_data = pd.DataFrame([
            {"class_name": entry.__class__.__name__, **entry.__dict__}
            for entry in entries_list
        ])
    return df.equals(existing_data)

