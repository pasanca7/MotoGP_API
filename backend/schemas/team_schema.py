from pydantic import BaseModel

class TeamCreateSchema(BaseModel):
    name: str
    factory: str

class TeamSchema(TeamCreateSchema):
    id: int