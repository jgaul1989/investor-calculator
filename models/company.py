from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Company(Base):
    __tablename__ = 'companies'
    ticker: Mapped[str] = mapped_column(String(), primary_key=True)
    name: Mapped[str] = mapped_column(String())
    sector: Mapped[str] = mapped_column(String())
