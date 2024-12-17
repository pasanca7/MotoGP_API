from fastapi import FastAPI
from backend.routers import (
    season_router,
    race_router,
    riders_router,
    team_router
)

app = FastAPI()

# Routers
app.include_router(season_router.router)
app.include_router(race_router.router)
app.include_router(riders_router.router)
app.include_router(team_router.router)

@app.get("/")
async def root():
    return "MotoGP API is working!"