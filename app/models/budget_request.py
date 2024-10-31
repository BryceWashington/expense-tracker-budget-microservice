from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from datetime import date

class CreateBudgetRequest(BaseModel):
    amount: float
    start_date: date
    end_date: date
    user_id: int

class UpdateBudgetRequest(BaseModel):
    amount: Optional[float] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

