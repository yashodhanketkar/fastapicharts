from datetime import date

from pydantic import BaseModel, Field


class CustomerSchema(BaseModel):
    record_date: date = Field(...)
    chart_type: str = Field(...)
    customer_id: int = Field(...)
    customer_name: str = Field(...)
    days_overdue: int = Field(...)
    amount_outstanding: int = Field(...)
    recovery: int = Field(...)
