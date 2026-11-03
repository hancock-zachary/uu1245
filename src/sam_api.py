"""
file name: sam_api.py
file author: Zachary Hancock
last edit date: 11/1/2026

Tiny SAM.gov query to fetch a few recent contract opportunities.
"""
#%% Import modules and libraries.
# First party libraries.
from datetime import date, timedelta
import os
from pathlib import Path
import sqlite3

# Third party libraries.
from dotenv import load_dotenv
import pandas as pd
import requests

# Program Modules.

# Format system and file settings.

# Assign global variables.
URL = "https://api.sam.gov/opportunities/v2/search"


#%% Code.
class System_For_Award_Management_API:
    def __init__(self) -> None:
        load_dotenv(Path(__file__).resolve().parent.parent / ".env")
        self.__API_KEY = os.environ["SAM_GOV_API_KEY"]

        self.URL = "https://api.sam.gov/opportunities/v2/search"

    def query_API(self
                  , limit: int = 1
                  , offset: int = 0
                  ) -> dict:
        """
        Query the SAM.gov API and return the query results as a data dictionary.
        """
        assert limit >= 1 or limit <= 1_000, "limit indicates the total number of records to be retrieved per page. Max = 1_000 and min = 1."
        assert offset >= 0, "offset indicates the page index. Set to 0 or greater."

        parameters = {
            "api_key": self.__API_KEY
           #, "ptype": "u"
           #, "solnum":   # Solicitation Number
           #, "noticeid":   # Notice ID
           #, "title":   # Title
           , "postedFrom": (date.today() - timedelta(days=7)).strftime("%m/%d/%Y")
           , "postedTo": date.today().strftime("%m/%d/%Y")
           #, "deptname":   # Department Name (L1)
           #, "subtier":   # Agency Name (L2)
           #, "state":   # Place of Performance (State)
           #, "status": 
           #, "zip":   # Place of Performance (Zip Code)
           #, "organizationCode":   # Code of associated organization
           #, "organizationName":   # Name of associated organization
           #, "typeOfSetAside": 
           #, "typeOfSetAsideDescription": 
           #, "ncode":   # NAICS Code. Max 6 digits
           #, "ccode":   # Classification Code
           #, "rdlfrom":   # Response Deadline date
           #, "rdlto":   # Response Deadline date
            , "limit": limit  # Total number of records to be retrieved per page. Max = 1_000
            , "offset": offset  # Indicates the page index.
        }
        
        response = requests.get(url=self.URL, params=parameters, timeout=30)  # Query the SAM.gov API.
        response.raise_for_status()  # Raise any exceptions from the API if present.
        data = response.json()  # Format the SAM.gov response in the JSON format.
        return data
        

    def format_database(self):
        """
        Format JSON data into pandas dataframes and upload those pandas dataframes into a
        SQLite object in the data folder of the repo.
        """
        pass
    

#%% Execute module code.
"""
This block of code will only execute when the file is explictly commanded to run.
If this file is pulled into another file as a module, this block of code will not
execute.
"""
if __name__ == "__main__":
    data = System_For_Award_Management_API().query_API(limit=100)
    
    print(f"Total matches: {data.get('totalRecords')}")  # Print a portion of the data collected.
    for opportunity in data.get("opportunitiesData", []):
        print(f"- {opportunity.get('postedDate')}  {opportunity.get('title')}")


#%% END OF CODE.