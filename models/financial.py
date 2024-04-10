from .base import Base
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from utils.helper import safe_divide_and_round


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

    def print_financials(self, company_name: str):
        print(f"{self.ticker} {company_name}")
        print(f"P/E = {safe_divide_and_round(self.market_price, self.net_profit)}")
        print(f"P/S = {safe_divide_and_round(self.market_price, self.sales)}")
        print(f"P/B = {safe_divide_and_round(self.market_price, self.assets)}")
        print(f"ND/EBITDA = {safe_divide_and_round(self.net_debt, self.ebitda)}")
        print(f"ROE = {safe_divide_and_round(self.net_profit, self.equity)}")
        print(f"ROA = {safe_divide_and_round(self.net_profit, self.assets)}")
        print(f"L/A = {safe_divide_and_round(self.liabilities, self.assets)}")
