import streamlit as st
from pydrive.auth import GoogleAuth
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from io import BytesIO

import pandas as pd
import requests


class ProcessData:
    """
    This class does something...
    """
    def __init__(self):
        self.__sheets_ids = {
            "educadores": {
                "key": "18nRArdEX3ek0iBo-Mu-acmGOUtPNS5OE",
                "sheetname": "Psicométricos",
                "type": "excel",
                "engine": "openpyxl"
            },
            "estudiantes_g1": {
                "key": "1EyPLSHmoeAloT6MGjk0YPmwASvuKGnztNkmlgjMl8yY",
                "sheetname": "Psicométricos",
                "type": "gsheets",
                "engine": "calamine"
            },
            "estudiantes_g2": {
                "key": "10fpv_VB6G0gV2E5V2wF8jzHl4xSdXrIMo3Mw4imftbk",
                "sheetname": "Psicométricos con items inverso",
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
        self.data = {}

    @st.cache_data
    def read_data(_self):
        """
        This function reads the necessary data for the dashboards. The st.cache_data decorator
        was used in order to save all the data in cache, reading the data only once when the
        application is launched.
        """
        # Authenticating with a valid Google account
        gauth = GoogleAuth()

        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["connections"],
            scopes=["https://www.googleapis.com/auth/drive"]
        )
        # Ensure the credentials are valid and refresh if necessary
        credentials.refresh(Request())
        gauth.credentials = credentials

        for k, i in _self.__sheets_ids.items():
            key = i["key"]
            engine = i["engine"]
            # st.write(key)
            if i["type"] == "gsheets":
                url = f"https://docs.google.com/spreadsheets/export?id={key}&exportFormat=xlsx"
            else:
                url = f"https://www.googleapis.com/drive/v3/files/{key}?alt=media"

            rqst = requests.get(url, headers={"Authorization": f"Bearer {credentials.token}"})
            _self.data[k] = pd.read_excel(BytesIO(rqst.content), sheet_name=i["sheetname"], engine=engine)

        return _self.data
