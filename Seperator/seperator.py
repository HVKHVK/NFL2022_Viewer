import pandas as pd
import warnings
from config import *

warnings.simplefilter(action='ignore', category=FutureWarning)

games = pd.read_csv(GAMES_PATH)

tracking = [TRACKING_2018_PATH, TRACKING_2019_PATH, TRACKING_2020_PATH]

for track_year in tracking:
    tracking = pd.read_csv(track_year)

    unique = tracking["gameId"].unique()

    for id in unique:
        dataframe = tracking[tracking["gameId"] == id]
        dataframe["home"] = games[games["gameId"] == id]["homeTeamAbbr"].values.item(0)
        dataframe["away"] = games[games["gameId"] == id]["visitorTeamAbbr"].values.item(0)
        dataframe["week"] = games[games["gameId"] == id]["week"].values.item(0)
        dataframe["gameTimeEastern"] = games[games["gameId"] == id]["gameTimeEastern"].values.item(0)
        dataframe.to_csv("../Exports/" + str(id) + ".csv")
    del tracking