import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import heapq
from tabulate import tabulate
import gc
import matplotlib.pyplot as plt
import seaborn as sns

fcd = pd.read_csv('/grefolc/herokudeploy/blob/main/bike_usage_2019.csv')

def summary(x):

    fig = plt.figure(figsize=(15, 10))
    plt.subplots_adjust(hspace = 0.6)
    sns.set_palette('pastel')
    
    plt.subplot(221)
    ax1 = sns.distplot(fcd[x], color = 'r')
    plt.title(f'{x.capitalize()} Density Distribution')
    
    plt.subplot(222)
    ax2 = sns.violinplot(x = fcd[x], palette = 'Accent', split = True)
    plt.title(f'{x.capitalize()} Violinplot')
    
    plt.subplot(223)
    ax2 = sns.boxplot(x=fcd[x], palette = 'cool', width=0.7, linewidth=0.6)
    plt.title(f'{x.capitalize()} Boxplot')
    
    plt.subplot(224)
    ax3 = sns.kdeplot(fcd[x], cumulative=True)
    plt.title(f'{x.capitalize()} Cumulative Density Distribution')
    
    plt.show()
    
    summary('Bicycle Stolen')
