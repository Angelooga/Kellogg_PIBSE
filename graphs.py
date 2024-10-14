from collections import defaultdict
import streamlit as st
import math
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


class CreateGraphs:
    """
    This class creates various types of charts (bar chart, forest plot, summary table, etc.)
    for visualizing data in a dashboard. It leverages Plotly for graph generation and Streamlit for display.
    """

    def __init__(self, data: dict):
        """
        Initialize the CreateGraphs object with the provided data and configuration settings.

        :param data: Dictionary containing the data and various settings for creating graphs.
        """
        self.data = data
        self.aux_data = defaultdict(lambda: None, data)
        self.bg_color = "#F5F0EA"   # Default background color for charts
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
        # Color palettes for various categories
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
                "Other": "#A7B4CD",
                "Not Reached":  "#FFFFFF"
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
        # Color scale for the summary table
        self.color_scales = {
            "Comportamiento": [[0, "#F9C6BF"], [0.25, "#F49184"], [0.5, "#D1DAEB"], [1, "#415E99"]]
        }
        # Category orders to display
        self.category_orders = {
            "Constructo": ["Malestar psicológico", "Bienestar psicológico", "Regulación emocional", "Prosocialidad",
                           "Autoconocimiento", "Seguridad y pertenencia",
                           "Creencias sobre el Aprendizaje Socioemocional",
                           "Aprendizaje socioemocional en la comunidad educativa"],
            "Prioridad": ["Kellogg's Priority", "Authorized Extension", "Other"],
            "Entidad": ["Campeche", "Quintana Roo", "Yucatán", "No data"],
            "Tipo": ["Professionals", "Systemic Leadership Training", "Professionals/Systemic Leadership Training",
                     "Teenagers"],
            "Ben_directo": ["25", "1"]
        }
        # Settings for adding lines to charts (like D-Cohen effect size thresholds)
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

    def create_barchart(self, **kwargs):
        """
        Creates a bar chart using Plotly with customizable features like orientation, color, text,
        and adding annotations or reference lines. Additional layout properties can be passed via kwargs.

        :param kwargs: Optional layout properties to customize the chart (like width, title, etc.)
        :return: A Plotly figure object representing the bar chart.
        """

        # Create a basic bar chart with Plotly Express.
        # 'data_frame': Data to be plotted, 'x' and 'y': Axis mappings, 'orientation': Horizontal or vertical bars.
        # 'category_orders': Dict to define the order of categories on axes, 'color': Category to color by.
        # 'color_discrete_map': Custom color mapping for categories, 'text': Labels to show on bars.
        fig = px.bar(
            data_frame=self.aux_data["df"],
            x=self.aux_data["x"],
            y=self.aux_data["y"],
            orientation=self.aux_data["orientation"],
            category_orders=self.category_orders,
            color=self.aux_data["color"],
            color_discrete_map=self.color_palettes[self.aux_data["color"]],
            text=self.aux_data["text"]
        )

        # Customize layout properties for the bar chart.
        # Set axis titles, legend title, and background color. Additional layout properties can be provided via kwargs.
        fig.update_layout(
            xaxis_title=self.aux_data["xaxis_name"],
            yaxis_title=self.aux_data["yaxis_name"],
            legend_title=self.aux_data["legend_name"],
            paper_bgcolor=self.bg_color,
            plot_bgcolor=self.bg_color,
            height=550,  # Set chart height
            **kwargs  # Apply any additional layout customizations passed via kwargs
        )

        # If the text data type is float, format the text on bars to show two decimal places.
        if self.aux_data["text_dtype"] == "float":
            fig.update_traces(texttemplate="%{value:.2f}")

        # Translate the legend labels if a translation is specified.
        # For example, translating internal variable names to more readable labels for the chart's legend.
        translate = self.aux_data["legend_translation"]
        if translate in self.legend_translations:
            # Get the translation mapping
            new_names = self.legend_translations[translate]

            # Update each trace (category) in the legend with the translated name.
            fig.for_each_trace(lambda x: x.update(
                name=new_names[x.name],  # Update the name
                legendgroup=new_names[x.name],  # Update the group name in the legend
                hovertemplate=x.hovertemplate.replace(x.name, new_names[x.name])  # Update the hover text
            ))

        # Add reference lines (like for effect sizes) to the chart if 'line' data is provided.
        type_line = self.aux_data["line"]
        if type_line is not None:
            # Loop through each defined line and add it to the chart.
            for k, i in self.lines[type_line]["line"].items():
                # Add a vertical line for horizontal bar charts (orientation == 'h').
                if self.aux_data["orientation"] == "h":
                    fig.add_vline(
                        x=i,  # Position of the vertical line
                        line_width=1, line_dash="dash",  # Style of the line
                        line_color="grey",  # Line color
                        annotation_text=k,  # Label for the line (e.g., 'Small', 'Medium', 'Large')
                        annotation_position="bottom"  # Position of the label
                    )

            # Add any annotations (e.g., statistical significance notes) to the chart.
            annotation = self.lines[type_line]["annotation"]
            if annotation is not None:
                for k, i in annotation.items():
                    # Add the annotation text at a specific location on the chart.
                    fig.add_annotation(dict(
                        xref="paper", yref="paper",  # Reference coordinates relative to the entire chart area
                        x=i["x"], y=i["y"],  # Position of the annotation
                        text=i["text"],  # Annotation text (e.g., "*p<0.05, **p<0.01")
                        showarrow=False,  # No arrow
                        textangle=0  # Horizontal text
                    ))

                    # Optionally hide tick labels on the x-axis (if desired) for a cleaner look.
                    fig.update_layout(xaxis={'showticklabels': False})

        # Customize the legend layout and positioning.
        fig.update_layout(
            legend=dict(
                xref="paper", yref="paper",  # Position the legend relative to the chart
                orientation="h",  # Horizontal legend
                entrywidth=160,  # Width for each legend item
                yanchor="bottom",  # Align legend to the bottom
                y=1.02,  # Vertical position (just above the chart)
                xanchor="left",  # Align legend to the left
                x=0  # Horizontal position
            ),
            showlegend=self.data["show_legend"]  # Show or hide the legend based on user settings
        )

        return fig  # Return the finalized bar chart figure.

    def create_forest_plot(self, **kwargs):
        """
        Creates a forest plot using Plotly, which typically shows estimates (like odds ratios) with confidence intervals.
        The plot is customizable with markers for different groups, error bars representing the confidence intervals,
        and optional reference lines and annotations.

        :param kwargs: Additional layout properties to customize the chart (e.g., title, margins).
        :return: A Plotly figure object representing the forest plot.
        """

        # Extract key columns from auxiliary data for easier access.
        x = self.aux_data["x"]  # Column for the central estimate (e.g., odds ratio)
        y = self.aux_data["y"]  # Column for the labels or categories (y-axis values)
        high = self.aux_data["high"]  # Column for the upper bound of the confidence interval
        low = self.aux_data["low"]  # Column for the lower bound of the confidence interval
        color = self.aux_data["color"]  # Column indicating different groups/colors in the plot

        # Initialize a Plotly figure with a specified range for the x-axis and background colors.
        fig = go.Figure(
            layout_xaxis_range=[-1, 1],  # Setting x-axis range from -1 to 1, useful for odds ratios or effect sizes
            layout={
                "paper_bgcolor": self.bg_color,  # Set the background color of the entire figure
                "plot_bgcolor": self.bg_color  # Set the background color of the plot area
            }
        )

        # Get the unique categories from the 'color' column to differentiate groups in the plot.
        unique_colors = self.aux_data["df"][color].unique()

        # Loop through each unique color group and add traces (markers with error bars) for that group.
        for c in unique_colors:
            # Create a mask to filter data by the current color/group.
            color_mask = self.aux_data["df"][color] == c

            # Add scatter plot points with error bars for this group.
            fig.add_trace(
                go.Scatter(
                    x=self.aux_data["df"][x][color_mask],  # X-values: central estimates
                    y=self.aux_data["df"][y][color_mask],  # Y-values: categories or labels
                    mode="markers",  # Use markers to represent the points
                    error_x=dict(
                        type="data",  # The error bars represent data values
                        array=abs(self.aux_data["df"][high][color_mask] - self.aux_data["df"][x][color_mask]),
                        # Upper bound of CI
                        symmetric=False,  # Error bars are asymmetric
                        arrayminus=abs(self.aux_data["df"][low][color_mask] - self.aux_data["df"][x][color_mask])
                        # Lower bound of CI
                    ),
                    marker=dict(
                        color=self.color_palettes[color][c],  # Set the marker color based on the group
                        size=20  # Marker size
                    ),
                    name=c  # Name for this trace (appears in the legend)
                )
            )

        # If reference lines (e.g., no-effect lines) are specified, add vertical dashed lines to the plot.
        type_line = self.aux_data["line"]
        for i in self.lines[type_line]["line"]:
            # Add a vertical reference line (e.g., at odds ratio 1 or effect size 0)
            fig.add_vline(x=i, line_width=1, line_dash="dash", line_color="grey")

        # Add annotations (e.g., notes for statistical significance) if provided.
        annotation = self.lines[type_line]["annotation"]
        for k, i in annotation.items():
            # Place the annotation text at specific positions on the plot.
            fig.add_annotation(dict(
                xref="paper", yref="paper",  # Coordinates relative to the full plot area
                x=i["x"], y=i["y"],  # X and Y position of the annotation
                text=i["text"],  # Annotation text (e.g., "*p<0.05")
                showarrow=False,  # No arrow pointing to the text
                textangle=0  # Keep the text horizontal
            ))

        # Update the layout of the figure with additional properties.
        fig.update_layout(
            width=750,  # Set the figure width
            height=500,  # Set the figure height
            showlegend=True,  # Show the legend
            legend=dict(
                # Customize the position and orientation of the legend
                orientation="h",  # Horizontal legend
                entrywidth=175,  # Set the width of each legend item
                yanchor="bottom",  # Anchor the legend at the bottom
                y=1.02,  # Position just above the plot area
                xanchor="left",  # Anchor the legend to the left
                x=0.6  # Position it more towards the center (on the right)
            ),
            xaxis_title=self.aux_data["xaxis_name"],  # Set the x-axis title (e.g., 'Odds Ratio')
            **kwargs  # Apply any additional layout customizations passed via kwargs
        )

        return fig  # Return the final forest plot figure.

    def create_summary_table(self):
        """
        Creates a summary table and visualizes it as a heatmap. The table merges multiple datasets on common columns
        and adds significance and behavior labels to effect size (Cohen's D). The result is color-coded for easy interpretation
        using a heatmap, with specific annotations for the table cells.

        :return: A Plotly heatmap figure object representing the summary table.
        """

        # Loop through each dataset and modify the 'D-cohen' column to include significance and behavior information.
        for k, i in self.data["data"].items():
            # Format 'D-cohen' to 3 decimal places, concatenate significance and behavior information.
            tempdf = i["D-cohen"].apply(lambda x: f"{x:.3f}")
            i["D-cohen_sig"] = tempdf + i["Significancia"].astype(str) + "/" + i["Comportamiento"].astype(str)

        # Define the columns to keep for merging.
        cols_to_keep = ["Constructo", "Medición inglés", "D-cohen_sig"]

        # Get the keys (names of the datasets) to iterate over for merging.
        keys = list(self.data["data"].keys())

        # Start merging the datasets by initializing with the first dataset.
        merged = self.data["data"][keys[0]][cols_to_keep]

        # Merge all datasets on 'Constructo' and 'Medición inglés' columns using outer join.
        for i in range(1, len(keys)):
            merged = pd.merge(merged, self.data["data"][keys[i]][cols_to_keep],
                              on=cols_to_keep[:2],  # Merge on the first two columns: 'Constructo' and 'Medición inglés'
                              how="outer",  # Outer join to include all rows from both datasets
                              suffixes=(f"{keys[i - 1]}", f"{keys[i]}"))  # Add suffixes to differentiate the columns

        # If a legend translation for 'Constructo' exists, reorder and rename the values.
        if self.legend_translations["Constructo"] is not None:
            # Get the desired order for 'Constructo' from legend translations.
            order = self.legend_translations["Constructo"]

            # Convert 'Constructo' to a categorical variable with the specified order, then sort it.
            merged["Constructo"] = pd.Categorical(merged["Constructo"], ordered=True, categories=order)
            merged = merged.sort_values("Constructo", ascending=False)  # Sort in descending order.

            # Replace 'Constructo' names with their translated values.
            merged = merged.replace({"Constructo": self.legend_translations["Constructo"]})

        # Create an empty dataframe to hold encoded values for color-coding the heatmap.
        encoded = pd.DataFrame({})

        # Encode values in the merged table for visualization in the heatmap.
        for col in merged.columns:
            encoded[col] = merged[col].apply(lambda x: 2 if "Significativo/sentido esperado" in str(x)
                                             else 1 if "No significativo/sentido esperado" in str(x)
                                             else -2 if "No significativo/sentido contrario" in str(x)
                                             else -1 if "Significativo/sentido contrario" in str(x)
                                             else x)

        # Define a helper function to format the table cells for annotation.
        def format_table(x):
            """
            Formats the table entries for display in the heatmap, removing NaN values and cleaning up strings.

            :param x: The table cell value to be formatted.
            :return: A formatted string suitable for display in the heatmap annotations.
            """
            v = str(x)
            if v[0] == "-" and v[6:9] == "nan":
                new_str = v[:6] + v[9:]
                return new_str.split("/")[0]  # Remove anything after the "/" (behavior info)
            elif v[0] != "-" and v[5:8] == "nan":
                new_str = v[:5] + v[8:]
                return new_str.split("/")[0]
            elif v == "nan":
                return " "  # Replace NaN with a space for better visualization
            else:
                return v.split("/")[0]  # Return only the Cohen's D part before the "/"

        # Create another dataframe to hold the formatted annotations for display in the heatmap.
        annotations = pd.DataFrame({})

        # Apply the format_table function to each column in the merged dataframe.
        for col in merged.columns:
            annotations[col] = merged[col].apply(format_table)

        # Create a heatmap using Plotly's Heatmap trace, visualizing the encoded values and showing annotations.
        colorscale = self.data["color_scale"]  # Get the color scale for the heatmap.
        fig = go.Figure(
            data=go.Heatmap(z=encoded.iloc[:, 2:],  # Use encoded values for color-coding (omit first 2 columns).
                            x=self.data["xaxis_name"],  # Set x-axis labels from data.
                            y=[encoded["Constructo"], encoded["Medición inglés"]],  # Set y-axis labels.
                            colorscale=self.color_scales[colorscale],  # Apply the specified color scale.
                            text=annotations.iloc[:, 2:],  # Use formatted annotations for each cell.
                            texttemplate="%{text}",  # Template to show text annotations on the heatmap.
                            showscale=False),  # Hide the color scale.
            layout={"paper_bgcolor": self.bg_color,  # Set background color of the figure.
                    "plot_bgcolor": self.bg_color})  # Set background color of the plot area.

        # Update layout settings: set figure height and position the x-axis labels at the top.
        fig.update_layout(height=1200, xaxis=dict(side='top'))

        return fig  # Return the final heatmap figure.

    def reached_municipalities_legend(self):
        """
        Creates a legend for municipalities that have or have not been reached. If all priority municipalities
        are reached, a message stating so is displayed. Otherwise, a list of municipalities not reached is
        generated and displayed in a Plotly figure.

        :return: A Plotly figure object displaying the legend with the appropriate text message.
        """
        import plotly.graph_objects as go  # Import Plotly graph objects for figure creation.

        # Create an empty figure object.
        fig = go.Figure()

        # Check if the dataframe is empty, indicating all priority municipalities were reached.
        if self.data["df"].empty:
            # If no municipalities are missing, display a message indicating all were reached.
            text = "<b>All priority municipalities were reached.</b>"
        else:
            # If some municipalities were not reached, get the unique list of those municipalities.
            not_reached = self.data["df"]["Not Reached"].unique()

            # Start composing the message with HTML formatting.
            text = "<b>Priority municipalities not reached:</b><br>"

            # Initialize an empty string to store municipality names.
            muns = ""

            # Loop through the list of not reached municipalities and concatenate their names into the string.
            for m in not_reached:
                muns = muns + f"{m}, "  # Add each municipality followed by a comma and a space.

            # Combine the message text and municipality list, then remove the trailing comma and space.
            text = (text + muns)[:-2]

        # Add an annotation (text) to the figure with HTML formatting.
        fig.add_annotation(
            text=text,  # The formatted text message.
            xref="paper", yref="paper",  # Use paper coordinates for absolute positioning.
            x=0.5, y=0.5,  # Center the text in the figure.
            showarrow=False,  # Disable any arrow that would point to the text.
            font=dict(size=40)  # Set the font size to 45 for readability.
        )

        # Update the layout to remove axis lines and grids since this is just a text-based visualization.
        fig.update_layout(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),  # Hide the x-axis completely.
            yaxis=dict(showgrid=False, zeroline=False, visible=False),  # Hide the y-axis completely.
            width=1200,  # Set the width of the figure.
            height=200  # Set the height of the figure.
        )

        # Return the created figure with the text message.
        return fig

    def set_plots_grid(self, type_graph: str = "barchart",
                       ncols: int = 2, last: list = None, idx: int = 1):
        """
        Arranges multiple plots in a grid layout. The method can create different types of plots based on the
        provided 'type_graph' argument. It supports disaggregating data based on a specified parameter and
        displaying the plots accordingly.

        :param type_graph: Type of graph to create (e.g., "barchart", "forest", "summary_table", or
                           "reached_municipalities_legend"). Default is "barchart".
        :param ncols: Number of columns to display the plots in. Default is 2.
        :param last: A list specifying the relative widths of the last row's columns. If None, default
                     values are used. Default is None.
        :param idx: Index to determine which column to use when the number of columns is less than expected.
                    Default is 1.
        :return: None
        """
        # Set default column widths for the last row if not provided.
        if last is None:
            last = [1 / 4, 1 / 2, 1 / 4]

        # Dictionary mapping plot types to their respective creation methods.
        charts = {
            "barchart": self.create_barchart,
            "forest": self.create_forest_plot,
            "summary_table": self.create_summary_table,
            "reached_municipalities_legend": self.reached_municipalities_legend
        }

        counter = 0  # Initialize a counter for tracking the number of plots created.

        # Check if there is a disaggregate parameter set in the aux_data.
        if self.aux_data["disaggregate"] is not None:
            param = self.aux_data["disaggregate"]  # Get the disaggregate parameter.

            # Determine the disaggregate values based on category orders or unique values in the DataFrame.
            if param in self.category_orders:
                disaggregate = [x for x in self.category_orders[param] if x in self.aux_data["df"][param].unique()]
            else:
                disaggregate = self.aux_data["df"][param].unique()

            nrows = math.ceil(len(disaggregate) / 2)  # Calculate the number of rows needed.
            rows = {}  # Dictionary to hold the row columns for layout.

            # Loop through the number of rows to create the grid layout.
            for i in range(nrows):
                # Check if it's the last row and if it has an odd number of disaggregates.
                if i == (nrows - 1) and (len(disaggregate) % 2) != 0:
                    # Create columns with specified widths for the last row.
                    rows[f"{i}"] = st.columns(last)
                else:
                    # Create two equal columns for other rows.
                    rows[f"{i}"] = st.columns([1 / 2, 1 / 2])

                # Loop through the number of columns to place the plots.
                for j in range(ncols):
                    # Filter the DataFrame for the current disaggregate value.
                    self.aux_data["df"] = self.data["df"][self.data["df"][param] == disaggregate[counter]]

                    # Create the plot using the specified type and translate the title if necessary.
                    temp_fig = charts[type_graph](title=self.legend_translations[param][disaggregate[counter]])

                    if len(rows[f"{i}"]) == 2:  # Check if there are two columns in the row.
                        tile = rows[f"{i}"][j].container(border=True)  # Create a container for the plot.
                        tile.plotly_chart(temp_fig)  # Display the plot in the container.
                        counter += 1  # Increment the counter to move to the next disaggregate.
                    else:  # If the number of columns is less than expected (e.g., in the last row).
                        tile = rows[f"{i}"][idx].container(border=True)  # Use the specified index for the tile.
                        tile.plotly_chart(temp_fig)  # Display the plot in the tile.
                        break  # Exit the loop after placing the plot.

        else:  # If there is no disaggregate parameter.
            tile = st.columns(1)  # Create a single column layout.
            tile[0].container(border=True).plotly_chart(charts[type_graph]())  # Display the plot.

