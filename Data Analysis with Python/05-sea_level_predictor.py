import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    extension = pd.DataFrame({'Year': np.arange(1880,2051)})
    dfMerged = pd.merge(extension, df, on='Year', how='left')
    # print(extension)
    # print(dfMerged)

    # Create scatter plot
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    bestFit1 = linregress(x=df['Year']-df['Year'].min(),y=df['CSIRO Adjusted Sea Level'])
    ax.plot(dfMerged['Year'], ((dfMerged['Year']-dfMerged['Year'].min())*bestFit1.slope)+bestFit1.intercept)

    #bestFitExt = np.arange(2014,2051)
    #ax.plot(bestFitExt, ((bestFitExt-df['Year'].min())*bestFit1.slope+bestFit1.intercept),'--',label='Extrapolation since 1880')

    # Create second line of best fit
    dfCut = df.copy()[df['Year'] >= 2000]
    dfCutMerged = dfMerged.copy()[dfMerged['Year'] >= 2000]
    # #print(dfCut)
    bestFit2 = linregress(x=dfCut['Year']-dfCut['Year'].min(),y=dfCut['CSIRO Adjusted Sea Level'])
    ax.plot(dfCutMerged['Year'], ((dfCutMerged['Year']-dfCutMerged['Year'].min())*bestFit2.slope)+bestFit2.intercept)
    # bestFitExt = np.arange(2014,2051)
    # ax.plot(bestFitExt, ((bestFitExt-dfCut['Year'].min())*bestFit2.slope+bestFit2.intercept),'--',label='Extrapolation since 2000')


    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    #plt.legend(loc='best')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()
