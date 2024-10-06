import math
import streamlit as st
# from processing import read_data
from processing import ProcessData
from graphs import CreateGraphs


def set_header(title: str = "Default", type: str = "title"):
    """
    This function formats a string containing the title in html format.
    :return:
    """
    if type == "title":
        html_title = ("<h1 style='text-align: center; color: white; background: #22314E'>" +
                      f"{title}" +
                      "</h1>")
        st.markdown(html_title, unsafe_allow_html=True)
    elif type == "subtitle":
        html_title = ("<h1 style='text-align: center; color: black; background: #F0BA54; font-size:20px'>" +
                      f"{title}" +
                      "</h1>")
        st.markdown(html_title, unsafe_allow_html=True)


class CreateDashboard:
    """
    This class does something
    """
    def __init__(self, df):
        self.df = df

    def set_sidebar(self):
        pass

    def launch_dashboard(self):
        pass
