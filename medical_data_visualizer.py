import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
pd.set_option('mode.chained_assignment',None)
df['bmi'] = df['weight']/((df['height']/100)**2)
df['bmi'].describe()
df['overweight'] = 0
df.overweight[df['bmi']>25] = 1
df.drop('bmi', inplace=True, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol[df.cholesterol == 1] = 0
df.cholesterol[df.cholesterol > 1] = 1
df.gluc[df.gluc == 1] = 0
df.gluc[df.gluc > 1] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"] )


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    

    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df
    df_heat = df_heat[df_heat.ap_lo <= df_heat.ap_hi]
    df_heat = df_heat[df_heat.height >= df_heat.height.quantile(0.025)]
    df_heat = df_heat[df_heat.height <= df_heat.height.quantile(0.975)]
    df_heat = df_heat[df_heat.weight >= df_heat.weight.quantile(0.025)]
    df_heat = df_heat[df_heat.weight <= df_heat.weight.quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    corrMatrix = round(df.corr(),1)

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corrMatrix, annot=True, mask=mask, fmt = '.1f', linewidths = .2, center = .08)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
