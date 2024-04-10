from models.company import Company
from sqlalchemy import create_engine
from models.base import Base
from models.financial import Financial
from utils.helper import show_crud_menu, show_main_menu, show_top_ten, read_csv, preprocess_data
from crud.operations import insert_data, select_data_from_company, select_financials


def import_data(engine):
    companies_data = read_csv('data/companies.csv')
    companies_data = preprocess_data(companies_data)
    insert_data(engine, Company, companies_data)

    financial_data = read_csv('data/financial.csv')
    financial_data = preprocess_data(financial_data)
    insert_data(engine, Financial, financial_data)


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


def read_company(engine):
    print("Enter company name:")
    name = input("")
    companies = select_data_from_company(engine, name)

    if len(companies) == 0:
        print("Company not found!")
    else:
        for index, company in enumerate(companies):
            print(f"{index} {company.name}")
        print("Enter a company number:")
        number = int(input(""))
        ticker = companies[number].ticker
        company_name = companies[number].name
        company_financials = select_financials(engine, ticker)
        company_financials.print_financials()


def crud_operations_menu(engine):
    show_crud_menu()
    print("Enter an option:")
    crud_operation = input("")

    if crud_operation in ["0", "3", "4", "5"]:
        print("Not implemented!")
    elif crud_operation == "1":
        create_company(engine)
    elif crud_operation == "2":
        read_company(engine)
    else:
        print("Invalid option!")


if __name__ == "__main__":
    engine = create_engine('sqlite:///investor.db')
    Base.metadata.create_all(engine)
    # import_data(engine)

    user_command = ""
    print("Welcome to the Investor Program!")
    while user_command != "0":

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
