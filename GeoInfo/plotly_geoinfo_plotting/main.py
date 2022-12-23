from datetime import datetime, timedelta

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

from utils import make_globe_plot_per_continent
# This data is necessary to connect the continents from Wikidata to the countries required by Plotly for interactive GeoPlotting

gh_url = 'https://raw.githubusercontent.com'
gh_user = 'jendcruz22'
gh_repo = 'Medium-articles'
gh_branch = 'master'
gh_subdir = 'Geographical%20plotting%20with%20plotly'
gh_filename = 'GlobalGDP.csv'
csv_path = f"{gh_url}/{gh_user}/{gh_repo}/{gh_branch}/{gh_subdir}/{gh_filename}"

G_GDP = pd.read_csv(csv_path)

# map_title = f'{referer_class.title()} {access_method.title()} 
# {agent_type.title()} per Continent'

map_title = ''

make_globe_plot_per_continent(
    df=G_GDP,
    locations_col='CODE',
    data_col='GDP (BILLIONS)',
    text_col='COUNTRY',
    title=map_title,
    type='choropleth',
    lakecolor='rgb(0,191,255)',
    showlakes=True,
    log_plot=True,
    height=800,
    width=800
)