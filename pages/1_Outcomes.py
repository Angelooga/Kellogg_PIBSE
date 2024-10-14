import streamlit as st
from dashboard import CreateDashboard
from graphs import CreateGraphs
from processing import ProcessData


class DashboardOutcomes(CreateDashboard):
    """
    DashboardOutcomes class is responsible for creating outcome-related visualizations and summaries
    for educational program data. It inherits from the CreateDashboard class, allowing for
    a structured dashboard interface and functionality.
    """

    def __init__(self, df):
        """
        Initializes the DashboardOutcomes instance with the provided DataFrame.

        :param df: DataFrame containing the data for various educational outcomes, including
                   information about educators, students, and their respective measurements.
        """
        # Call the parent class constructor to initialize base dashboard functionalities
        super().__init__(df)

        # Define the options for graphs that will be displayed in the dashboard
        self.graph_options = {
            "Outcome Graphs (Vertical)": {
                "Professionals": {
                    # Data for educators
                    "df": self.df["educadores"],
                    "x": "Medición inglés",  # X-axis measurement
                    "y": "D-cohen",  # Y-axis measurement
                    "type_graph": "barchart",  # Type of graph
                    "orientation": "v",  # Vertical orientation
                    "color": "Constructo",  # Color categorization
                    "title": "Outcomes Graph: Professional Development",  # Title for the graph
                    "text": "Significancia",  # Text to display on the graph
                    "text_dtype": "str",  # Data type of text
                    "xaxis_name": "Scale",  # Name of the x-axis
                    "yaxis_name": "D-Cohen",  # Name of the y-axis
                    "show_legend": True,  # Whether to show legend
                    "legend_name": None,  # Legend name
                    "legend_translation": "Constructo"  # Translation for legend
                },
                # Additional graph configurations for different educator and student groups go here...
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "title": "Outcomes Graph: Systemic Leadership Training",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "show_legend": True,
                    "legend_name": None,
                    "legend_translation": "Constructo"
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "show_legend": True,
                    "legend_name": None,
                    "legend_translation": "Constructo"
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "show_legend": True,
                    "legend_name": None,
                    "legend_translation": "Constructo"
                }
            },
            # Additional configurations for "Outcome Graphs (Horizontal)", "Detailed Outcome Graphs",
            # and "Outcome Summary Table" will go here...
            "Outcome Graphs (Horizontal)": {
                "Professionals": {
                    "df": self.df["educadores"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",  # Horizontal orientation
                    "color": "Constructo",
                    "title": "Outcomes Graph: Professional Development",
                    "text": "D-cohen",
                    "text_dtype": "float",  # Text data type
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": None,
                    "line": "Effect_Size",  # Line representation for effect size
                    "show_legend": False  # Hide the legend for this graph
                },
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "order": None,
                    "color": "Constructo",
                    "title": "Outcomes Graph: Systemic Leadership Training",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": None,
                    "line": "Effect_Size",
                    "show_legend": False
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": None,
                    "line": "Effect_Size",
                    "show_legend": False
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": None,
                    "line": "Effect_Size",
                    "show_legend": False
                }
            },
            "Detailed Outcome Graphs": {
                "Professionals": {
                    "df": self.df["educadores"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",  # Use forest plot for detailed outcomes
                    "high": "conf.high",  # Upper bound for confidence interval
                    "low": "conf.low",  # Lower bound for confidence interval
                    "orientation": None,  # Orientation is not applicable for forest plots
                    "color": "Comportamiento",
                    "title": "Detailed Outcomes Graph: Professional Development",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",  # Legend for the forest plot
                    "line": "D-Cohen",
                    "legend_translation": "Comportamiento"
                },
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",  # Use forest plot for detailed outcomes
                    "high": "conf.high",  # Upper bound for confidence interval
                    "low": "conf.low",  # Lower bound for confidence interval
                    "orientation": None,  # Orientation is not applicable for forest plots
                    "color": "Comportamiento",
                    "title": "Outcomes Graph: Systemic Leadership Training",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",  # Legend for the forest plot
                    "line": "D-Cohen",
                    "legend_translation": "Comportamiento"
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",  # Use forest plot for detailed outcomes
                    "high": "conf.high",  # Upper bound for confidence interval
                    "low": "conf.low",  # Lower bound for confidence interval
                    "orientation": None,  # Orientation is not applicable for forest plots
                    "color": "Comportamiento",
                    "title":  "Outcomes Graph: Teenagers Groups 1 & 2",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",  # Legend for the forest plot
                    "line": "D-Cohen",
                    "legend_translation": "Comportamiento"
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",  # Use forest plot for detailed outcomes
                    "high": "conf.high",  # Upper bound for confidence interval
                    "low": "conf.low",  # Lower bound for confidence interval
                    "orientation": None,  # Orientation is not applicable for forest plots
                    "color": "Comportamiento",
                    "title":  "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",  # Legend for the forest plot
                    "line": "D-Cohen",
                    "legend_translation": "Comportamiento"
                }
                # Additional configurations for "Professionals_FLS", "Teenagers_g1", and "Teenagers_g2"
            },
            "Outcome Summary Table": {
                "general": {
                    "data": {
                        # Data for summary table from different educational groups
                        "df1": self.df["educadores"],
                        "df2": self.df["fls"],
                        "df3": self.df["estudiantes_g1"],
                        "df4": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                               "& Pre == 'inicial' & Post == 'final'")
                    },
                    "type_graph": "summary_table",  # Type set for summary table
                    "color_scale": "Comportamiento",  # Color scale used for table visualization
                    "title": "Outcome Summary Table",  # Title for the summary table
                    "xaxis_name": ["Professional Development", "Systemic Leadership Training",
                                   "Teenagers: Groups 1, 2 & 3", "Teenagers: Groups 4 & 5"]  # X-axis names for summary
                }
            }
        }

        # Set the default graph option to "Outcome Graphs (Horizontal)"
        self.option = "Outcome Graphs (Horizontal)"

    def set_sidebar(self):
        """
        Configures the sidebar of the Streamlit dashboard, allowing users to select a graph option
        from the available options defined in the graph_options dictionary.

        This method uses Streamlit's sidebar functionality to create a dropdown menu where users can
        choose from the keys of the graph_options dictionary. The selected option will determine which
        graph is displayed on the main dashboard.

        :return: None
        """
        with st.sidebar:
            # Create a select box in the sidebar for users to choose a graph option
            self.option = st.selectbox(
                label="Default",  # Label displayed above the select box
                label_visibility="collapsed",  # Hides the label to maintain a clean sidebar
                options=self.graph_options.keys()  # Options are the keys from the graph_options dictionary
            )

    def launch_dashboard(self):
        """
        Launches the outcomes dashboard by configuring the header, sidebar,
        and displaying the relevant graphs based on the user's selection.

        This method sets the main header of the dashboard to "Outcomes",
        invokes the sidebar for user input, and iterates over the selected
        graph options to render the corresponding graphs. Each graph is
        displayed with its title as a subtitle, and the appropriate plotting
        function is called to generate the graph visuals.

        :return: None
        """
        # Set the main header of the dashboard
        self.set_header("Outcomes")

        # Set the sidebar options for graph selection
        self.set_sidebar()

        # Iterate through the selected graph options and display each graph
        for k in self.graph_options[self.option]:
            data = self.graph_options[self.option][k]  # Get data configuration for the current graph
            st.write(" ")  # Add a space for better visual separation
            # st.write(data["df"])
            if "df" in data and data["df"].empty:
                continue
            # Set the subtitle header for the current graph
            self.set_header(data["title"], type_header="subtitle")
            # Create the graph using the specified configuration
            CreateGraphs(data).set_plots_grid(type_graph=data["type_graph"])


st.set_page_config(layout="wide")
DashboardOutcomes(ProcessData().read_data()).launch_dashboard()
