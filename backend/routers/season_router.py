from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend.models.Season import Season
from backend.schemas.season_schemas import SeasonBaseSchema, SeasonSchema
from backend.utils.database import get_db

router = APIRouter(prefix="/seasons", tags=["seasons"])

# CRUD Season

@router.post("/seasons/", response_model=SeasonSchema)
async def create_season(season: SeasonBaseSchema, db: Session = Depends(get_db)):
    db_season = Season(year=season.year)
    db.add(db_season)
    db.commit()
    db.refresh(db_season)
    return db_season

@router.get("/seasons/", response_model=List[SeasonSchema])
async def get_seasons(db: Session = Depends(get_db)):
    return db.query(Season).all()

@router.get("/seasons/{season_id}", response_model=SeasonSchema)
async def get_season(season_id: int, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    return db_season

@router.put("/seasons/{season_id}", response_model=SeasonSchema)
async def update_season(season_id: int, season: SeasonBaseSchema, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    db_season.year = season.year
    db.commit()
    db.refresh(db_season)
    return db_season

@router.delete("/seasons/{season_id}", response_model=SeasonSchema)
async def delete_season(season_id: int, db: Session = Depends(get_db)):
    db_season = db.query(Season).filter(Season.id == season_id).first()
    if db_season is None:
        raise HTTPException(status_code=404, detail="Season not found")
    db.delete(db_season)
    db.commit()
    return db_season