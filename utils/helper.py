import csv


def read_csv(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def show_main_menu():
    print("")
    print("MAIN MENU")
    print("0 Exit")
    print("1 CRUD operations")
    print("2 Show top ten companies by criteria\n")


def show_crud_menu():
    print("")
    print("CRUD MENU")
    print("0 Back")
    print("1 Create a company")
    print("2 Read a company")
    print("3 Update a company")
    print("4 Delete a company")
    print("5 List all companies\n")


def show_top_ten():
    print("TOP TEN MENU")
    print("0 Back")
    print("1 List by ND/EBITDA")
    print("2 List by ROE")
    print("3 List by ROA")


def preprocess_data(data_set):
    for data in data_set:
        for key, value in data.items():
            if value == '':  # Check for empty strings
                data[key] = None  # Replace empty strings with None
    return data_set


def safe_divide_and_round(numerator, denominator, digits=2):
    try:
        return round(numerator / denominator, digits) if denominator else None
    except TypeError:
        return None

