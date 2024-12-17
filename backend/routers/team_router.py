from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.utils.database import get_db
from backend.schemas.team_schema import TeamSchema, TeamCreateSchema
from backend.models.Team import Team

router = APIRouter(prefix="/teams", tags=["Teams"])

# CRUD Team

@router.get("/", response_model=List[TeamSchema])
async def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()

@router.get("/{team_id}", response_model=TeamSchema)
async def get_team(team_id:int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.post("/", response_model=TeamSchema)
async def create(team: TeamCreateSchema, db: Session=Depends(get_db)):
    team_db = Team(
        name=team.name,
        factory=team.factory
    )
    db.add(team_db)
    db.commit()
    db.refresh(team_db)
    return team_db

@router.delete("/{team_id}", response_model=TeamSchema)
async def delete_team(team_id: int, db:Session=Depends(get_db)):
    team_db = db.query(Team).filter(Team.id == team_id).first()
    if not team_db:
        raise HTTPException(status_code=404, detail="Team not found")
    db.delete(team_db)
    db.commit()
    return team_db

@router.put("/{team_id}", response_model=TeamSchema)
async def update_team(team_id: int, team:TeamCreateSchema, db:Session=Depends(get_db)):
    team_db = db.query(Team).filter(Team.id == team_id).first()
    if not team_db:
        raise HTTPException(status_code=404, detail="Team not found")
    team_db.name=team.name
    team_db.factory=team.factory
    db.commit()
    db.refresh(team_db)
    return team_db