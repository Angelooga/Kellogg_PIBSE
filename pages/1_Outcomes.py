import streamlit as st
import plotly.express as px
from dashboard import CreateDashboard, set_header
from graphs import CreateGraphs
from processing import ProcessData


class DashboardOutcomes(CreateDashboard):
    """
    This class does something...
    """

    def __init__(self, df):
        super().__init__(df)
        self.option = "Outcome Graphs (Horizontal)"
        self.graph_options = {
            "Outcome Graphs (Vertical)": {
                "Professionals": {
                    "df": self.df["educadores"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8",
                        "Aprendizaje socioemocional en la comunidad educativa": "#F59794"
                    },
                    "title": "Outcomes Graph: Professionals Groups 1 & 2",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    }
                },
                "Professionals_FLS": {
                    "df": self.df["fls"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Aprendizaje socioemocional en la comunidad educativa": "#F59794"
                    },
                    "title": "Outcomes Graph: Systematic Leadership Training",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    }
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8"
                    },
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation"
                    }
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "x": "Medición inglés",
                    "y": "D-cohen",
                    "type_graph": "barchart",
                    "orientation": "v",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8",
                        "Creencias sobre el Aprendizaje Socioemocional": "#F59794",
                        "Seguridad y pertenencia": "#D094EA"
                    },
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "text": "Significancia",
                    "text_dtype": "str",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Seguridad y pertenencia": "Belonging",
                        "Creencias sobre el Aprendizaje Socioemocional": "Social Emotional Learning"
                    }
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
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8",
                        "Aprendizaje socioemocional en la comunidad educativa": "#F59794"
                    },
                    "title": "Outcomes Graph: Professionals Groups 1 & 2",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    },
                    "line": {
                        "S": 0.2,
                        "M": 0.5,
                        "B": 0.8
                    },
                    "annotation": "S: Small, M: Medium, B: Big"
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
                    "color_palette": {
                        "Aprendizaje socioemocional en la comunidad educativa": "#F59794"
                    },
                    "title": "Outcomes Graph: Systematic Leadership Training",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    },
                    "line": {
                        "S": 0.2,
                        "M": 0.5,
                        "B": 0.8
                    },
                    "annotation": "S: Small, M: Medium, B: Big"
                },
                "Teenagers_g1": {
                    "df": self.df["estudiantes_g1"],
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8"
                    },
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation"
                    },
                    "line": {
                        "S": 0.2
                    },
                    "annotation": "S: Small, M: Medium, B: Big"
                },
                "Teenagers_g2": {
                    "df": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                          "& Pre == 'inicial' & Post == 'final'"),
                    "disaggregate": "Constructo",
                    "x": "D-cohen",
                    "y": "Medición inglés",
                    "type_graph": "barchart",
                    "orientation": "h",
                    "order": None,
                    "color": "Constructo",
                    "color_palette": {
                        "Autoconocimiento": "#22314E", "Regulación emocional": "#1A7F83",
                        "Malestar psicológico": "#F15D4A", "Prosocialidad": "#F0BA54",
                        "Bienestar psicológico": "#4F6AA8",
                        "Creencias sobre el Aprendizaje Socioemocional": "#F59794",
                        "Seguridad y pertenencia": "#D094EA"
                    },
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "text": "D-cohen",
                    "text_dtype": "float",
                    "yaxis_name": "Scale",
                    "xaxis_name": "D-Cohen/Effect Size",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Seguridad y pertenencia": "Belonging",
                        "Creencias sobre el Aprendizaje Socioemocional": "Social Emotional Learning"
                    },
                    "line": {
                        "S": 0.2
                    },
                    "annotation": "S: Small, M: Medium, B: Big"
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
                    "order": None,
                    "color": self.df["educadores"]["Comportamiento"]
                    .apply(lambda x: "#415E99" if x == "Significativo/sentido esperado"
                           else "#F49184" if x == "Significativo/sentido contrario"
                           else "#D1DAEB" if x == "No significativo/sentido esperado"
                           else "#F9C6BF"),
                    "color_palette": None,
                    "title": "Detailed Outcomes Graph: Professionals Groups 1 & 2",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    }
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
                    "order": None,
                    "color": self.df["fls"]["Comportamiento"]
                    .apply(lambda x: "#415E99" if x == "Significativo/sentido esperado"
                           else "#F49184" if x == "Significativo/sentido contrario"
                           else "#D1DAEB" if x == "No significativo/sentido esperado"
                           else "#F9C6BF"),
                    "color_palette": None,
                    "title": "Outcomes Graph: Systematic Leadership Training",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Aprendizaje socioemocional en la comunidad educativa": "Social Emotional Learning"
                    }
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
                    "order": None,
                    "color": self.df["estudiantes_g1"]["Comportamiento"]
                    .apply(lambda x: "#415E99" if x == "Significativo/sentido esperado"
                           else "#F49184" if x == "Significativo/sentido contrario"
                           else "#D1DAEB" if x == "No significativo/sentido esperado"
                           else "#F9C6BF"),
                    "color_palette": None,
                    "title": "Outcomes Graph: Teenagers Groups 1 & 2",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation"
                    }
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
                    "order": None,
                    "color": self.df["estudiantes_g2"].query("Subanálisis == 'Todos-as 1+ CA' "
                                                             "& Pre == 'inicial' & Post == 'final'")["Comportamiento"]
                    .apply(lambda x: "#415E99" if x == "Significativo/sentido esperado"
                           else "#F49184" if x == "Significativo/sentido contrario"
                           else "#D1DAEB" if x == "No significativo/sentido esperado"
                           else "#F9C6BF"),
                    "color_palette": None,
                    "title": "Outcomes Graph: Teenagers Groups 3, 4 & 5",
                    "xaxis_name": "Scale",
                    "yaxis_name": "D-Cohen",
                    "legend_name": "Construct",
                    "legend_elements": {
                        "Autoconocimiento": "Self-knowledge",
                        "Bienestar psicológico": "Well-being",
                        "Malestar psicológico": "Discomfort",
                        "Prosocialidad": "Prosociality",
                        "Regulación emocional": "Emotional Regulation",
                        "Seguridad y pertenencia": "Belonging",
                        "Creencias sobre el Aprendizaje Socioemocional": "Social Emotional Learning"
                    }
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
                    "color_scale": [[0, "#F9C6BF"], [0.25, "#F49184"],
                                    [0.5, "#D1DAEB"], [1, "#415E99"]],
                    "title": "Outcome Summary Table",
                    "xaxis_name": ["Professionals: Groups 1 & 2", "Systemic Leadership Training",
                                   "Teenagers: Groups 1, 2 & 3", "Teenagers: Groups 4 & 5"],
                    "yaxis_name": None
                }
            }
        }

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
        set_header("Outcomes")

        self.set_sidebar()

        for k in self.graph_options[self.option]:
            data = self.graph_options[self.option][k]
            st.write(" ")
            set_header(data["title"], type="subtitle")
            CreateGraphs(data).set_plots_grid(type_graph=data["type_graph"])


st.set_page_config(layout="wide")
DashboardOutcomes(ProcessData().read_data()).launch_dashboard()
