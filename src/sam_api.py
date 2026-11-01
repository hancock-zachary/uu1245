"""
file name: sam_api.py
file author: Zachary Hancock
last edit date: 11/1/2026

Tiny SAM.gov query to fetch a few recent contract opportunities.
"""
#%% Import modules and libraries.
import os  # First party libraries.
from datetime import date, timedelta
from pathlib import Path

import requests  # Third party libraries.
from dotenv import load_dotenv


#%% Format system and file settings.


#%% Assign global variables.
URL = "https://api.sam.gov/opportunities/v2/search"


#%% Code.
def load_api_key() -> str:
    """
    Read SAM_GOV_API_KEY from the environment, falling back to the project's .env file.
    """
    load_dotenv(Path(__file__).resolve().parent.parent / ".env")
    return os.environ["SAM_GOV_API_KEY"]


def main() -> None:
    """
    Query the SAM.gov API and print the query results.
    """
    today = date.today()
    params = {
        "api_key": load_api_key()  # Function returns the SAM.gov API key.
        , "postedFrom": (today - timedelta(days=7)).strftime("%m/%d/%Y")  # Review posted data from the past week.
        , "postedTo": today.strftime("%m/%d/%Y")
        , "limit": 5  # SAM.gov daily API limit is 10 observations.
    }
    response = requests.get(URL, params=params, timeout=30)  # Query the SAM.gov API.
    response.raise_for_status()  # Raise any exceptions from the API if present.
    data = response.json()  # Format the SAM.gov response in the JSON format.

    print(f"Total matches: {data.get('totalRecords')}")  # Output the data as a print statement.
    for opportunity in data.get("opportunitiesData", []):
        print(f"- {opportunity.get('postedDate')}  {opportunity.get('title')}")


#%% Execute module code.
"""
This block of code will only execute when the file is explictly commanded to run.
If this file is pulled into another file as a module, this block of code will not
execute.
"""
if __name__ == "__main__":
    main()  # Run the code from the main() function.


#%% END OF CODE.