from logger_config import setup_logging
from analysis import analyzer
from transform import merge_df

setup_logging()

def main():
    df = merge_df()
    analyzer(df)

main()