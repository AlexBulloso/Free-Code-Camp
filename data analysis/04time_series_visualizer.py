import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.dates import DateFormatter
from pandas.plotting import register_matplotlib_converters
from calendar import month_name
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(15)

    df.plot(use_index=True, y='value',xlabel='Date',ylabel='Page Views', style={'value': 'firebrick'}, ax=ax, title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig.autofmt_xdate(rotation=0, ha='center')
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_name[1:], ordered=True)
    df_bar = df_bar.groupby(['year','month'],as_index=False).agg('mean')
    df_bar.set_index('year', inplace=False)
    df_bar = df_bar.pivot(index='year',columns='month', values='value')
    #print(df_bar.head())
    fig, ax = plt.subplots()
    fig.set_figheight(7.5)
    fig.set_figwidth(7.5)

    df_bar.plot.bar(xlabel='Years',ylabel='Average Page Views', ax=ax)
    ax.legend(title="Months")
    #print(df_bar.head())


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_order, ordered=True)

    #print(df_box)
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(data=df_box, x='year', y='value', ax=ax1, hue='year', palette="tab10",flierprops=dict(marker='o', markerfacecolor='black', markersize=1))
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, hue='month', palette='husl',flierprops=dict(marker='o', markerfacecolor='black', markersize=1))
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
