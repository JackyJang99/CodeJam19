import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Product Summary"),
                                    html.Br([]),
                                    html.P(
                                        "Mistplay is the first Loyalty Platform for mobile gamers. \
                                        Players use Mistplay daily to play games, earn rewards and \
                                        connect with friends. With already over 3 million users around \
                                        the world, Mistplay is one of the fastest growing companies in Canada. \
                                        Mistplay leverages a wealth of in-game data and Machine Learning to \
                                        recommend the best games to its users. We empower mobile game studios \
                                        to acquire and deeply engage users around the world through our Loyalty Platform. \
                                        Mistplay is the Netflix of gaming.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Reviews"], className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("reviews.png")
                                            ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [
                            html.Br([]),html.Br([]),html.Br([]),
                            "Powered by  ",
                            html.Img(
                                src=app.get_asset_url("plotly.png"),
                                alt="Plotly",
                                title="Plotly",
                                className="logo_plt"
                            )
                        ]
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
