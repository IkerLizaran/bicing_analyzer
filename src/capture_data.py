from logger_config import setup_logging
from transform import merge_df, save_snapshot, save_to_db

setup_logging()

def main():
    df = merge_df()
    save_to_db(df)
    save_snapshot(df)

main()