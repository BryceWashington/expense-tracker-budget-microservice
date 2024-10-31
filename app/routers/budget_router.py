from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from app.controllers import budget_controller
from app.models.budget_response import BudgetResponse, CreateBudgetResponse, BudgetsResponse, DeleteBudgetResponse, UpdateBudgetResponse
from app.models.budget_request import CreateBudgetRequest, UpdateBudgetRequest

router = APIRouter(prefix="/api/budgets", tags=["Budgets"])
prefix = "/api/budgets"
@router.get("", response_model=BudgetsResponse, status_code=status.HTTP_200_OK)
async def get_budgets(user_id: Optional[int] = None, limit: Optional[int] = 10, offset: Optional[int] = 0):
    try:
        budgets = budget_controller.get_budgets(user_id=user_id, limit=limit, offset=offset)

        #add links to each expense(HATEOAS)
        for i, budget in enumerate(budgets):
            budgets[i] = {
                "data": budget,
                "links": [
                    {
                        "rel": "self",
                        "href": f"{prefix}/{budget['id']}"
                    },
                    {
                        "rel": "update",
                        "href": f"{prefix}/{budget['id']}",
                        "method": "PUT"
                    },
                    {
                        "rel": "delete",
                        "href": f"{prefix}/{budget['id']}",
                        "method": "DELETE"
                    }
                ]
            }


        #add links after array of expenses data
        links = []
        if user_id:
            links.append({
                "rel": "self",
                "href": f"{prefix}?user_id={user_id}&limit={limit}&offset={offset}"
            })

            if len(budgets) == limit: #smaller len means that it is last page
                links.append({
                    "rel": "next",
                    "href": f"{prefix}?user_id={user_id}&limit={limit}&offset={limit + offset}"
                })

            if offset > 0: #it means that there are previous datas
                links.append({
                    "rel": "prev",
                    "href": f"{prefix}?user_id={user_id}&limit={limit}&offset={max(0, offset - limit)}"
                })

        else:
            links.append({
                "rel": "self",
                "href": f"{prefix}?limit={limit}&offset={offset}"
            })

            if len(budgets) == limit: #smaller len means that it is last page
                links.append({
                    "rel": "next",
                    "href": f"{prefix}?limit={limit}&offset={limit + offset}"
                })

            if offset > 0: #it means that there are previous datas
                links.append({
                    "rel": "prev",
                    "href": f"{prefix}?limit={limit}&offset={max(0, offset - limit)}"
                })


        return {
            "data": budgets,
            "links": links
        }

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error")

@router.get("/{budget_id}", response_model=BudgetResponse, status_code=status.HTTP_200_OK)
async def get_budget(budget_id: int):
    try:
        budget = budget_controller.get_budget_by_id(budget_id)
        if not budget:
            raise HTTPException(status_code=404, detail="Budget not found")

        return {
            "data": budget,
            "links": [
                {
                    "rel": "self",
                    "href": f"{prefix}/{budget['id']}"
                },
                {
                    "rel": "update",
                    "href": f"{prefix}/{budget['id']}",
                    "method": "PUT"
                },
                {
                    "rel": "delete",
                    "href": f"{prefix}/{budget['id']}",
                    "method": "DELETE"
                }
            ]
        }
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error")
    

@router.post("", response_model=CreateBudgetResponse, status_code=status.HTTP_201_CREATED)
async def create_budget(budget: CreateBudgetRequest):
    try:
        new_budget = budget_controller.create_budget(budget)

        if not new_budget:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Budget creation failed")

        return {
            "message": "Budget created",
            "data": new_budget,
            "links": [
                {
                    "rel": "self",
                    "href": f"{prefix}/{new_budget['id']}"
                },
                {
                    "rel": "update",
                    "href": f"{prefix}/{new_budget['id']}",
                    "method": "PUT"
                },
                {
                    "rel": "delete",
                    "href": f"{prefix}/{new_budget['id']}",
                    "method": "DELETE"
                }
            ]
        }

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error")

@router.put("/{budget_id}", response_model=UpdateBudgetResponse, status_code=status.HTTP_200_OK)
async def update_budget(budget_id: int, new_budget_data: UpdateBudgetRequest):
    try:
        current_budget = budget_controller.get_budget_by_id(budget_id)
        if not current_budget:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")

        updated_budget = budget_controller.update_budget(budget_id, current_budget, new_budget_data)

        if not updated_budget:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Budget update failed")


        return {
            "message": "Budget updated",
            "data": updated_budget,
            "links": [
                {
                    "rel": "self",
                    "href": f"{prefix}/{updated_budget['id']}"
                },
                {
                    "rel": "update",
                    "href": f"{prefix}/{updated_budget['id']}",
                    "method": "PUT"
                },
                {
                    "rel": "delete",
                    "href": f"{prefix}/{updated_budget['id']}",
                    "method": "DELETE"
                }
            ]
        }

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error")

@router.delete("/{budget_id}", response_model=DeleteBudgetResponse, status_code=status.HTTP_200_OK)
async def delete_budget(budget_id: int):
    try:
        budget = budget_controller.get_budget_by_id(budget_id)
        if not budget:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Budget not found")

        delete_success = budget_controller.delete_budget(budget_id)
        if not delete_success:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="failed to delete")

        # use this when want to send 200 for success instead of 204
        return {
            "message": "Budget deleted",
        }

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error")