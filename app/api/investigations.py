from fastapi import APIRouter

from app.api.transactions import graph_service
from app.services.fraud_service import FraudService


router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"]
)


@router.get("/circular-flows")
def detect_circular_flows():

    fraud_service = FraudService(graph_service.graph)

    return {
        "patterns_detected": fraud_service.detect_circular_flows()
    }