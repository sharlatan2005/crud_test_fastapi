from models.base import Base
from models.enums import EmployeeRole
from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Enum,
    Text,
    text
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID

UUID_TYPE = PGUUID(as_uuid=True)

def enum_type(enum_class, name: str) -> Enum:
    return Enum(enum_class, name=name, values_callable=lambda items: [item.value for item in items])

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[UUID] = mapped_column(UUID_TYPE, primary_key=True, server_default=text("gen_random_uuid()"))

    name: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[EmployeeRole] = mapped_column(enum_type(EmployeeRole, "employee_role"))