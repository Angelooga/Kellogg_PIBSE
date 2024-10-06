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

    def create_barchart(self, **kwargs):
        """
        This function does something
        :param kwargs:
        :return:
        """
        fig = px.bar(data_frame=self.aux_data["df"], x=self.aux_data["x"], y=self.aux_data["y"],
                     orientation=self.aux_data["orientation"],
                     category_orders=self.aux_data["order"],
                     color=self.aux_data["color"],
                     color_discrete_map=self.aux_data["color_palette"],
                     # title=self.aux_data["title"],
                     text=self.aux_data["text"],
                     **kwargs
                     )
        fig.update_layout(xaxis_title=self.aux_data["xaxis_name"],
                          yaxis_title=self.aux_data["yaxis_name"],
                          legend_title=self.aux_data["legend_name"],
                          paper_bgcolor=self.bg_color,
                          plot_bgcolor=self.bg_color,
                          height=550)

        if self.aux_data["text_dtype"] == "float":
            fig.update_traces(texttemplate="%{value:.2f}")

        if self.aux_data["legend_elements"] is not None:
            new_names = self.aux_data["legend_elements"]
            fig.for_each_trace(lambda x: x.update(name=new_names[x.name],
                                                  legendgroup=new_names[x.name],
                                                  hovertemplate=x.hovertemplate.replace(x.name, new_names[x.name])
                                                  )
                               )

        if self.aux_data["line"] is not None:
            for k, i in self.aux_data["line"].items():
                if self.aux_data["orientation"] == "h":
                    fig.add_vline(x=i, line_width=1, line_dash="dash",
                                  line_color="grey", annotation_text=k)

        if self.aux_data["annotation"] is not None:
            fig.add_annotation(dict(xref="paper", yref="paper", x=0, y=-0.17,
                                    text=self.aux_data["annotation"],
                                    showarrow=False,
                                    textangle=0))
            fig.add_annotation(dict(xref="paper", yref="paper", x=0, y=-0.2,
                                    text="*p<0.05, **p<0.01, *** p<0.001",
                                    showarrow=False,
                                    textangle=0))

        return fig

    def create_forest_plot(self, **kwargs):
        """

        :return:
        """
        x = self.aux_data["x"]
        y = self.aux_data["y"]

        high = self.aux_data["high"]
        low = self.aux_data["low"]

        fig = go.Figure(data=go.Scatter(x=self.aux_data["df"][x], y=self.aux_data["df"][y],
                                        mode="markers",
                                        error_x=dict(
                                            type="data",
                                            array=abs(self.aux_data["df"][high] - self.aux_data["df"][x]),
                                            symmetric=False,
                                            arrayminus=abs(self.aux_data["df"][low] - self.aux_data["df"][x])
                                        ),
                                        marker=dict(color=self.aux_data["color"],
                                                    size=20)),
                        layout_xaxis_range=[-1, 1], layout={
                # "title": self.aux_data["title"],
                                                            "paper_bgcolor": self.bg_color,
                                                            "plot_bgcolor": self.bg_color})

        for i in [-1.0, -0.5, 0.0, 0.5, 1.0]:
            fig.add_vline(x=i, line_width=1, line_dash="dash", line_color="grey")

        fig.update_layout(width=750, height=500)

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

        fig = go.Figure(data=go.Heatmap(z=encoded.iloc[:, 2:],
                                        x=self.data["xaxis_name"],
                                        y=[encoded["Constructo"], encoded["Medición inglés"]],
                                        colorscale=self.data["color_scale"],
                                        text=annotations.iloc[:, 2:],
                                        texttemplate="%{text}",
                                        showscale=False),
                        layout={"title": self.data["title"],
                                "paper_bgcolor": self.bg_color,
                                "plot_bgcolor": self.bg_color})

        fig.update_layout(height=1200)

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
                    temp_fig = charts[type_graph]()
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
