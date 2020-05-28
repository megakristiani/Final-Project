import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
from clean import data_bir

def trend():
    df = data_bir()
    df_group = df['Style'].value_counts()[:26]
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def sugarscale():
    df = data_bir()
    df_group = df['SugarScale'].value_counts()[:26]
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def gravity():
    df = data_bir()
    fig = px.scatter(df, x="OG", y="FG", hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def ibu():
    df = data_bir()
    fig = px.scatter(df, x="IBU", y="ABV")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def color():
    df = data_bir()
    fig = px.scatter(df, x="Color", y="ABV")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json