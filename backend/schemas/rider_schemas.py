from pydantic import BaseModel

class RiderCreateSchema(BaseModel):
    name: str
    surname: str
    number: int
    country: str

class RiderSchema(RiderCreateSchema):
    id: int