from sqlalchemy.orm import Session


def insert_data(engine, model_class, data):
    with Session(engine) as session:
        for record in data:
            instance = model_class(**record)
            session.add(instance)
        session.commit()