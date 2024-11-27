from pydantic import BaseModel
from typing import List

class SeasonBaseSchema(BaseModel):
    year: int

class SeasonSchema(SeasonBaseSchema):
    id: int
    races: List["RaceBasicSchema"] = [] 

    class Config:
        orm_mode = True 

class SeasonBasicSchema(SeasonBaseSchema):
    id: int
    
    class Config:
        orm_mode = True 

class RaceBaseSchema(BaseModel):
    sequence: int
    short_name: str
    circuit_name: str

class RaceSchema(RaceBaseSchema):
    id: int
    season_id: int 

    season: SeasonBasicSchema 

    class Config:
        orm_mode = True

class RaceBasicSchema(RaceBaseSchema):
    id: int
    season_id: int 

    class Config:
        orm_mode = True 

class RaceCreationSchema(RaceBaseSchema):
    season_id: int 
