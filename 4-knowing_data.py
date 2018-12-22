import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('cleaned_data.csv')
data.head()

categories = list(data.columns.values)
categories = categories[1:]

"""

df_title = data.drop(['title'], axis=1)
counts = []
categories = list(df_title.columns.values)
for i in categories:
    counts.append((i, df_title[i].sum()))
df_stats = pd.DataFrame(counts, columns=['category', 'number_of_titles'])



df_stats.plot(x='category', y='number_of_titles', kind='bar', legend=False, grid=True, figsize=(8, 5))
plt.title("Number of titles per category")
plt.ylabel('# of Occurrences', fontsize=12)
plt.xlabel('category', fontsize=12)
"""

lens = data.title.str.len()
lens.hist(bins = np.arange(0,51,1))
