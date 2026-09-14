from fastapi import APIRouter
from api.employee_schemas import EmployeeResponse, EmployeeCreate
from services.employee import create_employee

router = APIRouter(prefix="/v1")

@router.post("/employees", response_model=EmployeeResponse, status_code=201, tags=["employees"])
async def add_employee(
    payload: EmployeeCreate
) -> EmployeeResponse:
    return await create_employee(payload)