from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend.models.Season import Race
from backend.schemas.season_schemas import RaceSchema, RaceCreationSchema, RaceBasicSchema
from backend.utils.database import get_db

router = APIRouter(prefix="/races", tags=["Races"])

# CRUD Race

@router.post("/", response_model=RaceSchema)
async def create_race(race: RaceCreationSchema, db: Session = Depends(get_db)):
    db_race = Race(
        sequence=race.sequence,
        short_name=race.short_name,
        circuit_name=race.circuit_name,
        season_id=race.season_id
    )
    db.add(db_race)
    db.commit()
    db.refresh(db_race)
    return db_race

@router.get("/", response_model=List[RaceSchema])
async def get_races(db: Session = Depends(get_db)):
    return db.query(Race).all()

@router.get("/{race_id}", response_model=RaceSchema)
async def get_race(race_id: int, db: Session = Depends(get_db)):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race is None:
        raise HTTPException(status_code=404, detail="Race not found")
    return db_race

@router.put("/{race_id}", response_model=RaceSchema)
async def update_race(race_id: int, race: RaceCreationSchema, db: Session = Depends(get_db)):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race is None:
        raise HTTPException(status_code=404, detail="Race not found")
    db_race.sequence = race.sequence
    db_race.short_name = race.short_name
    db_race.circuit_name = race.circuit_name
    db_race.season_id = race.season_id
    db.commit()
    db.refresh(db_race)
    return db_race

@router.delete("/{race_id}", response_model=RaceBasicSchema)
async def delete_race(race_id: int, db: Session = Depends(get_db)):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race is None:
        raise HTTPException(status_code=404, detail="Race not found")
    db.delete(db_race)
    db.commit()
    return db_race