import streamlit as st
from dashboard import CreateDashboard
from graphs import CreateGraphs
from processing import ProcessData


class DashboardAlcance(CreateDashboard):
    """
    This class inherits from CreateDashboard and is responsible for generating
    visualizations related to direct beneficiaries and reached municipalities
    based on the provided data.

    Attributes:
        option (str): The current option being displayed, default is "Direct Beneficiaries".
        graph_options (dict): A nested dictionary containing configuration for various graphs
                              related to direct beneficiaries and reached municipalities.
    """

    def __init__(self, df):
        """
        Initializes the DashboardAlcance class, setting up the graph options based on the input data.

        :param df: A DataFrame containing the data for visualizations, including 'alcance'
                   and 'municipios' information.
        """
        super().__init__(df)  # Call the constructor of the parent class to initialize base functionality.

        # Set the default option for the dashboard.
        self.option = "Direct Beneficiaries"

        # Define graph options for various categories of data related to beneficiaries and municipalities.
        self.graph_options = {
            "Direct Beneficiaries": {
                "states": {
                    # Data for direct beneficiaries grouped by state and priority.
                    "df": self.df["alcance"].groupby(["Entidad", "Prioridad"]).aggregate({
                        "Email": "nunique"  # Count unique emails (beneficiaries).
                    }).reset_index(),
                    "x": "Email",  # X-axis variable for the graph.
                    "y": "Entidad",  # Y-axis variable for the graph.
                    "type_graph": "barchart",  # Type of graph to create.
                    "orientation": "h",  # Orientation of the bars in the bar chart.
                    "color": "Prioridad",  # Column used for coloring the bars.
                    "title": "Number of direct beneficiaries per state",  # Title of the graph.
                    "xaxis_name": "Number of beneficiaries",  # X-axis label.
                    "yaxis_name": "State",  # Y-axis label.
                    "show_legend": True,  # Flag to show the legend.
                    "legend_name": "Municipality\nPriority",  # Name for the legend.
                    "legend_translation": None  # No translation for the legend.
                },
                "program": {
                    # Data for direct beneficiaries grouped by program type and priority.
                    "df": self.df["alcance"].groupby(["Tipo", "Prioridad"]).aggregate({
                        "Email": "nunique"
                    }).reset_index(),
                    "x": "Email",
                    "y": "Tipo",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of direct beneficiaries per program component",
                    "xaxis_name": "Number of beneficiaries",
                    "yaxis_name": "Program component",
                    "show_legend": True,
                    "legend_name": "Municipality Priority",
                    "legend_translation": None
                },
                "professionals": {
                    # Data for educators who benefited, grouped by state and priority.
                    "df": self.df["alcance"][self.df["alcance"]["Implementación"].str.contains("Educadores")]
                    .groupby(["Entidad", "Prioridad"]).aggregate({"Email": "nunique"}).reset_index(),
                    "x": "Email",
                    "y": "Entidad",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of benefited educators per state",
                    "xaxis_name": "Benefited educators",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality Priority",
                    "legend_translation": None
                },
                "schools": {
                    # Data for verified schools grouped by state and priority.
                    "df": self.df["alcance"][(self.df["alcance"]["Centro de trabajo verificado"]) &
                                             (self.df["alcance"]["Tipo_cct"] == "Escuela")].groupby(
                        ["Entidad", "Prioridad"])
                    .aggregate({"Centro de trabajo": "nunique"}).reset_index(),
                    "x": "Centro de trabajo",
                    "y": "Entidad",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of verified schools per state",
                    "xaxis_name": "Verified schools",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_translation": None
                },
                "teenagers": {
                    # Data for directly benefited teenagers, grouped by state and priority.
                    "df": self.df["alcance"][self.df["alcance"]["Implementación"].str.contains("Estudiantes")]
                    .groupby(["Entidad", "Prioridad"]).aggregate({"Email": "nunique"}).reset_index(),
                    "x": "Email",
                    "y": "Entidad",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of directly benefited teenager students per state",
                    "xaxis_name": "Benefited teenager students",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_translation": None
                },
                "indirect": {
                    # Data for both directly and indirectly benefited teenagers grouped by state.
                    "df": self.df["alcance"][self.df["alcance"]["Implementación"].str.contains("Estudiantes")]
                    .groupby(["Entidad", "Ben_directo"]).agg(Conteo=("Ben_directo", "sum"))
                    .reset_index().astype(str),
                    "x": "Conteo",
                    "y": "Entidad",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Ben_directo",
                    "title": "Number of directly and indirectly benefited teenager students per state",
                    "xaxis_name": "Benefited teenager students",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Beneficiary Type",
                    "legend_translation": "Ben_directo"
                }
            },
            "Reached Municipalities": {
                "states": {
                    # Data for municipalities reached, grouped by state.
                    "df": self.df["municipios"],
                    "x": "Municipio_Porcentaje",
                    "y": "Entidad",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of benefited municipalities per state",
                    "xaxis_name": "Benefited municipalities",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality Priority",
                    "legend_translation": None
                },
                # "legend": {
                #     # Data for the legend of reached municipalities.
                #     "df": self.df["municipios_alcanzados"],
                #     "type_graph": "reached_municipalities_legend",
                #     "title": None
                # }
            }
        }

    def set_sidebar(self):
        """
        Configures the sidebar of the dashboard. This method creates dropdown menus
        that allow users to select different options for data visualization based on
        the available graph options.

        :return: None; sets the selected option to self.option.
        """
        # Creating the sidebar section in the Streamlit app
        with st.sidebar:
            # Displaying a title or instruction in the sidebar
            st.write("Select an option to display")

            # Creating a dropdown menu (selectbox) for users to choose a graph option
            # The options are populated from the keys of the graph_options dictionary
            self.option = st.selectbox(
                label="Default",  # Label for the dropdown menu
                label_visibility="collapsed",  # Collapses the label to save space
                options=self.graph_options.keys()  # Options are the keys from the graph_options dictionary
            )

    def launch_dashboard(self):
        """
        Launches the dashboard by configuring the header and sidebar,
        and rendering the selected graphs based on user options.

        :return: None; executes the methods to set the dashboard layout and graphs.
        """

        # Set the main header of the dashboard to "Beneficiaries"
        self.set_header("Beneficiaries")

        # Configure the sidebar for user selections
        self.set_sidebar()

        # Iterate through the graph options based on the selected option from the sidebar
        for k in self.graph_options[self.option]:
            # Add a space in the Streamlit app for visual separation
            st.write("")

            # Retrieve the data configuration for the current graph option
            data = self.graph_options[self.option][k]

            # Set the subtitle header for the current graph
            self.set_header(data["title"], type_header="subtitle")

            # Create an instance of CreateGraphs with the current data configuration
            # and set up the plots in a grid format based on the specified graph type
            CreateGraphs(data).set_plots_grid(type_graph=data["type_graph"])


st.set_page_config(layout="wide")
DashboardAlcance(ProcessData().read_data()).launch_dashboard()
