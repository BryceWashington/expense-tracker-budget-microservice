from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import budget_router

import uvicorn

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domain
)

# add routers
app.include_router(budget_router.router)

@app.get("/")
async def root():
    return {"message": "Budget Service"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)