from .base import Base
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Financial(Base):
    __tablename__ = 'financial'
    ticker: Mapped[str] = mapped_column(String(), primary_key=True)
    ebitda: Mapped[float] = mapped_column(Float(), nullable=True)
    sales: Mapped[float] = mapped_column(Float(), nullable=True)
    net_profit: Mapped[float] = mapped_column(Float(), nullable=True)
    market_price: Mapped[float] = mapped_column(Float(), nullable=True)
    net_debt: Mapped[float] = mapped_column(Float(), nullable=True)
    assets: Mapped[float] = mapped_column(Float(), nullable=True)
    equity: Mapped[float] = mapped_column(Float(), nullable=True)
    cash_equivalents: Mapped[float] = mapped_column(Float(), nullable=True)
    liabilities: Mapped[float] = mapped_column(Float(), nullable=True)
