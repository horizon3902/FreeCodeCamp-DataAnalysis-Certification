import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res1 = linregress(x, y)
    x2 = list(range(1880,2051))
    y2 = []
    for year in x2:
      y2.append(res1.intercept + (res1.slope)*year)
    plt.plot(x2, y2, 'r')

    # Create second line of best fit
    x = df[df['Year'] > 1999]['Year']
    y = df[df['Year'] > 1999]['CSIRO Adjusted Sea Level']
    
    res2 = linregress(x, y)
    x2 = list(range(2000, 2051))
    y2 = []
    for year in x2:
      y2.append(res2.intercept + (res2.slope)*year)
    plt.plot(x2, y2, 'g')

    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()