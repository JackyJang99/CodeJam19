import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

age_dolphins = pd.read_csv(DATA_PATH.joinpath("ageDolphins.csv"))
mean_age_amount_0 = pd.read_csv(DATA_PATH.joinpath("meanAgeAmount.csv"))
mean_age_amount_1 = pd.read_csv(DATA_PATH.joinpath("meanAgeAmount1.csv"))

days_btw = pd.read_csv(DATA_PATH.joinpath("days_between_purchase.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Proportion of People Who Made Microtransactions per Age Group"], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id="graph-3",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=age_dolphins["Age"],
                                                    y=age_dolphins["Prop"],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Proportion"
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=650,
                                                height=200,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 50,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    )
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Average Number of Apps Installed per Age Group", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=mean_age_amount_0["Age"],
                                                    y=mean_age_amount_0["Mean"],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Free to play",
                                                ),
                                                go.Scatter(
                                                    x=mean_age_amount_1["Age"],
                                                    y=mean_age_amount_1["Mean"],
                                                    line={"color": "#b5b5b5"},
                                                    mode="lines",
                                                    name="Pay to win",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=650,
                                                height=300,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 50,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="eight columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Delay Between Installation and First Purchase (in Days)"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-5",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=days_btw["A"],
                                                    y=days_btw["B"],
                                                    name="Days",
                                                    marker=dict(color="#97151c"),
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=650,
                                                height=300,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 50,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
#                     html.Div(
#                         [
#                             html.Div(
#                                 [
#                                     html.H6(
#                                         [
#                                             "After-tax returns--updated quarterly as of 12/31/2017"
#                                         ],
#                                         className="subtitle padded",
#                                     ),
#                                     html.Div(
#                                         [
#                                             html.Table(
#                                                 make_dash_table(df_after_tax),
#                                                 className="tiny-header",
#                                             )
#                                         ],
#                                         style={"overflow-x": "auto"},
#                                     ),
#                                 ],
#                                 className=" twelve columns",
#                             )
#                         ],
#                         className="row ",
#                     ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
