import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")

# 2
df['overweight'] = ((df['weight'] / ((df['height']/100) ** 2)) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# print(df.shape)
# df = df.drop(df[].index)
# print(df.shape)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco','active', 'overweight'])
    # 6
    print(df_cat)
    df_cat["total"] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'],as_index=True).count()
    print(df_cat)
    # 7
    fig = sns.catplot(df_cat, x='variable', y='total', hue="value", kind="bar", col="cardio").fig

   # 8

    
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()
# 10
def draw_heat_map():
    # 11
    
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 12
    corr = df_heat.corr()


    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15

    sns.heatmap(corr, mask=mask, annot=True, ax=ax, fmt=".1f")

    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
