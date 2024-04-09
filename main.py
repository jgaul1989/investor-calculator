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


def crud_operations():
    show_crud_menu()
    print("Enter an option:")
    crud_operation = input("")

    if crud_operation in ["0", "1", "2", "3", "4", "5"]:
        print("Not implemented!")
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
    import_data(engine)

    user_command = ""

    while user_command != "0":
        print("Welcome to the Investor Program!")
        show_main_menu()
        print("Enter an option:")
        user_command = input("")

        if user_command == "1":
            crud_operations()
        elif user_command == "2":
            top_ten_operations()
        elif user_command not in ["0", "1", "2"]:
            print("Invalid option!")

    print("Have a nice day!")
