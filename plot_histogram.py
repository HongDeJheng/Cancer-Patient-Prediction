import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_histogram(df : pd.DataFrame) -> np.array:
    '''
    Plot the histogram of the data

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame after preprocessing.

    Returns
    -------
    None

    '''
    
    assert isinstance(df, pd.DataFrame)
    
    # correlation heatmap between variables
    fig, ax = plt.subplots(figsize = (36, 36))
    cmap = sns.diverging_palette(230, 20, as_cmap = True)
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype = bool))
    sns.heatmap(corr,
                mask = mask,
                cmap = cmap,
                vmax = .3,
                center = 0,
                square =True,
                linewidths = .5,
                cbar_kws = {"shrink": .7},
                annot = True,
                fmt = '.2f',
                ax = ax,
                annot_kws = {"size": 10})
    plt.savefig('img/corr.png', bbox_inches = 'tight')
    # plt.show()
    
    #Age distribution of patients
    plt.figure(figsize = (6,4))
    sns.kdeplot(df.Age, shade = True, color = "b")
    plt.title("Histogram for Age Distribution", fontsize = 10)
    plt.savefig('img/hist_Age.png', bbox_inches = 'tight')
    # plt.show()
    # print("Mean age is {}, median is {}, standard deviation is {}".format(df.Age.mean(), df.Age.median(), df.Age.std()))
    
    props = df.columns.values
    props = props[:-1]
    
    toIdx = {
        'Age': 0, 
        'Gender': 1, 
        'Air Pollution': 2,
        'Alcohol use' : 3, 
        'Dust Allergy' : 4, 
        'OccuPational Hazards' : 5,
        'Genetic Risk' : 6, 
        'chronic Lung Disease' : 7, 
        'Balanced Diet' : 8, 
        'Obesity' : 9,
        'Smoking' : 10, 
        'Passive Smoker' : 11, 
        'Chest Pain' : 12, 
        'Coughing of Blood' : 13,
        'Fatigue' : 14, 
        'Weight Loss' : 15, 
        'Shortness of Breath' : 16, 
        'Wheezing' : 17,
        'Swallowing Difficulty' : 18, 
        'Clubbing of Finger Nails' : 19,
        'Frequent Cold' : 20, 
        'Dry Cough' : 21, 
        'Snoring' : 22
    }
    
    # Distribution of other features
    plt.figure(figsize = (25, 30))
    for i in range(len(toIdx) - 1):
        plt.subplot(5, 5, i + 1)
        sns.countplot(df[props[i + 1]])
        plt.title("Histogram for {}".format(props[i + 1]), fontsize = 10)
    plt.savefig('img/hist.png', bbox_inches = 'tight')
    # plt.show()
    
    return props