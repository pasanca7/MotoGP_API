from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.utils.database import get_db
from backend.schemas.rider_schemas import RiderSchema, RiderCreateSchema
from backend.models.Rider import Rider

router = APIRouter(prefix="/riders", tags=["Riders"])

@router.get("/", response_model=List[RiderSchema])
async def get_riders(db: Session = Depends(get_db)):
    riders = db.query(Rider).all()
    return riders

@router.get("/{rider_id}", response_model=RiderSchema)
async def get_rider(rider_id:int, db: Session = Depends(get_db)):
    rider = db.query(Rider).filter(Rider.id == rider_id).first()
    if not rider:
        raise HTTPException(status_code=404, detail="Rider not found")
    return rider

@router.post("/", response_model=RiderSchema)
async def create_rider(rider: RiderCreateSchema, db:Session = Depends(get_db)):
    db_rider = Rider(
        name=rider.name,
        surname=rider.surname,
        number=rider.number,
        country=rider.country
    )
    db.add(db_rider)
    db.commit()
    db.refresh(db_rider)
    return db_rider

@router.put("/{rider_id}", response_model=RiderSchema)
async def update_race(rider_id: int, rider: RiderCreateSchema, db: Session = Depends(get_db)):
    rider_db = db.query(Rider).filter(Rider.id == rider_id).first()
    if not rider_db:
        raise HTTPException(status_code=404, detail="Rider not found")
    rider_db.name=rider.name
    rider_db.surname=rider.surname
    rider_db.country=rider.country
    rider_db.number=rider.number
    db.commit()
    db.refresh(rider_db)
    return rider_db

@router.delete("/{rider_id}", response_model=RiderSchema)
async def delete_rider(rider_id: int, db:Session = Depends(get_db)):
    rider_db = db.query(Rider).filter(Rider.id == rider_id).first()
    if not rider_db:
        raise HTTPException(status_code=404, detail="Rider not found")
    db.delete(rider_db)
    db.commit()
    return rider_db

