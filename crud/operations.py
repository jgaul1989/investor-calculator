from sqlalchemy.orm import Session
from sqlalchemy import select
from models.company import Company


def insert_data(engine, model_class, data):
    with Session(engine) as session:
        for record in data:
            instance = model_class(**record)
            session.add(instance)
        session.commit()


def select_data_from_company(engine, search_string):
    with Session(engine) as session:
        # Construct a query to select companies where the name contains `search_string`
        stmt = select(Company).where(Company.name.like(f"%{search_string}%"))
        result = session.execute(stmt)

        # Fetch all results
        companies = result.scalars().all()
        return companies