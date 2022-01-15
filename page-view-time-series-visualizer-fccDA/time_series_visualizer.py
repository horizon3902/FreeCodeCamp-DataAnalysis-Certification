import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')
months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) &
(df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14,6))
    plt.plot(df.index, df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year.values
    df_bar['month'] = df.index.month_name()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14,6))
    ax = sns.barplot(data=df_bar, x="year", hue="month", y="value", hue_order=months, ci=None)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(loc='upper left')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['monthNumbers'] = df_box['date'].dt.month
    df_box = df_box.sort_values('monthNumbers')

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(14,6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    sns.boxplot(data=df_box, x='month', y='value', ax=ax[1])
    ax[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    ax[1].set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
