import kagglehub
import pandas as pd
from backend.settings import DATASET_PATH
from backend.models.Season import Season, Race
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

    df21 = df[df["year"] == 2021]
    races_df = df21.drop_duplicates(subset=["sequence"], keep="first")
    races_df = races_df[["sequence","shortname", "circuit_name"]]


    season21 = Season(
        year=2021
    )
    print("Creating Season " + str(season21.year) + "...")
    db.add(season21)

    races = []
    for _, row in races_df.iterrows():
        print("Loading race " + str(row["sequence"]) +" - " + row["circuit_name"] + " " + str(season21.year))
        race = Race(
            sequence=row["sequence"],
            short_name=row["shortname"],
            circuit_name=row["circuit_name"],
            season=season21
        )
        races.append(race)
    db.add_all(races)
    db.commit()
    print("Season " + str(season21.year) + " successfully created")
    


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
