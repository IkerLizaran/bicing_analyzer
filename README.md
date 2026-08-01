# Bicing Analyzer

A tool that extracts live data from Barcelona's Bicing bike stations, cleans it, saves a historical record automatically, and visualizes it with interactive charts and a map using Plotly.

## About this project

This is a personal project to practice working with APIs, cleaning data with pandas, automating tasks with cron, and visualizing data — applying all of this step by step on a real dataset.

## Project structure

```
bicing_analyzer/
├── src/
│   ├── extractor.py       # Fetches data from the Bicing API
│   ├── transform.py       # Cleans, merges and saves the data
│   ├── analysis.py        # Generates charts and the map
│   ├── logger_config.py   # Centralized logging setup
│   ├── main.py            # Manual entry point (with visualizations)
│   └── capture_data.py    # Entry point for cron (data capture only)
└── data/
    ├── bicing_data.csv    # Historical snapshots
    └── bicing.log         # Application log
```

## How it works

The project has two entry points:

- `main.py`: runs the full pipeline and shows the interactive charts and map. Meant for manual use.
- `capture_data.py`: runs the pipeline and saves a snapshot to the CSV file, without opening any charts. Meant to be run automatically (e.g. with cron).

Both entry points follow the same underlying flow:

1. `extractor.py` fetches raw data from the Bicing API (station status and locations)
2. `transform.py` cleans the data, merges both sources, and adds calculated columns (like station color and timestamp)
3. Depending on the entry point:
    - `capture_data.py` saves the result to `data/bicing_data.csv`
    - `main.py` sends the result to `analysis.py` to generate the map

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Create a `.env` file in the project root with your Bicing API token:

```
TOKEN_BICING=your_token_here
```

You can request a token from [Open Data BCN](https://opendata-ajuntament.barcelona.cat/).

## How to run it

Make sure your virtual environment is activated before running any command.

Run manually (shows the map):
```bash
python src/main.py
```

Run only the data capture (no charts, used for automation and saves the data to a csv located in data folder):
```bash
python src/capture_data.py
```

After running either one, it will also appear a `bicing.log` file in the data folder, informing about how the code is working.

### Automating with cron

To run the data capture automatically every hour, add this line with `crontab -e` in your terminal:
```
0 * * * * /path/to/venv/bin/python /path/to/project/src/capture_data.py
```