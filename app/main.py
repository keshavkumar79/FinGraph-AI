from fastapi import FastAPI

from app.api.transactions import router as transaction_router
from app.api.investigations import router as investigation_router
from app.api.accounts import router as account_router


app = FastAPI(
    title="FinGraph AI",
    description="AI-powered financial crime network detection system",
    version="0.1.0"
)


app.include_router(transaction_router)
app.include_router(investigation_router)
app.include_router(account_router)


@app.get("/")
def root():

    return {
        "message": "FinGraph AI backend is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }