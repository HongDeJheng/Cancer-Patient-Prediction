import pandas as pd

def data_preprocessing(csv : str = "cancer patient data sets.csv", drop : list = []) -> pd.DataFrame:
    '''
    Read csv and preprocess the data

    Parameters
    ----------
    csv : str, optional
        Filename of a csv. The default is "cancer patient data sets.csv".
        
    drop: list
        Fields to drop

    Returns
    -------
    pd.DataFrame
        Output DataFrame after preprocessing.

    '''
    
    assert isinstance(csv, str) and ".csv" in csv
    assert isinstance(drop, list)
    assert len(drop) == 0 or (len(drop) > 0 and all(isinstance(x, str) for x in drop))
    
    df = pd.read_csv(csv)
    df.drop(drop, axis = 1, inplace = True)
    df.reset_index(drop = True, inplace = True)
    
    return df