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


def get_company_info() -> tuple:
    print("Enter ticker (in the format 'MOON'):")
    ticker = input("")
    print("Enter company (in the format 'Moon Corp'):")
    name = input("")
    print("Enter industries (in the format 'Technology'):")
    sector = input("")
    return ticker, name, sector


def get_company_financials() -> tuple:
    print("Enter ebitda (in the format '987654321'):")
    ebitda = float(input(""))
    print("Enter sales (in the format '987654321'):")
    sales = float(input(""))
    print("Enter net profit (in the format '987654321'):")
    net_profit = float(input(""))
    print("Enter market price (in the format '987654321'):")
    market_price = float(input(""))
    print("Enter net debt (in the format '987654321'):")
    net_debt = float(input(""))
    print("Enter assets (in the format '987654321'):")
    assets = float(input(""))
    print("Enter equity (in the format '987654321'):")
    equity = float(input(""))
    print("Enter cash equivalents (in the format '987654321'):")
    cash_equivalents = float(input(""))
    print("Enter liabilities (in the format '987654321'):")
    liabilities = float(input(""))
    return ebitda, sales, net_profit, market_price, net_debt, assets, equity, cash_equivalents, liabilities


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

