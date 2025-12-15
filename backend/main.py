from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import season_router, race_router, riders_router, team_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(season_router.router)
app.include_router(race_router.router)
app.include_router(riders_router.router)
app.include_router(team_router.router)


@app.get("/")
async def root():
    return "MotoGP API is working!"
