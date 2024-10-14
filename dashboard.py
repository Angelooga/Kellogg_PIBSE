import streamlit as st


class CreateDashboard:
    """
    This class does something
    """
    def __init__(self, df):
        self.df = df
        self.bg_title_color = "#22314E"
        self.bg_subtitle_color = "#F0BA54"

    def set_header(self, title: str = "Default", type_header: str = "title"):
        """
        This function formats a string containing the title in html format.
        :return:
        """
        if type_header == "title" and title is not None:
            html_title = ("<h1 style='text-align: center; color: white; "
                          f"background: {self.bg_title_color}'>" +
                          f"{title}" +
                          "</h1>")
            st.markdown(html_title, unsafe_allow_html=True)
        elif type_header == "subtitle" and title is not None:
            html_title = ("<h1 style='text-align: center; color: black; " +
                          f"background: {self.bg_subtitle_color}; " +
                          f"font-size:20px'>" +
                          f"{title}" +
                          "</h1>")
            st.markdown(html_title, unsafe_allow_html=True)

        elif title is None:
            pass

    def set_sidebar(self):
        pass

    def launch_dashboard(self):
        pass
