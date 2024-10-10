import streamlit as st
from dashboard import CreateDashboard
from graphs import CreateGraphs
from processing import ProcessData


class DashboardOutcomes(CreateDashboard):
    """
    This class does something...
    """

    def __init__(self, df):
        super().__init__(df)
        self.graph_options = {
            "Outcome Graphs (Vertical)": {
                "Professionals": {
                    "df": self.df["educadores"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Professionals Groups 1 & 2",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "show_legend": True,
                    "legend_name": None,
                    "legend_translation": "Constructo"
                },
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "title": "Outcomes Graph: Systematic Leadership Training",
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
            "Outcome Graphs (Horizontal)": {
                "Professionals": {
                    "df": self.df["educadores"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "color": "Constructo",
                    "title": "Outcomes Graph: Professionals Groups 1 & 2",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": None,
                    "line": "Effect_Size",
                    "show_legend": False
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
                    "title": "Outcomes Graph: Systematic Leadership Training",
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
                    "type_graph": "forest",
                    "high": "conf.high",
                    "low": "conf.low",
                    "orientation": None,
                    "color": "Comportamiento",
                    "title": "Detailed Outcomes Graph: Professionals Groups 1 & 2",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",
                    "line": "D-Cohen"
                },
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",
                    "high": "conf.high",
                    "low": "conf.low",
                    "orientation": None,
                    "color": "Comportamiento",
                    "title": "Outcomes Graph: Systematic Leadership Training",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",
                    "line": "D-Cohen"
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",
                    "high": "conf.high",
                    "low": "conf.low",
                    "orientation": None,
                    "color": "Comportamiento",
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",
                    "line": "D-Cohen"
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés_sig",
                    "type_graph": "forest",
                    "high": "conf.high",
                    "low": "conf.low",
                    "orientation": None,
                    "color": "Comportamiento",
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "xaxis_name": "D-Cohen",
                    "yaxis_name": "Scale",
                    "legend_name": "Construct",
                    "line": "D-Cohen"
                }
            },
            "Outcome Summary Table": {
                "general": {
                    "data": {
                        "df1": self.df["educadores"],
                        "df2": self.df["fls"],
                        "df3": self.df["estudiantes_g1"],
                        "df4": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                               "& Pre == 'inicial' & Post == 'final'")
                    },
                    "type_graph": "summary_table",
                    "color_scale": "Comportamiento",
                    "title": "Outcome Summary Table",
                    "xaxis_name": ["Professionals: Groups 1 & 2", "Systemic Leadership Training",
                                   "Teenagers: Groups 1, 2 & 3", "Teenagers: Groups 4 & 5"]
                }
            }
        }
        self.option = "Outcome Graphs (Horizontal)"

    def set_sidebar(self):
        """
        This function does something...
        :return:
        """
        with st.sidebar:
            self.option = st.selectbox(label="Default", label_visibility="collapsed",
                                       options=self.graph_options.keys())

    def launch_dashboard(self):
        """
        This function does something...
        :return:
        """
        self.set_header("Outcomes")

        self.set_sidebar()

        for k in self.graph_options[self.option]:
            data = self.graph_options[self.option][k]
            st.write(" ")
            self.set_header(data["title"], type_header="subtitle")
            CreateGraphs(data).set_plots_grid(type_graph=data["type_graph"])


st.set_page_config(layout="wide")
DashboardOutcomes(ProcessData().read_data()).launch_dashboard()
