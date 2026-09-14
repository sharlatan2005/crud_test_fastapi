from uuid import UUID, uuid4
from api.employee_schemas import EmployeeResponse, EmployeeCreate
from models.entities import Employee
from db.db import async_session_factory

async def create_employee(payload: EmployeeCreate) -> EmployeeResponse:
    async with async_session_factory() as session, session.begin():
        employee = Employee(
            id=uuid4(),
            name=payload.name,
            role=payload.role
        )
        session.add(employee)
    return EmployeeResponse(id=employee.id, name=employee.name, role=employee.role)