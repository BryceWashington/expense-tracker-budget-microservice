# Expense Tracker - Budget Microservice

# Endpoints - For details please check Swagger UI
## Endpoint: GET /api/budget?user_id={user_id}&limit={limit}&offset={offset}
### Response Codes:
- 200: Success
- 500: Internal Server Error

### Request and Response Example: GET /api/expenses?budget_id=1&limit=2&offset=5
#### response
```json
{
    "data": [
        {
            "data": {
                "id": 10,
                "amount": 18.00,
                "expense_date": "2024-10-15",
                "description": "salad",
                "created_at": "2024-10-19T22:50:26",
                "modified_at": "2024-10-19T22:50:26",
                "budget_id": 1
            },
            "links": [
                {
                    "rel": "self",
                    "href": "/api/expenses/10",
                    "method": "GET"
                },
                {
                    "rel": "update",
                    "href": "/api/expenses/10",
                    "method": "PUT"
                },
                {
                    "rel": "delete",
                    "href": "/api/expenses/10",
                    "method": "DELETE"
                }
            ]
        },
        {
            "data": {
                "id": 23,
                "amount": 244.00,
                "expense_date": "2024-10-15",
                "description": "pizza",
                "created_at": "2024-10-19T22:50:26",
                "modified_at": "2024-10-19T22:50:26",
                "budget_id": 1
            },
            "links": [
                {
                    "rel": "self",
                    "href": "/api/expenses/23",
                    "method": "GET"
                },
                {
                    "rel": "update",
                    "href": "/api/expenses/23",
                    "method": "PUT"
                },
                {
                    "rel": "delete",
                    "href": "/api/expenses/23",
                    "method": "DELETE"
                }
            ]
        }
      
    ],
    "links": [
        {
            "rel": "self",
            "href": "/api/expenses?budget_id=1&limit=2&offset=5",
            "method": "GET"
        },
        {
            "rel": "next",
            "href": "/api/expenses?budget_id=1&limit=2&offset=7",
            "method": "GET"
        },
        {
            "rel": "prev",
            "href": "/api/expenses?budget_id=1&limit=2&offset=3",
            "method": "GET"
        }
    ]
}
```

## Endpoint: GET /api/budget/{budget_id}
### Response Codes:
- 200: Success
- 404: Expense Not Found
- 500: Internal Server Error

### Request and Response Example: GET /api/expenses/21
#### response
```json
{
    "data": {
        "id": 21,
        "amount": 50.00,
        "expense_date": "2024-10-20",
        "description": "earbuds",
        "created_at": "2024-10-19T23:39:36",
        "modified_at": "2024-10-19T23:39:42",
        "budget_id": 30
    },
    "links": [
        {
            "rel": "self",
            "href": "/api/expenses/21",
            "method": "GET"
        },
        {
            "rel": "update",
            "href": "/api/expenses/21",
            "method": "PUT"
        },
        {
            "rel": "delete",
            "href": "/api/expenses/21",
            "method": "DELETE"
        }
    ]
}
```

## Endpoint: PUT /api/budget/{budget_id}
### Response Codes:
- 200: Expense Updated
- 404: Expense Not Found
- 500: Internal Server Error

### Request and Response Example: PUT /api/expenses/21
#### request body
```json
{
    "amount": 50.00,
    "expense_date": "2024-10-20",
    "description": "earbuds"
}
```
#### response
```json
{
    "message": "Expense updated",
    "data": {
        "id": 21,
        "amount": 50.00,
        "expense_date": "2024-10-20",
        "description": "earbuds",
        "created_at": "2024-10-19T23:39:36",
        "modified_at": "2024-10-19T23:39:42",
        "budget_id": 30
    },
    "links": [
        {
            "rel": "self",
            "href": "/api/expenses/21",
            "method": "GET"
        },
        {
            "rel": "update",
            "href": "/api/expenses/21",
            "method": "PUT"
        },
        {
            "rel": "delete",
            "href": "/api/expenses/21",
            "method": "DELETE"
        }
    ]
}
```

## Endpoint: POST /api/budgets
### Response Codes:
- 201: Expense Created
- 500: Internal Server Error

### Request and Response Example: POST /api/expenses
#### request body
```json
{
    "amount": 100.00,
    "expense_date": "2024-10-20",
    "description": "Big Pizza",
    "budget_id": 5
}
```
#### response
```json
{
    "message": "Expense created",
    "data": {
        "id": 20,
        "amount": 100.00,
        "expense_date": "2024-10-20",
        "description": "Big Pizza",
        "created_at": "2024-10-19T23:35:23",
        "modified_at": "2024-10-19T23:35:23",
        "budget_id": 5
    },
    "links": [
        {
            "rel": "self",
            "href": "/api/expenses/20",
            "method": "GET"
        },
        {
            "rel": "update",
            "href": "/api/expenses/20",
            "method": "PUT"
        },
        {
            "rel": "delete",
            "href": "/api/expenses/20",
            "method": "DELETE"
        }
    ]
}

```

## Endpoint: DELETE /api/budgets/{budget_id}
### Response Codes:
- 200: Expense Deleted
- 404: Expense Not Found
- 500: Internal Server Error

### Request and Response Example: DELETE /api/expenses/21
```json
{
    "message": "Expense deleted"
}
```

# File structure

```
├─ .env.sample
├─ .gitignore
├─ app
│  ├─ __init__.py
│  ├─ controllers
│  │  ├─ __init__.py
│  │  └─ budget_controller.py
│  ├─ db
│  │  ├─ __init__.py
│  │  └─ database.py
│  ├─ models
│  │  ├─ __init__.py
│  │  ├─ budget_request.py
│  │  └─ budget_response.py
│  ├─ routers
│  │  ├─ __init__.py
│  │  └─ budget_router.py
│  └─ utils
│     ├─ __init__.py
│     └─ config.py
├─ docs
│  └─ README.md
├─ main.py
└─ requirements.txt
```

# Short description of each files

```
main.py: Entry point for FastAPI

app/controllers: Business logic and handle mysql queries

app/db/database.py: Database connection setting

app/models/budget_request.py: Data models for budget requests. Good for autogenerated API documentation.

app/models/budget_response.py: Models for expense responses. Good for autogenerated API documentation.

app/routers: API endpoints

app/utils/config.py: configure settings using .env, in this project, configs are about MySQL
```

# How to run

## Database

![budget_database.png](budget_database.png)
### Create table query

```mysql
CREATE DATABASE IF NOT EXISTS budget_service;

USE budget_service;

CREATE TABLE IF NOT EXISTS budget_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS budgets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    budget_type_id INT NOT NULL,
    FOREIGN KEY (budget_type_id) REFERENCES budget_types(id)
);
```

### add dummy data

```mysql
USE budget_service;

INSERT INTO budget_types (name) VALUES 
    ('Food'),
    ('Transportation'),
    ('Entertainment');

INSERT INTO budgets (amount, start_date, end_date, user_id, budget_type_id) VALUES 
    (1500.50, '2024-01-01', '2024-01-31', 1, 1),
    (2500.75, '2024-01-01', '2024-01-31', 2, 2),
    (750.00, '2024-01-01', '2024-01-31', 3, 3);
```

## How to run locally

### Set Up Venv and activate

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Set Up .env

```
$ cp .env.sample .env

setup .env
```
