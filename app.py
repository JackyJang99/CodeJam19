# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib

import os
import time

import base64
import datetime
import io
from dash.dependencies import Input, Output, State
import dash_table

from pages import (
    overview,
    pricePerformance,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

class_rep = pd.read_csv(DATA_PATH.joinpath("classfication_report.csv"))
confusion = pd.read_csv(DATA_PATH.joinpath("confusion.csv"))

app.config.suppress_callback_exceptions = True


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content"),
     html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Submit a file"], className="subtitle padded"
                                    ),
                                    html.Div([
                                        dcc.Upload(
                                            id='upload-data',
                                            children=html.Div([
                                                'Drag and Drop or ',
                                                html.A('Select Files')
                                            ]),
                                            style={
                                                'width': '100%',
                                                'height': '60px',
                                                'lineHeight': '60px',
                                                'borderWidth': '1px',
                                                'borderStyle': 'dashed',
                                                'borderRadius': '5px',
                                                'textAlign': 'center',
                                                'margin': '10px'
                                            },
                                            # Allow multiple files to be uploaded
                                            multiple=True
                                        ),
                                        html.Div(id='outtie'),
                                    ])
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Confusion Matrix",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(confusion)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Classification Report",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(class_rep)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
    ])
    


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/price-performance":
        return pricePerformance.create_layout(app)
    elif pathname == "/dash-financial-report/distributions":
        return distributions.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            pricePerformance.create_layout(app),
        )
    else:
        return overview.create_layout(app)

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df.to_csv(filename)
            
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    

@app.callback(Output('outtie', 'children'),
              [Input("upload-data", "contents"),
               Input('upload-data', 'filename')])
def upd(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
    
    while not os.path.exists("predicted.csv"):
        time.sleep(7)
    display = pd.read_csv('predicted.csv')
    
    return html.Div(
        [
            str(display['predicted'].array),
            html.Br([]),
            "Saving to predicted.csv..."
        ]
    )
               
    
    
    
    
    
    
if __name__ == "__main__":
    app.run_server(debug=True)

    
    
#     Consume -- just HOW do?