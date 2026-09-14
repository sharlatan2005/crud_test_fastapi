from pydantic import BaseModel, ConfigDict, Field, model_validator
from uuid import UUID
from models.enums import EmployeeRole


class EmployeeResponse(BaseModel):
    id: UUID
    name: str
    role: EmployeeRole

class EmployeeCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    role: EmployeeRole
    name: str = Field(min_length=3, max_length=50)

class EmployeeUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    role: EmployeeRole | None = None
    name: str | None = Field(default=None, min_length=3, max_length=50)

    @model_validator(mode="after")
    def validate_no_explicit_null(self):
        for field in self.model_fields_set:
            if getattr(self, field) is None:
                raise ValueError(f"{field} cannot be null")
        return self