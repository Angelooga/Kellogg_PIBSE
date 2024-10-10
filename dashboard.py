import streamlit as st


# def set_header(title: str = "Default", type_header: str = "title"):
#     """
#     This function formats a string containing the title in html format.
#     :return:
#     """
#     if type_header == "title":
#         html_title = ("<h1 style='text-align: center; color: white; background: #22314E'>" +
#                       f"{title}" +
#                       "</h1>")
#         st.markdown(html_title, unsafe_allow_html=True)
#     elif type_header == "subtitle":
#         html_title = ("<h1 style='text-align: center; color: black; background: #F0BA54; font-size:20px'>" +
#                       f"{title}" +
#                       "</h1>")
#         st.markdown(html_title, unsafe_allow_html=True)


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
        if type_header == "title":
            html_title = ("<h1 style='text-align: center; color: white; "
                          f"background: {self.bg_title_color}'>" +
                          f"{title}" +
                          "</h1>")
            st.markdown(html_title, unsafe_allow_html=True)
        elif type_header == "subtitle":
            html_title = ("<h1 style='text-align: center; color: black; " +
                          f"background: {self.bg_subtitle_color}; " +
                          f"font-size:20px'>" +
                          f"{title}" +
                          "</h1>")
            st.markdown(html_title, unsafe_allow_html=True)

    def set_sidebar(self):
        pass

    def launch_dashboard(self):
        pass
