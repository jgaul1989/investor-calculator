from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from models.company import Company
from models.financial import Financial


def insert_data(engine, model_class, data):
    with Session(engine) as session:
        for record in data:
            instance = model_class(**record)
            session.add(instance)
        session.commit()


def update_company_financial(engine, ticker, data):
    with Session(engine) as session:
        stmt = select(Financial).where(Financial.ticker == ticker)
        result = session.scalars(stmt).one()
        for key, value in data.items():
            if hasattr(result, key):
                setattr(result, key, value)
        session.commit()


def delete_from_company(engine, ticker):
    with Session(engine) as session:
        stmt = delete(Company).where(Company.ticker == ticker)
        session.execute(stmt)
        session.commit()


def delete_from_financial(engine, ticker):
    with Session(engine) as session:
        stmt = delete(Financial).where(Financial.ticker == ticker)
        session.execute(stmt)
        session.commit()


def select_all_companies(engine):
    with Session(engine) as session:
        stmt = select(Company).order_by(Company.ticker)
        result = session.execute(stmt)
        companies = result.scalars().all()
        return companies


def select_data_from_company(engine, search_string):
    with Session(engine) as session:
        # Construct a query to select companies where the name contains `search_string`
        stmt = select(Company).where(Company.name.like(f"%{search_string}%"))
        result = session.execute(stmt)
        companies = result.scalars().all()
        return companies


def select_company_with_ticker(engine, ticker):
    with Session(engine) as session:
        stmt = select(Company).where(Company.ticker == ticker)
        result = session.execute(stmt)
        company = result.scalars().one()
        return company


def select_top_10_tickers_by_nd_ebitda(engine):
    with Session(engine) as session:
        nd_ebitda = (Financial.net_debt / Financial.ebitda).label('ND/EBITDA')
        stmt = (
            select(Financial.ticker, nd_ebitda)
            .order_by(nd_ebitda.desc())
            .limit(10)
        )
        result = session.execute(stmt)
        data = result.all()
        return data


def select_top_10_tickers_roe(engine):
    with Session(engine) as session:
        roe = (Financial.net_profit / Financial.equity).label('ROE')
        stmt = (
            select(Financial.ticker, roe)
            .order_by(roe.desc())
            .limit(10)
        )
        result = session.execute(stmt)
        data = result.all()
        return data


def select_top_10_tickers_roa(engine):
    with Session(engine) as session:
        roa = (Financial.net_profit / Financial.assets).label('ROA')
        stmt = (
            select(Financial.ticker, roa)
            .order_by(roa.desc())
            .limit(10)
        )
        result = session.execute(stmt)
        data = result.all()
        return data


def select_financials(engine, ticker):
    with Session(engine) as session:
        stmt = select(Financial).where(Financial.ticker == ticker)
        result = session.execute(stmt)
        financials = result.scalars().one()
        return financials