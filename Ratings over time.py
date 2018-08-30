import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from scipy.stats import ttest_ind

metacritic_vg_data = pd.read_csv('Video_Games_Metacritic.csv', delimiter=',', na_values=['NaN','N/A', 'tbd'], parse_dates=True, index_col='Year_of_Release')

imdb_mov_data = pd.read_csv('IMDB-Movie-Data.csv', parse_dates=True, index_col='Year')

engine = create_engine('sqlite:///database.sqlite')

imdb_mov_data.drop(labels=['Rank', 'Title', 'Genre', 'Director', 'Actors', 'Runtime (Minutes)', 'Votes', 'Revenue (Millions)', 'Description', 'Metascore'], axis=1, inplace=True)
imdb_mov_data.dropna(how='any', inplace=True)


metacritic_vg_data.drop(labels=['Name', 'Platform', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Count', 'User_Count', 'Developer', 'Rating'], axis=1, inplace=True)
metacritic_vg_data.dropna(how='any', inplace=True)

# Process 'year of release' for metacritic, year for imdb, and pub_date for pitchfork_data

mus_rev = pd.read_sql_query("SELECT * FROM reviews", engine, parse_dates=['pub_date'], index_col='pub_date')
mus_rev.drop(labels=['reviewid', 'title','artist','url','best_new_music','author','author_type', 'pub_weekday','pub_day','pub_year','pub_month'], axis=1, inplace=True)


# Normalizing to 100

norm_hundred = lambda x: x * 10

metacritic_vg_data['User_Score'] = metacritic_vg_data['User_Score'].map(norm_hundred)

mus_rev['score'] = mus_rev['score'].map(norm_hundred)


# merging dataframes: (make sure you keep date as well)

pd.to_numeric(mus_rev['score'], errors='raise')

pd.to_numeric(imdb_mov_data['Rating'], errors='raise')



metacritic_vg_full = pd.concat([metacritic_vg_data['Critic_Score'], metacritic_vg_data['User_Score']])

full_data = pd.concat([metacritic_vg_full, imdb_mov_data['Rating'], mus_rev['score']])

full_data.index.name = 'date'

full_data.dropna(how='any', inplace=True)

# Visualize per year in a line-graph
