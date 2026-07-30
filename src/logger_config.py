import logging
import os

def setup_logging():
    logging.basicConfig(
        filename=os.path.join(os.path.dirname(__file__), "..", "data", "bicing.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )