import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Make hists into seaborn b/c (makes data easier to read)

# make a function to take in the dataframe,
# compute mean and std,
# then use it to plot the pdf

######################

# Videogame Portion

vg_rev = pd.read_csv('Video_Games_Metacritic.csv', delimiter=',', na_values=['NaN','N/A', 'tbd'])

# Critic reviews

vg_rev_critic = vg_rev[['Critic_Score']]

vg_rev_critic.dropna(how='any', inplace=True)

n, bins, patches = plt.hist(vg_rev_critic, bins=26, linewidth=1, edgecolor='#0a2b60')



plt.tick_params(rotation=90)
plt.tight_layout()
plt.title('Metacritic Metascore for Videogames')
plt.xlabel('Metacritic Score (out of 100)')
plt.ylabel('# of reviews')
plt.show()

plt.cla()
plt.clf()

# User reviews

vg_rev_user = vg_rev[['User_Score']]

vg_rev_user.dropna(how='any', inplace=True)

plt.hist(vg_rev_user, bins=26, linewidth=1, color='#ff9900', edgecolor='#b36b00')

plt.tick_params(rotation=90)
plt.tight_layout()
plt.title('Metacritic User Score for Videogames')
plt.xlabel('Metacritic Score (out of 10)')
plt.ylabel('# of reviews')
plt.show()

plt.cla()
plt.clf()

# Movie Portion

#######################

mov_rev = pd.read_csv('IMDB-Movie-Data.csv', delimiter=',')

# IMDB Site Reviews

mov_rev_imdb = mov_rev[['Rating']]

mov_rev_imdb.dropna(how='any', inplace=True)

mov_rev_imdb.groupby('Rating')

plt.hist(mov_rev_imdb, bins='auto', linewidth=1, color='#00cc00', edgecolor='#004d00')

plt.tick_params(rotation=90)
plt.tight_layout()
plt.title('IMDB Review Scores for Movies (by Users)')
plt.xlabel('IMDB Score (out of 10)')
plt.ylabel('# of reviews')
plt.show()

plt.cla()
plt.clf()
