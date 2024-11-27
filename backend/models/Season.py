from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.utils.database import Base

class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    races = relationship("Race", back_populates="season")  # Referencia tardía

class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sequence = Column(Integer, nullable=False)
    short_name = Column(String, nullable=False)
    circuit_name = Column(String, nullable=False)
    season_id = Column(Integer, ForeignKey("seasons.id"))
    season = relationship("Season", back_populates="races")
