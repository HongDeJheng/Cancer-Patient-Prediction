from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def split_dataset(df : pd.DataFrame, label : str, labelEnc : dict, test_size : float = 0.3) -> tuple[np.array, np.array, np.array, np.array, np.array, np.array]:
    '''
    Split dataset into train, test, valid with specified portion

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    label : str
        Target column
    labelEnc : dict
        Label to replace.
    test_size : float
        Test set size.

    Returns
    -------
    tuple of np.array
        X_train, X_valid, X_test, y_train y_valid, y_test.

    '''
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(label, str)
    assert isinstance(labelEnc, dict)
    assert isinstance(test_size, float) and 0.0 < test_size < 1.0
    
    df[label].replace(labelEnc, inplace = True)
    dataTrain, dataValid = train_test_split(df.to_numpy(), test_size = test_size, random_state = 14, shuffle = True)
    dataValid, dataTest = train_test_split(dataValid, test_size = 0.5)
    print("# of train = {}".format(len(dataTrain)))
    print("# of valid = {}".format(len(dataValid)))
    print("# of test  = {}\n".format(len(dataTest)))
    
    X_train = dataTrain[:, :-1]
    X_valid = dataValid[:, :-1]
    X_test = dataTest[:, :-1]
    
    y_train = dataTrain[:, -1].astype(int)
    y_valid = dataValid[:, -1].astype(int)
    y_test = dataTest[:, -1].astype(int)
    
    return (X_train, X_valid, X_test, y_train, y_valid, y_test)