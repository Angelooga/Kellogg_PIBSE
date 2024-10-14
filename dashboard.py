import streamlit as st


class CreateDashboard:
    """
    This class is responsible for creating the layout and structure of the dashboard.
    It allows setting headers, sidebars, and launching the dashboard layout.
    """
    def __init__(self, df):
        """
        Initializes the dashboard with a dataframe and some style settings for
        the header titles.

        Args:
            df (DataFrame): The dataframe containing the data to be displayed in the dashboard.
        """
        self.df = df  # DataFrame to be used for the dashboard content
        self.bg_title_color = "#22314E"  # Background color for main titles
        self.bg_subtitle_color = "#F0BA54"  # Background color for subtitles

    def set_header(self, title: str = "Default", type_header: str = "title"):
        """
        Displays a formatted header (title or subtitle) at the top of the dashboard.
        The header's style is set using HTML and Streamlit's `markdown` function.

        Args:
            title (str): The text to be displayed as the header. Defaults to "Default".
            type_header (str): Defines the type of header - "title" or "subtitle".
                               Default is "title".

        This function formats the header using inline CSS to control text alignment,
        text color, background color, and size.
        """
        # Check if the header is a title (default) and if a title is provided
        if type_header == "title" and title is not None:
            # Create HTML for the title with a background and white text
            html_title = ("<h1 style='text-align: center; color: white; "
                          f"background: {self.bg_title_color}'>" +
                          f"{title}" +
                          "</h1>")
            # Display the formatted title using Streamlit's markdown method
            st.markdown(html_title, unsafe_allow_html=True)
        # Check if the header is a subtitle
        elif type_header == "subtitle" and title is not None:
            # Create HTML for the subtitle with a different background and smaller font size
            html_title = ("<h1 style='text-align: center; color: black; " +
                          f"background: {self.bg_subtitle_color}; " +
                          f"font-size:20px'>" +
                          f"{title}" +
                          "</h1>")
            # Display the formatted subtitle using Streamlit's markdown method
            st.markdown(html_title, unsafe_allow_html=True)

        # If no title is provided, simply do nothing (skip header rendering)
        elif title is None:
            pass

    def set_sidebar(self):
        """
        Sets the layout and content of the sidebar. This function is currently a placeholder
        and can be expanded to include interactive sidebar elements like filters or navigation.
        """
        pass

    def launch_dashboard(self):
        """
        Launches the dashboard layout. This function is currently a placeholder and should be
        expanded to define the main sections of the dashboard (e.g., graphs, data displays).
        """
        pass

