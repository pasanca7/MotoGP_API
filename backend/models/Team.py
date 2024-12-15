from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.utils.database import Base
from backend.models.Rider import Contract

class SeasonTeam(Base):
    __tablename__ = 'season_team'
    season_id = Column(
        Integer,
        ForeignKey('seasons.id', ondelete='CASCADE'),
        primary_key=True
    )
    team_id = Column(
        Integer,
        ForeignKey('teams.id',  ondelete='CASCADE'),
        primary_key=True
    )


class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    factory = Column(String, nullable=False)
    seasons = relationship(
        "Season",
        secondary="season_team",
        back_populates="teams"
    )
    contracts = relationship(
        Contract,
        back_populates="team"
    )
