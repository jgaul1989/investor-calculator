from models.company import Company
from sqlalchemy import create_engine
from models.base import Base
from models.financial import Financial
from utils.helper import read_csv, preprocess_data
from crud.operations import insert_data


def show_main_menu():
    print("MAIN MENU")
    print("0 Exit")
    print("1 CRUD operations")
    print("2 Show top ten companies by criteria")


def show_crud_menu():
    print("CRUD MENU")
    print("0 Back")
    print("1 Create a company")
    print("2 Read a company")
    print("3 Update a company")
    print("4 Delete a company")
    print("5 List all companies")


def show_top_ten():
    print("TOP TEN MENU")
    print("0 Back")
    print("1 List by ND/EBITDA")
    print("2 List by ROE")
    print("3 List by ROA")


def top_ten_operations():
    show_top_ten()
    print("Enter an option:")
    command = input("")

    if command in ["0", "1", "2", "3"]:
        print("Not implemented!")
    else:
        print("Invalid option!")


def create_company(engine):
    print("Enter ticker (in the format 'MOON'):")
    ticker = input("")
    print("Enter company (in the format 'Moon Corp'):")
    name = input("")
    print("Enter industries (in the format 'Technology'):")
    sector = input("")
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

    company = [{"ticker": ticker, "name": name, "sector": sector}]
    financial = [{"ticker": ticker, "ebitda": ebitda, "sales": sales, "net_profit": net_profit,
                  "market_price": market_price, "net_debt": net_debt, "assets": assets, "equity": equity,
                  "cash_equivalents": cash_equivalents, "liabilities": liabilities}]
    insert_data(engine, Company, company)
    insert_data(engine, Financial, financial)
    print("Company created successfully!")


def crud_operations_menu(engine):
    show_crud_menu()
    print("Enter an option:")
    crud_operation = input("")

    if crud_operation in ["0", "2", "3", "4", "5"]:
        print("Not implemented!")
    elif crud_operation == "1":
        create_company(engine)
    else:
        print("Invalid option!")


def import_data(engine):
    companies_data = read_csv('data/companies.csv')
    companies_data = preprocess_data(companies_data)
    insert_data(engine, Company, companies_data)

    financial_data = read_csv('data/financial.csv')
    financial_data = preprocess_data(financial_data)
    insert_data(engine, Financial, financial_data)


if __name__ == "__main__":
    engine = create_engine('sqlite:///investor.db')
    Base.metadata.create_all(engine)
    # import_data(engine)

    user_command = ""

    while user_command != "0":
        print("Welcome to the Investor Program!")
        show_main_menu()
        print("Enter an option:")
        user_command = input("")

        if user_command == "1":
            crud_operations_menu(engine)
        elif user_command == "2":
            top_ten_operations()
        elif user_command not in ["0", "1", "2"]:
            print("Invalid option!")

    print("Have a nice day!")
