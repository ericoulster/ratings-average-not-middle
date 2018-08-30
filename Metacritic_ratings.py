import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats

vg_rev = pd.read_csv('Video_Games_Metacritic.csv', delimiter=',', na_values=['N/A', 'tbd'])

# Compare Global_Sales and User_Score on a scatter

# scatter comparing critical review to user review
graph = sns.lmplot(x='Critic_Score', y='User_Score', data=vg_rev,
 scatter_kws={'alpha':0.1, 'color':'#cc33ff'}, line_kws={'color':'#ffbf00'}, x_jitter=0.5, y_jitter=0.5,
)

plt.title('Metacritic Videogame Review Scores')
plt.xlabel('Metacritic Critic Scores (Out of 100)')
plt.ylabel('Metacritic User Scores (Out of 10)')

plt.show()

vg_rev.dropna(inplace=True)

x = vg_rev[['Critic_Score']]
y=  vg_rev[['User_Score']]

print(stats.spearmanr(x,y))
