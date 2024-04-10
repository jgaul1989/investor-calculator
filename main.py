from models.company import Company
from sqlalchemy import create_engine
from models.base import Base
from models.financial import Financial
from utils.helper import (show_crud_menu, show_main_menu, show_top_ten, read_csv, preprocess_data,
                          get_company_info, get_company_financials)
from crud.operations import (insert_data, select_data_from_company, select_financials,
                             update_company_financial, delete_from_financial, delete_from_company, select_all_companies)


def import_data(engine):
    companies_data = read_csv('data/companies.csv')
    companies_data = preprocess_data(companies_data)
    insert_data(engine, Company, companies_data)

    financial_data = read_csv('data/financial.csv')
    financial_data = preprocess_data(financial_data)
    insert_data(engine, Financial, financial_data)


def select_company(engine):
    print("Enter company name:")
    name = input("")
    companies = select_data_from_company(engine, name)

    if len(companies) == 0:
        print("Company not found!")
        return None
    else:
        for index, company in enumerate(companies):
            print(f"{index} {company.name}")
        print("Enter a company number:")
        number = int(input(""))
        ticker = companies[number].ticker
        return select_financials(engine, ticker)


def top_ten_operations():
    show_top_ten()
    print("Enter an option:")
    command = input("")

    if command in ["0", "1", "2", "3"]:
        print("Not implemented!")
    else:
        print("Invalid option!")


def create_company(engine):
    ticker, name, sector = get_company_info()
    (ebitda, sales, net_profit, market_price, net_debt,
     assets, equity, cash_equivalents, liabilities) = get_company_financials()

    company = [{"ticker": ticker, "name": name, "sector": sector}]
    financial = [{"ticker": ticker, "ebitda": ebitda, "sales": sales, "net_profit": net_profit,
                  "market_price": market_price, "net_debt": net_debt, "assets": assets, "equity": equity,
                  "cash_equivalents": cash_equivalents, "liabilities": liabilities}]
    insert_data(engine, Company, company)
    insert_data(engine, Financial, financial)
    print("Company created successfully!")


def read_company(engine):
    company_financials = select_company(engine)
    if company_financials is not None:
        company_financials.print_financials()


def update_company(engine):
    company_financials = select_company(engine)
    if company_financials is not None:
        (ebitda, sales, net_profit, market_price, net_debt,
         assets, equity, cash_equivalents, liabilities) = get_company_financials()
        data = {'ebitda': ebitda, 'sales': sales, 'net_profit': net_profit, 'market_price': market_price,
                'net_debt': net_debt, 'assets': assets, 'equity': equity, 'cash_equivalents': cash_equivalents,
                'liabilities': liabilities}
        update_company_financial(engine, company_financials.ticker, data)
        print("Company updated successfully!")


def delete_company(engine):
    company_financials = select_company(engine)
    if company_financials is not None:
        delete_from_financial(engine, company_financials.ticker)
        delete_from_company(engine, company_financials.ticker)
        print("Company deleted successfully!")


def list_all_companies(engine):
    companies = select_all_companies(engine)
    for company in companies:
        print(f"{company}")


def crud_operations_menu(engine):
    show_crud_menu()
    print("Enter an option:")
    crud_operation = input("")

    if crud_operation == "0":
        pass
    elif crud_operation == "1":
        create_company(engine)
    elif crud_operation == "2":
        read_company(engine)
    elif crud_operation == "3":
        update_company(engine)
    elif crud_operation == "4":
        delete_company(engine)
    elif crud_operation == "5":
        list_all_companies(engine)
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
