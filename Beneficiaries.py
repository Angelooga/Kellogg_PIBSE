import streamlit as st
from dashboard import CreateDashboard
from graphs import CreateGraphs
from processing import ProcessData


class DashboardAlcance(CreateDashboard):
    """
    This class does something
    """
    def __init__(self, df):
        super().__init__(df)
        self.option = "Direct Beneficiaries"
        self.graph_options = {
            "Direct Beneficiaries": {
                "states": {
                    "df": self.df.groupby(["Entidad", "Prioridad"]).aggregate({
                        "Email": "nunique"
                    }).reset_index(),
                    "x": "Email",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of direct beneficiaries per state",
                    "xaxis_name": "Number of beneficiaries",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                },
                "program": {
                    "df": self.df.groupby(["Tipo", "Prioridad"]).aggregate({
                        "Email": "nunique"
                    }).reset_index(),
                    "x": "Email",
                    "y": "Tipo",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of direct beneficiaries per program",
                    "xaxis_name": "Number of beneficiaries",
                    "yaxis_name": "Program",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                },
                "professionals": {
                    "df": self.df[self.df["Implementación"].str.contains("Educadores")].groupby(["Entidad",
                                                                                                 "Prioridad"])
                    .aggregate({"Email": "nunique"})
                    .reset_index(),
                    "x": "Email",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of benefited professionals per state",
                    "xaxis_name": "Benefited professionals",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                },
                "schools": {
                    "df": self.df[(self.df["Centro de trabajo verificado"]) &
                                  (self.df["Tipo_cct"] == "Escuela")].groupby(["Entidad", "Prioridad"])
                    .aggregate({"Centro de trabajo": "nunique"})
                    .reset_index(),
                    "x": "Centro de trabajo",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of benefited verified schools per state",
                    "xaxis_name": "Benefited verified schools",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                },
                "teenagers": {
                    "df": self.df[self.df["Implementación"].str.contains("Estudiantes")].groupby(["Entidad",
                                                                                                  "Prioridad"])
                    .aggregate({"Email": "nunique"})
                    .reset_index(),
                    "x": "Email",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of direct benefited teenagers per state",
                    "xaxis_name": "Benefited teenagers",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                },
                "indirect": {
                    "df": self.df[self.df["Implementación"].str.contains("Estudiantes")].groupby(["Entidad",
                                                                                                  "Ben_directo"])
                    .agg(Conteo=("Ben_directo", "sum"))
                    .reset_index().astype(str),
                    "x": "Conteo",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Ben_directo",
                    "title": "Number of direct and indirect benefited teenagers per state",
                    "xaxis_name": "Benefited teenagers",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Beneficiary Type",
                    "legend_elements": {"25": "Indirect", "1": "Direct"}
                }
            },
            # "Professional Development": {
            #     "states": {
            #         "df": self.df[self.df["Implementación"].str.contains("Educadores")].groupby(["Entidad",
            #                                                                                      "Prioridad"])
            #         .aggregate({"Email": "nunique"})
            #         .reset_index(),
            #         "x": "Email",
            #         "y": "Entidad",
            #         "orientation": "h",
            #         "order": {
            #             "Prioridad": ["Kellogg's Priority", "Authorized Extension", "Other"],
            #             "Entidad": ["Campeche", "Quintana Roo", "Yucatán", "No data"]
            #         },
            #         "color": "Prioridad",
            #         "color_palette": {
            #             "Kellogg's Priority": "#22314E", "Authorized Extension": "#4A5E7A",
            #             "Other": "#A7B4CD"
            #         },
            #         "title": "Number of benefited professionals per state",
            #         "xaxis_name": "Benefited professionals",
            #         "yaxis_name": "State",
            #         "legend_name": "Municipality\nPriority",
            #         "legend_elements": None
            #     }
            # },
            # "PIBSE Teenagers": {
            #     "states": {
            #         "df": self.df[self.df["Implementación"].str.contains("Estudiantes")].groupby(["Entidad",
            #                                                                                       "Prioridad"])
            #         .aggregate({"Email": "nunique"})
            #         .reset_index(),
            #         "x": "Email",
            #         "y": "Entidad",
            #         "orientation": "h",
            #         "order": {
            #             "Prioridad": ["Kellogg's Priority", "Authorized Extension", "Other"],
            #             "Entidad": ["Campeche", "Quintana Roo", "Yucatán", "No data"]
            #         },
            #         "color": "Prioridad",
            #         "color_palette": {
            #             "Kellogg's Priority": "#22314E", "Authorized Extension": "#4A5E7A",
            #             "Other": "#A7B4CD"
            #         },
            #         "title": "Number of direct benefited teenagers per state",
            #         "xaxis_name": "Benefited teenagers",
            #         "yaxis_name": "State",
            #         "legend_name": "Municipality\nPriority",
            #         "legend_elements": None
            #     }
            # },
            "Reached Municipalities": {
                "states": {
                    "df": self.df.groupby(["Entidad", "Prioridad"])
                    .aggregate({"Municipio": "nunique"})
                    .reset_index(),
                    "x": "Municipio",
                    "y": "Entidad",
                    "orientation": "h",
                    "color": "Prioridad",
                    "title": "Number of benefited municipalities per state",
                    "xaxis_name": "Benefited municipalities",
                    "yaxis_name": "State",
                    "show_legend": True,
                    "legend_name": "Municipality\nPriority",
                    "legend_elements": None
                }
            }
            # "Benefited Schools": {
            #     "states": {
            #         "df": self.df[(self.df["Centro de trabajo verificado"]) &
            #                       (self.df["Tipo_cct"] == "Escuela")].groupby(["Entidad", "Prioridad"])
            #         .aggregate({"Centro de trabajo": "nunique"})
            #         .reset_index(),
            #         "x": "Centro de trabajo",
            #         "y": "Entidad",
            #         "orientation": "h",
            #         "order": {
            #             "Prioridad": ["Kellogg's Priority", "Authorized Extension", "Other"],
            #             "Entidad": ["Campeche", "Quintana Roo", "Yucatán", "No data"]
            #         },
            #         "color": "Prioridad",
            #         "color_palette": {
            #             "Kellogg's Priority": "#22314E", "Authorized Extension": "#4A5E7A",
            #             "Other": "#A7B4CD"
            #         },
            #         "title": "Number of benefited verified schools per state",
            #         "xaxis_name": "Benefited verified schools",
            #         "yaxis_name": "State",
            #         "legend_name": "Municipality\nPriority",
            #         "legend_elements": None
            #     }
            # }
        }

    def set_sidebar(self):
        """
        This function takes charge of the sidebar configurations. For the dropdown menus, it takes the columns as the
        options in said menus.
        :param df: Dataframe whose columns will work as the dropdown menus options.
        :return: Variables chosen in the dropdown menus.
        """
        # Sidebar
        with st.sidebar:
            st.write("Select an option to display")
            self.option = st.selectbox(label="Default", label_visibility="collapsed",
                                       options=self.graph_options.keys())

    def launch_dashboard(self):
        """
        This function does something...
        :return:
        """

        # st.write(data)
        self.set_header("Beneficiaries")

        self.set_sidebar()

        for k in self.graph_options[self.option]:
            st.write("")
            data = self.graph_options[self.option][k]
            self.set_header(data["title"], type_header="subtitle")
            st.plotly_chart(CreateGraphs(data).create_barchart())


st.set_page_config(layout="wide")
DashboardAlcance(ProcessData().read_data()["alcance"]).launch_dashboard()
