import streamlit as st
from pydrive.auth import GoogleAuth
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from io import BytesIO

import pandas as pd
import requests


class ProcessData:
    """
    This class is responsible for reading and loading data from Google Sheets
    and Excel files stored in Google Drive. The data is fetched based on
    sheet identifiers and cached to improve performance.
    """
    def __init__(self):
        """
        Initializes the ProcessData class by setting up the identifiers for
        the sheets to be loaded. These include the Google Sheets or Excel
        files' keys, sheet names, file types (Excel or Google Sheets),
        and the engines used to read the data.
        """
        self.__sheets_ids = {
            # List of all Google Sheets and Excel file configurations

            "educadores": {
                "key": "18nRArdEX3ek0iBo-Mu-acmGOUtPNS5OE",  # Unique Google Sheet or Excel file ID
                "sheetname": "Psicométricos",               # Specific sheet within the file
                "type": "excel",                            # Type of file (Excel or Google Sheets)
                "engine": "openpyxl"                        # Pandas engine for reading the Excel file
            },
            "estudiantes_g1": {
                "key": "1EyPLSHmoeAloT6MGjk0YPmwASvuKGnztNkmlgjMl8yY",
                "sheetname": "Psicométricos",
                "type": "gsheets",                          # Google Sheets type
                "engine": "calamine"                        # Engine for reading Google Sheets
            },
            "estudiantes_g2": {
                "key": "10fpv_VB6G0gV2E5V2wF8jzHl4xSdXrIMo3Mw4imftbk",
                "sheetname": "Psicométricos FINALES con items inversos",
                "type": "gsheets",
                "engine": "calamine"
            },
            "fls": {
                "key": "1_WcGc4kFasT19bnnn6MJAEpU0uWQ6SDed8MtLb_0A08",
                "sheetname": "Psicométricos_final",
                "type": "gsheets",
                "engine": "calamine"
            },
            "alcance": {
                "key": "1-0IDiwALcmsTvtQom8l_Y3G-TclKbGIo",
                "sheetname": "Sheet1",
                "type": "excel",
                "engine": "openpyxl"
            },
            "municipios": {
                "key": "1IFhfq6a5IcE1ZCLs4afmm5nAjrU8TgHH",
                "sheetname": "Sheet1",
                "type": "excel",
                "engine": "openpyxl"
            },
            "municipios_alcanzados": {
                "key": "1kINeWvQv5yrr62zNKgoXATqJwmosGTVd",
                "sheetname": "Sheet1",
                "type": "excel",
                "engine": "openpyxl"
            }
        }
        # Dictionary to store the loaded data
        self.data = {}

    @st.cache_data
    def read_data(_self):
        """
        Reads the necessary data for the dashboards from Google Sheets or Excel files
        located on Google Drive. The data is cached to avoid repeated reads and improve performance.

        :return:A dictionary containing all loaded data, where the keys represent the file labels
            (e.g., 'educadores', 'estudiantes_g1', etc.) and values are the corresponding dataframes.
        """
        # Initialize Google authentication object
        gauth = GoogleAuth()

        # Use service account credentials to authenticate with Google Drive API
        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["connections"],  # Use secret credentials stored in Streamlit config
            scopes=["https://www.googleapis.com/auth/drive"]  # Scope to access Google Drive files
        )
        # Ensure credentials are valid and refresh if necessary
        credentials.refresh(Request())
        gauth.credentials = credentials

        # Loop through each sheet configuration in self.__sheets_ids
        for k, i in _self.__sheets_ids.items():
            key = i["key"]         # Extract the Google Drive key (file ID)
            engine = i["engine"]   # Extract the engine for reading the data (e.g., openpyxl or calamine)

            # If the file is a Google Sheet, construct a URL to export it as Excel
            if i["type"] == "gsheets":
                url = f"https://docs.google.com/spreadsheets/export?id={key}&exportFormat=xlsx"
            else:
                # For Excel files, use the Google Drive API to download the file
                url = f"https://www.googleapis.com/drive/v3/files/{key}?alt=media"

            # Send a GET request to download the file from the constructed URL
            rqst = requests.get(url, headers={"Authorization": f"Bearer {credentials.token}"})

            # Read the downloaded content as an Excel file and store it in the data dictionary
            _self.data[k] = pd.read_excel(BytesIO(rqst.content), sheet_name=i["sheetname"], engine=engine)

        # Return the dictionary containing all the loaded data
        return _self.data
