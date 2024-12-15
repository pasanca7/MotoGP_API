import kagglehub
import pandas as pd
from backend.settings import DATASET_PATH
from backend.models.Season import Season, Race
from backend.models.Team import Team
from backend.models.Rider import Rider, Contract
from backend.utils.database import SessionLocal
from backend.utils.database import Base, engine

def populate_db(db):
    if DATASET_PATH:
        path = DATASET_PATH
    else:
        print("Downloading Dataset...")
        path = kagglehub.dataset_download("amalsalilan/motogpresultdataset")
    try:
        df = pd.read_csv(path+"/FILTERED_ROWS.csv")
    except FileNotFoundError as e:
        print("Dataset not found, check the env variables", e)
        raise FileNotFoundError

    df21 = df[(df["year"] == 2021) & (df["category"] == "MotoGP")]
    races_df = df21.drop_duplicates(subset=["sequence"], keep="first")
    races_df = races_df[["sequence","shortname", "circuit_name"]]
    teams_df = df21[["team_name","bike_name"]].drop_duplicates(subset=["team_name","bike_name"])
    riders_df = df21[["rider", "rider_name", "number", "country", "team_name", "bike_name"]].drop_duplicates(subset=["rider", "team_name"])

    season21 = Season(
        year=2021
    )
    db.add(season21)
    print("+ Creating Season " + str(season21.year) + "...")

    print(" \Loading Riders...")
    riders, contracts_dict = create_riders(riders_df)
    db.add_all(riders)

    print(" \Loading Teams...")
    teams, contracts = create_teams(teams_df, contracts_dict)
    season21.teams = teams
    db.add_all(teams)
    db.add_all(contracts)

    print(" \Loading Races...")
    races = create_races(races_df, season21)
    db.add_all(races)
    
    db.commit()
    print("Season " + str(season21.year) + " successfully created")


def create_riders(df):
    riders = []
    contracts = {}
    processed_riders = {}
    for _, row in df.iterrows():
        # Create rider
        if row["rider"] not in processed_riders.keys():
            print("  - Loading rider " + str(row["rider_name"]))
            full_name = row["rider_name"].split(",")
            rider = Rider(
                id = row["rider"],
                name = full_name[1].strip(),
                surname = full_name[0],
                number = int(row["number"]),
                country = row["country"]
            )
            processed_riders[row["rider"]] = rider

        if row["team_name"] in contracts.keys():
            contracts[row["team_name"]].append(processed_riders[row["rider"]])
        else:
            contracts[row["team_name"]] = [processed_riders[row["rider"]]]
        riders.append(rider)
    return riders, contracts    


def create_races(df, season):
    races = []
    for _, row in df.iterrows():
        print("  - Loading race " + str(row["sequence"]) +" - " + row["circuit_name"] + " " + str(season.year))
        race = Race(
            sequence=row["sequence"],
            short_name=row["shortname"],
            circuit_name=row["circuit_name"],
            season=season
        )
        races.append(race)
    return races

def create_teams(df, contract_df):
    teams = []
    contracts = []
    for _, row in df.iterrows():
        print("  - Loading team " + str(row["team_name"]) + "(" + str(row["bike_name"] +")"))
        team = Team(
            name = row["team_name"],
            factory = row["bike_name"],
            #contracts = 
        )
        for rider in contract_df[row["team_name"]]:
            contract = Contract(
                rider=rider,
                team=team
            )
        contracts.append(contract)
        teams.append(team)
    return teams, contracts


def init_db():
    db = SessionLocal()

    print("Dropping tables...")
    Base.metadata.drop_all(bind=engine)
    
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    
    print("Tables created successfully")
    
    populate_db(db)
    db.close()

if __name__ == "__main__":
    init_db()
