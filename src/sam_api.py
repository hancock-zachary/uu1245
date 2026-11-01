"""
file name: sam_api.py
file author: Zachary Hancock
last edit date: 11/1/2026

Tiny SAM.gov query to fetch a few recent contract opportunities.
"""
#%% Import modules and libraries.
import os
from datetime import date, timedelta
from pathlib import Path

import requests


#%% Format system and file settings.


#%% Assign global variables.
URL = "https://api.sam.gov/opportunities/v2/search"


#%% Code.
def load_api_key():
    # Read SAM_API_KEY from the environment, falling back to the project's .env file.
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            key, _, value = line.partition("=")
            if key.strip() == "SAM_API_KEY":
                os.environ.setdefault("SAM_API_KEY", value.strip())
    return os.environ["SAM_API_KEY"]


def main():
    today = date.today()
    params = {
        "api_key": load_api_key(),
        "postedFrom": (today - timedelta(days=7)).strftime("%m/%d/%Y"),
        "postedTo": today.strftime("%m/%d/%Y"),
        "limit": 5,
    }
    resp = requests.get(URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    print(f"Total matches: {data.get('totalRecords')}")
    for opp in data.get("opportunitiesData", []):
        print(f"- {opp.get('postedDate')}  {opp.get('title')}")


#%% Execute module code.
"""
This block of code will only execute when the file is explictly commanded to run.
If this file is pulled into another file as a module, this block of code will not
execute.
"""
if __name__ == "__main__":
    main()  # Run the code from the main() function.


#%% END OF CODE.