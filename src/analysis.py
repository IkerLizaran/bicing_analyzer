import pandas as pd
import plotly.express as px
import logging

# Bar chart based on the number of colors of the stations
def plot_colors(df):
    df_num_colors = df["color"].value_counts().reset_index()
    fig = px.bar(x= df_num_colors["color"], y= df_num_colors["count"],
    labels={"x": "Color", "y": "Número de estaciones"})
    fig.show()

# Histogram based on the number of bikes in different stations
def plot_histogram(df):
    fig2 = px.histogram(df, x="num_bikes_available")
    fig2.show()

# Bar chart based on the number of ebikes vs mechanical ones
def plot_bike_types(df):
    df_types_of_bikes = pd.DataFrame({"type" : ["mechanical", "ebike"], "count" : [df["mechanical"].sum(), df["ebike"].sum()]})
    fig3 = px.bar(df_types_of_bikes, x="type", y="count")
    fig3.show()

# Scatter plot between "num_bikes_available" and "num_docks_available"
def plot_scatter(df):
    fig4 = px.scatter(df, x="num_bikes_available", y="num_docks_available")
    fig4.show()

# Map of Barcelona with all the stations and coloured based on bike availability
def plot_map(df):
    fig5 = px.scatter_map(df, lat="lat", lon="lon", color="color", size="capacity_size", 
    color_discrete_map={
        "grey": "grey",
        "red": "red",
        "orange": "orange",
        "yellow": "gold",
        "clear green": "lightgreen",
        "dark green": "darkgreen"
    }, 
    size_max=15, zoom=10,
    hover_data={"lat":False, "lon":False, "color":False, "capacity_size":False, "capacity":True, "num_bikes_available":True},
    hover_name=("name"), labels={"num_bikes_available" : "Bicis disponibles", "capacity" : "Capacidad"})
    fig5.show()


def analyzer(df):
    if df is not None:
        plot_map(df)
    else:
        logging.warning("Skipping the plot analysis: merge_df() returned no data")
        return None