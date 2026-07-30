import extractor as ex
import pandas as pd
from datetime import datetime
import os
import logging

def colors(row):
    if (row["status"] != "IN_SERVICE") or (row["is_renting"] == False):
        return "grey"
    elif row["num_bikes_available"] == 0:
        return "red"
    else:
        return "green"

def capacity_size(row):
    if (row["capacity"] <= 0):
        return 10
    else:
        return row["capacity"]


def transform_data():
    json_bicing_data = ex.get_data()
    if json_bicing_data is not None:
        try:
            df = pd.DataFrame(json_bicing_data["data"]["stations"])
            df = df.drop("traffic", axis=1)
            df_types = pd.json_normalize(df["num_bikes_available_types"])
            df = pd.concat([df, df_types], axis=1)
            df = df.drop("num_bikes_available_types", axis=1)

            df["color"] = df.apply(colors, axis=1)
            df["timestamp"] = datetime.now()

            # ALERTS FOR NEGATIVE NUMBERS
            for name_column in ["num_bikes_available", "num_docks_available", "ebike", "mechanical"]:
                if df[name_column].min() < 0:
                    logging.warning(f"Alert: negative values on '{name_column}' column at data df")

            return df

        except KeyError as error:
            logging.error(f"The following exception ocurred: {error}")
            return None
    else:
        logging.warning("Skipping data transformation: no data received from API")
        return None

def transform_locations():
    json_bicing_locations = ex.get_locations()
    if json_bicing_locations is not None:
        try:
            df = pd.DataFrame(json_bicing_locations["data"]["stations"])
            df_locations = df[["station_id", "name", "lat", "lon", "capacity"]]

            # ALERTS FOR NEGATIVE NUMBERS
            for name_column in ["station_id", "capacity"]:
                if df_locations[name_column].min() < 0:
                    logging.warning(f"Alert: negative values on '{name_column}' column at locations df")

            df_locations["capacity_size"] = df_locations.apply(capacity_size, axis=1)

            return df_locations
        
        except KeyError as error:
            logging.error(f"The following exception ocurred: {error}")
            return None
    else:
        logging.warning("Skipping locations transformation: no data received from API")
        return None

def df_to_csv(df, file_address):
    if os.path.exists(file_address):
        df.to_csv(file_address, mode="a", header=False, index=False)
    else:
        df.to_csv(file_address, mode="a", header=True, index=False)

def save_snapshot(df):
    if df is not None:
        df_to_csv(df, os.path.join(os.path.dirname(__file__), "..", "data", "bicing_data.csv"))
        logging.info("Data saved correctly")
    else:
        logging.error("Snapshot not saved: merge_df returned no data")
    return df

def merge_df():
    df_data = transform_data()
    df_locations = transform_locations()

    if df_data is None:
        logging.warning("Skipping merge: missing station data")
        return None
    if df_locations is None:
        logging.warning("Skipping merge: missing location data")
        return None
    
    df_final = pd.merge(df_data, df_locations, on="station_id")
    return df_final