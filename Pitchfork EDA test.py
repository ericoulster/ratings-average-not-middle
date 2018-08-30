import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.sqlite')

mus_rev = pd.read_sql_query("SELECT * FROM reviews", engine)

print(mus_rev.head())

plt.hist(mus_rev['score'], bins='auto', linewidth=1, color='#6666ff', edgecolor='#000066')
plt.title('Pitchfork Music Reviews')
plt.xlabel('Review Score (Out of 10.00)')
plt.ylabel('# of reviews')


plt.show()

print(np.percentile(mus_rev['score'], 50))
