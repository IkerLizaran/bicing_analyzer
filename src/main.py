import logging
from analysis import analyser
from transform import save_snapshot

logging.basicConfig(
    filename="data/bicing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    save_snapshot()
    analyser()

main()