import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats
from sqlalchemy import create_engine

## data import ##

# import videogame data

metacritic_vg_data = pd.read_csv('Video_Games_Metacritic.csv', delimiter=',', na_values=['NaN','N/A', 'tbd'])

# import movie data

imdb_mov_data = pd.read_csv('IMDB-Movie-Data.csv')

# import pitchfork data (Via SQL - converted into pandas Dataframe)

engine = create_engine('sqlite:///database.sqlite')

mus_rev = pd.read_sql_query("SELECT * FROM reviews", engine)

## isolating relevant columns from datasets ##

# metascore isolation

vg_critic = metacritic_vg_data[['Critic_Score']].copy()
vg_critic.dropna(inplace=True)
vg_critic.columns = ['score']

# userscore isolation

vg_user_unadjusted = metacritic_vg_data[['User_Score']].copy()
vg_user_unadjusted.dropna(inplace=True)
vg_user = (vg_user_unadjusted * 10)
vg_user.columns = ['score']

# imdb isolation

imdb_rating_unadjusted = imdb_mov_data[['Rating']].copy()
imdb_rating_unadjusted.dropna(inplace=True)
imdb_rating = (imdb_rating_unadjusted * 10)
imdb_rating.columns = ['score']

# Pitchfork isolation

mus_score_unadjusted = mus_rev[['score']].copy()
mus_score_unadjusted.dropna(inplace=True)
mus_score = (mus_score_unadjusted * 10)

# concatenating all isolated columns into a master-list

master_list = pd.concat([vg_critic, vg_user, imdb_rating, mus_score], ignore_index=True)

master_list['score'] = master_list.score.astype(float)

master_list.reset_index()

sns.distplot(master_list, bins=100)
plt.tick_params(rotation=90)
plt.title("Frequency of Review Scores, Based on All Above Datasets \n μ = 69.98, σ = 13.587395, Median = 72.0")
plt.xlabel("Score Given (Normalized to 100)")
plt.ylabel("Proportion of Total Scores (Out of 1)")
plt.show()

print(np.mean(master_list))
print(np.std(master_list))
print(np.percentile(master_list, 50))
