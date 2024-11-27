from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.Season import Season, Race
from backend.schemas.season_schemas import SeasonBaseSchema, SeasonSchema, RaceSchema, RaceBasicSchema, RaceCreationSchema
from backend.utils.database import get_db

app = FastAPI()

# CRUD para Season

@app.post("/seasons/", response_model=SeasonSchema)
async def create_season(season: SeasonBaseSchema, db: Session = Depends(get_db)):
    db_season = Season(year=season.year)
    db.add(db_season)
    db.commit()
    db.refresh(db_season)
    return db_season

@app.get("/seasons/", response_model=List[SeasonSchema])
async def get_seasons(db: Session = Depends(get_db)):
    return db.query(Season).all()

@app.get("/seasons/{season_id}", response_model=SeasonSchema)
async def get_season(season_id: int, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    return db_season

@app.put("/seasons/{season_id}", response_model=SeasonSchema)
async def update_season(season_id: int, season: SeasonBaseSchema, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    db_season.year = season.year
    db.commit()
    db.refresh(db_season)
    return db_season

@app.delete("/seasons/{season_id}", response_model=SeasonSchema)
async def delete_season(season_id: int, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    db.delete(db_season)
    db.commit()
    return db_season

# CRUD para Race

@app.post("/races/", response_model=RaceSchema)
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

@app.get("/races/", response_model=List[RaceSchema])
async def get_races(db: Session = Depends(get_db)):
    return db.query(Race).all()

@app.get("/races/{race_id}", response_model=RaceSchema)
async def get_race(race_id: int, db: Session = Depends(get_db)):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race is None:
        raise HTTPException(status_code=404, detail="Race not found")
    return db_race

@app.put("/races/{race_id}", response_model=RaceSchema)
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

@app.delete("/races/{race_id}", response_model=RaceBasicSchema)
async def delete_race(race_id: int, db: Session = Depends(get_db)):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race is None:
        raise HTTPException(status_code=404, detail="Race not found")
    db.delete(db_race)
    db.commit()
    return db_race