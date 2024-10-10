from collections import defaultdict
import streamlit as st
import math
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


class CreateGraphs:
    """
    This class does something...
    """

    def __init__(self, data):
        self.data = data
        self.aux_data = defaultdict(lambda: None, data)
        self.bg_color = "#F5F0EA"
        self.legend_translations = {
            "Constructo": {
                "Autoconocimiento": "Self awareness",
                "Bienestar psicológico": "Well being",
                "Malestar psicológico": "Psychological distress",
                "Prosocialidad": "Prosociality",
                "Regulación emocional": "Emotion Regulation",
                "Seguridad y pertenencia": "Mindsets",
                "Creencias sobre el Aprendizaje Socioemocional": "Beliefs about  social and emotional learning",
                "Aprendizaje socioemocional en la comunidad educativa": "School-wide SEL implementation"
            },
            "Ben_directo": {
                "25": "Indirect",
                "1": "Direct"
            }
        }
        self.color_palettes = {
            "Constructo": {
                "Autoconocimiento": "#22314E",
                "Regulación emocional": "#1A7F83",
                "Malestar psicológico": "#F15D4A",
                "Prosocialidad": "#F0BA54",
                "Bienestar psicológico": "#4F6AA8",
                "Creencias sobre el Aprendizaje Socioemocional": "#F59794",
                "Seguridad y pertenencia": "#D094EA",
                "Aprendizaje socioemocional en la comunidad educativa": "#F59794"
            },
            "Prioridad": {
                "Kellogg's Priority": "#22314E",
                "Authorized Extension": "#4A5E7A",
                "Other": "#A7B4CD"
            },
            "Ben_directo": {
                "25": "#A7B4CD",
                "1": "#22314E"
            },
            "Comportamiento": {
                "Significativo/sentido esperado": "#22314E",
                "Significativo/sentido contrario": "#F15D4A",
                "No significativo/sentido esperado": "#8898b3",
                "No significativo/sentido contrario": "#F8BAB1"
            }
        }
        self.color_scales = {
            "Comportamiento": [[0, "#F9C6BF"], [0.25, "#F49184"], [0.5, "#D1DAEB"], [1, "#415E99"]]
        }
        self.category_orders = {
            "Constructo": ["Malestar psicológico", "Bienestar psicológico", "Regulación emocional", "Prosocialidad",
                           "Autoconocimiento", "Seguridad y pertenencia",
                           "Creencias sobre el Aprendizaje Socioemocional",
                           "Aprendizaje socioemocional en la comunidad educativa"],
            "Prioridad": ["Kellogg's Priority", "Authorized Extension", "Other"],
            "Entidad": ["Campeche", "Quintana Roo", "Yucatán", "No data"],
            "Tipo": ["Professionals", "SLT", "Professionals / SLT", "Teenagers"],
            "Ben_directo": ["25", "1"]
        }
        self.lines = {
            "Effect_Size": {
                "line": {
                    "Small": 0.2,
                    "Medium": 0.5,
                    "Big": 0.8
                },
                "annotation": {
                    1: {
                        "text": "*p<0.05, **p<0.01, *** p<0.001",
                        "x": 0,
                        "y": -0.175
                    }
                }
            },
            "D-Cohen": {
                "line": [-1.0, -0.5, 0.0, 0.5, 1.0],
                "annotation": {
                    1: {
                        "text": "*p<0.05, **p<0.01, *** p<0.001",
                        "x": 0,
                        "y": -0.225
                    }
                }
            }
        }
        self.apply_colors = {}
        self.show_legend = {}

    def create_barchart(self, **kwargs):
        """
        This function does something
        :param kwargs:
        :return:
        """
        st.write(self.aux_data["df"])

        fig = px.bar(data_frame=self.aux_data["df"], x=self.aux_data["x"], y=self.aux_data["y"],
                     orientation=self.aux_data["orientation"],
                     category_orders=self.category_orders,
                     color=self.aux_data["color"],
                     color_discrete_map=self.color_palettes[self.aux_data["color"]],
                     text=self.aux_data["text"]
                     )
        fig.update_layout(xaxis_title=self.aux_data["xaxis_name"],
                          yaxis_title=self.aux_data["yaxis_name"],
                          legend_title=self.aux_data["legend_name"],
                          paper_bgcolor=self.bg_color,
                          plot_bgcolor=self.bg_color,
                          height=550,
                          **kwargs)

        if self.aux_data["text_dtype"] == "float":
            fig.update_traces(texttemplate="%{value:.2f}")

        translate = self.aux_data["legend_translation"]
        if translate in self.legend_translations:
            new_names = self.legend_translations[translate]
            fig.for_each_trace(lambda x: x.update(name=new_names[x.name],
                                                  legendgroup=new_names[x.name],
                                                  hovertemplate=x.hovertemplate.replace(x.name, new_names[x.name])
                                                  )
                               )

        type_line = self.aux_data["line"]
        if type_line is not None:
            for k, i in self.lines[type_line]["line"].items():
                if self.aux_data["orientation"] == "h":
                    fig.add_vline(x=i, line_width=1, line_dash="dash",
                                  line_color="grey", annotation_text=k, annotation_position="bottom")

            annotation = self.lines[type_line]["annotation"]
            if annotation is not None:
                for k, i in annotation.items():
                    fig.add_annotation(dict(xref="paper", yref="paper", x=i["x"], y=i["y"],
                                            text=i["text"],
                                            showarrow=False,
                                            textangle=0))
                    fig.update_layout(xaxis={'showticklabels': False})

        fig.update_layout(
            legend=dict(
                xref="paper", yref="paper",
                orientation="h",
                entrywidth=160,
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            ),
            showlegend=self.data["show_legend"]
        )

        return fig

    def create_forest_plot(self, **kwargs):
        """

        :return:
        """
        x = self.aux_data["x"]
        y = self.aux_data["y"]
        high = self.aux_data["high"]
        low = self.aux_data["low"]
        color = self.aux_data["color"]

        fig = go.Figure(
            layout_xaxis_range=[-1, 1],
            layout={"paper_bgcolor": self.bg_color,
                    "plot_bgcolor": self.bg_color}
        )

        unique_colors = self.aux_data["df"][color].unique()

        for c in unique_colors:
            color_mask = self.aux_data["df"][color] == c

            fig.add_trace(
                go.Scatter(
                    x=self.aux_data["df"][x][color_mask],
                    y=self.aux_data["df"][y][color_mask],
                    mode="markers",
                    error_x=dict(
                        type="data",
                        array=abs(self.aux_data["df"][high][color_mask] - self.aux_data["df"][x][color_mask]),
                        symmetric=False,
                        arrayminus=abs(self.aux_data["df"][low][color_mask] - self.aux_data["df"][x][color_mask])
                    ),
                    marker=dict(
                        color=self.color_palettes[color][c],
                        size=20
                    ),
                    name=c
                )
            )

        type_line = self.aux_data["line"]
        for i in self.lines[type_line]["line"]:
            fig.add_vline(x=i, line_width=1, line_dash="dash", line_color="grey")

        annotation = self.lines[type_line]["annotation"]
        for k, i in annotation.items():
            fig.add_annotation(dict(xref="paper", yref="paper", x=i["x"], y=i["y"],
                                    text=i["text"],
                                    showarrow=False,
                                    textangle=0))

        fig.update_layout(width=750, height=500, showlegend=True,
                          legend=dict(
                              # xref="paper", yref="paper",
                              orientation="h",
                              entrywidth=175,
                              yanchor="bottom",
                              y=1.02,
                              xanchor="left",
                              x=0.6
                          ),
                          xaxis_title=self.aux_data["xaxis_name"],
                          **kwargs)

        return fig

    def create_summary_table(self):
        """
        This function does something...
        :return:
        """

        for k, i in self.data["data"].items():
            tempdf = i["D-cohen"].apply(lambda x: f"{x:.3f}")
            i["D-cohen_sig"] = tempdf + i["Significancia"].astype(str) + "/" \
                                      + i["Comportamiento"].astype(str)

        cols_to_keep = ["Constructo", "Medición inglés", "D-cohen_sig"]
        keys = list(self.data["data"].keys())
        merged = self.data["data"][keys[0]][cols_to_keep]

        for i in range(1, len(keys)):
            merged = pd.merge(merged, self.data["data"][keys[i]][cols_to_keep],
                              on=cols_to_keep[:2], how="outer", suffixes=(f"{keys[i-1]}", f"{keys[i]}"))

        if self.legend_translations["Constructo"] is not None:
            order = self.legend_translations["Constructo"]
            merged["Constructo"] = pd.Categorical(merged["Constructo"], ordered=True, categories=order)
            merged = merged.sort_values("Constructo", ascending=False)
            merged = merged.replace({"Constructo": self.legend_translations["Constructo"]})

        encoded = pd.DataFrame({})
        for col in merged.columns:
            encoded[col] = merged[col].apply(lambda x: 2 if "Significativo/sentido esperado" in str(x)
                                                         else 1 if "No significativo/sentido esperado" in str(x)
                                                         else -2 if "No significativo/sentido contrario" in str(x)
                                                         else -1 if "Significativo/sentido contrario" in str(x)
                                                         else x)

        def format_table(x):
            """
            This function does something...
            :param x:
            :return:
            """
            v = str(x)
            if v[0] == "-" and v[6:9] == "nan":
                new_str = v[:6] + v[9:]
                return new_str.split("/")[0]
            elif v[0] != "-" and v[5:8] == "nan":
                new_str = v[:5] + v[8:]
                return new_str.split("/")[0]
            elif v == "nan":
                return " "
            else:
                return v.split("/")[0]

        annotations = pd.DataFrame({})

        for col in merged.columns:
            annotations[col] = merged[col].apply(format_table)

        colorscale = self.data["color_scale"]
        fig = go.Figure(data=go.Heatmap(z=encoded.iloc[:, 2:],
                                        x=self.data["xaxis_name"],
                                        y=[encoded["Constructo"], encoded["Medición inglés"]],
                                        colorscale=self.color_scales[colorscale],
                                        text=annotations.iloc[:, 2:],
                                        texttemplate="%{text}",
                                        showscale=False),
                        layout={"paper_bgcolor": self.bg_color,
                                "plot_bgcolor": self.bg_color})

        fig.update_layout(height=1200, xaxis=dict(side='top'))

        return fig

    def set_plots_grid(self, type_graph: str = "barchart",
                       ncols: int = 2, last: list = None, idx: int = 1):
        """
        This
        :return:
        """
        if last is None:
            last = [1 / 4, 1 / 2, 1 / 4]

        charts = {
            "barchart": self.create_barchart,
            "forest": self.create_forest_plot,
            "summary_table": self.create_summary_table
        }

        counter = 0

        if self.aux_data["disaggregate"] is not None:

            param = self.aux_data["disaggregate"]

            if param in self.category_orders:
                disaggregate = [x for x in self.category_orders[param] if x in self.aux_data["df"][param].unique()]
            else:
                disaggregate = self.aux_data["df"][param].unique()

            nrows = math.ceil(len(disaggregate) / 2)
            rows = {}

            for i in range(nrows):

                if i == (nrows - 1) and (len(disaggregate) % 2) != 0:
                    rows[f"{i}"] = st.columns(last)
                else:
                    rows[f"{i}"] = st.columns([1 / 2, 1 / 2])

                for j in range(ncols):
                    self.aux_data["df"] = self.data["df"][self.data["df"][param] == disaggregate[counter]]

                    temp_fig = charts[type_graph](title=self.legend_translations[param][disaggregate[counter]])
                    if len(rows[f"{i}"]) == 2:
                        tile = rows[f"{i}"][j].container(border=True)
                        tile.plotly_chart(temp_fig)
                        counter += 1
                    else:
                        tile = rows[f"{i}"][idx].container(border=True)
                        tile.plotly_chart(temp_fig)
                        break

        else:
            tile = st.columns(1)
            tile[0].container(border=True).plotly_chart(charts[type_graph]())
