# code from the following article:
# https://towardsdatascience.com/visualizing-climate-change-a-step-by-step-guide-to-reproduce-climate-stripes-with-python-ea1d440e8e8d
# data from the following bureau:
# https://www.metoffice.gov.uk/hadobs/hadcrut5/data/current/download.html
# you need to download manually the following file:
# (under the heading "HadCRUT5 analysis time series: ensemble means and uncertainties", summary series "Global (NH+SH)/2"
# HadCRUT.5.0.1.0.analysis.summary_series.global.annual.csv

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap

df = pd.read_csv('HadCRUT.5.0.1.0.analysis.summary_series.global.annual.csv')
print(df.head())

# Create the figure and axes objects, specify the size and the dots per inches 
fig, ax = plt.subplots(figsize=(13.33,7.5), dpi = 96)

# Colours - Choose the colour map - 8 blues and 8 reds
cmap = ListedColormap([
    '#08306b', '#08519c', '#2171b5', '#4292c6',
    '#6baed6', '#9ecae1', '#c6dbef', '#deebf7',
    '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a',
    '#ef3b2c', '#cb181d', '#a50f15', '#67000d'])

# linearly normalizes data into the [0.0, 1.0] interval
norm = mpl.colors.Normalize(df['Anomaly (deg C)'].min(), df['Anomaly (deg C)'].max())

# Plot bars
bar = ax.bar(df['Time'], 1, color=cmap(norm(df['Anomaly (deg C)'])), width=1, zorder=2)

# Remove the spines
for spine in ['top', 'left', 'bottom', 'right']:
	ax.spines[spine].set_visible(False)
	#ax.spines[spine].set_edgecolor('white')

# Reformat x-axis label and tick labels
ax.set_xlabel('', fontsize=12, labelpad=10)
ax.xaxis.set_tick_params(pad=2, labelbottom=True, bottom=True, labelsize=12, labelrotation=0, labelcolor='white')
ax.set_xlim([df['Time'].min()-1, df['Time'].max()+1])

# Reformat y-axis label and tick labels
ax.set_ylabel('', fontsize=12, labelpad=10)
ax.set_yticks([])
ax.set_ylim([0, 1]) 

# Set source text
ax.text(x=0.1, y=0.12, s="Source: Met Office - https://www.metoffice.gov.uk/hadobs/hadcrut5/index.html / Original idea - Ed Hawkins", transform=fig.transFigure, ha='left', fontsize=10, alpha=.7, color='white')

# Set graph title
ax.set_title('Global Temperature Change (1850 - 2022)', loc='left', color='white', fontweight="bold", size=16, pad=10)

# Adjust the margins around the plot area
plt.subplots_adjust(left=0.11, right=None, top=None, bottom=0.2, wspace=None, hspace=None)

# Set a black background
fig.patch.set_facecolor('black')
ax.patch.set_facecolor('black')

plt.show()