import logging

def setup_logging():
    logging.basicConfig(
        filename="data/bicing.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )