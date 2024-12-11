from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime,date

class Link(BaseModel):
    rel: str
    href: str
    method: Optional[str] = "GET"

class BudgetData(BaseModel):
    id: int
    amount: float
    start_date: date
    end_date: date
    created_at: datetime
    modified_at: datetime
    user_id: int
    budget_type_id: str

class BudgetResponse(BaseModel):
    data: BudgetData
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "data": {
                    "id": 1,
                    "amount": 1500.5,
                    "start_date": "2024-01-01",
                    "end_date": "2024-01-31",
                    "created_at": "2024-10-01T17:58:20",
                    "modified_at": "2024-10-01T17:58:20",
                    "user_id": 1,
                    "budget_type_id": "Food"
                },
                "links": [
                    {
                        "rel": "self",
                        "href": "/api/budgets/1",
                        "method": "GET"
                    },
                    {
                        "rel": "update",
                        "href": "/api/budgets/1",
                        "method": "PUT"
                    },
                    {
                        "rel": "delete",
                        "href": "/api/budgets/1",
                        "method": "DELETE"
                    }
                ]
            }
        }


class BudgetsResponse(BaseModel):
    data: List[BudgetResponse]
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "data": [
                    {
                        "data": {
                            "id": 1,
                            "amount": 1500.5,
                            "start_date": "2024-01-01",
                            "end_date": "2024-01-31",
                            "created_at": "2024-10-01T17:58:20",
                            "modified_at": "2024-10-01T17:58:20",
                            "user_id": 1,
                            "budget_type_id": "Food"
                        },
                        "links": [
                            {
                                "rel": "self",
                                "href": "/api/budgets/1",
                                "method": "GET"
                            },
                            {
                                "rel": "update",
                                "href": "/api/budgets/1",
                                "method": "PUT"
                            },
                            {
                                "rel": "delete",
                                "href": "/api/budgets/1",
                                "method": "DELETE"
                            }
                        ]
                    },
                    {
                        "data": {
                            "id": 2,
                            "amount": 2500.75,
                            "start_date": "2024-01-01",
                            "end_date": "2024-01-31",
                            "created_at": "2024-10-01T17:58:20",
                            "modified_at": "2024-10-01T17:58:20",
                            "user_id": 2,
                            "budget_type_id": "Transportation"
                        },
                        "links": [
                            {
                                "rel": "self",
                                "href": "/api/budgets/2",
                                "method": "GET"
                            },
                            {
                                "rel": "update",
                                "href": "/api/budgets/2",
                                "method": "PUT"
                            },
                            {
                                "rel": "delete",
                                "href": "/api/budgets/2",
                                "method": "DELETE"
                            }
                        ]
                    }
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "/api/budgets?user_id=1&limit=2&offset=5",
                        "method": "GET"
                    },
                    {
                        "rel": "next",
                        "href": "/api/budgets?user_id=1&limit=2&offset=7",
                        "method": "GET"
                    },
                    {
                        "rel": "prev",
                        "href": "/api/budgets?user_id=1&limit=2&offset=3",
                        "method": "GET"
                    }
                ]
            }
        }


class CreateBudgetResponse(BaseModel):
    message: str
    data: BudgetData
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Budget created",
                "data": {
                    "id": 2,
                    "amount": 2500.75,
                    "start_date": "2024-01-01",
                    "end_date": "2024-01-31",
                    "created_at": "2024-10-01T17:58:20",
                    "modified_at": "2024-10-01T17:58:20",
                    "user_id": 2,
                    "budget_type_id": "Transportation"
                },
                "links": [
                    {
                        "rel": "self",
                        "href": "/api/budgets/2",
                        "method": "GET"
                    },
                    {
                        "rel": "update",
                        "href": "/api/budgets/2",
                        "method": "PUT"
                    },
                    {
                        "rel": "delete",
                        "href": "/api/budgets/2",
                        "method": "DELETE"
                    }
                ]
            }
        }


class UpdateBudgetResponse(BaseModel):
    message: str
    data: BudgetData
    links: List[Link]

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Budget created",
                "data": {
                    "id": 2,
                    "amount": 2500.75,
                    "start_date": "2024-01-01",
                    "end_date": "2024-01-31",
                    "created_at": "2024-10-01T17:58:20",
                    "modified_at": "2024-10-01T17:58:20",
                    "user_id": 2,
                    "budget_type_id": "Transportation"
                },
                "links": [
                    {
                        "rel": "self",
                        "href": "/api/budgets/2",
                        "method": "GET"
                    },
                    {
                        "rel": "update",
                        "href": "/api/budgets/2",
                        "method": "PUT"
                    },
                    {
                        "rel": "delete",
                        "href": "/api/budgets/2",
                        "method": "DELETE"
                    }
                ]
            }
        }


class DeleteBudgetResponse(BaseModel):
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Budget deleted"
            }
        }