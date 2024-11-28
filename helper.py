import pandas as pd

CW_DATA_FILENAME = 'cw_dataset.csv'
CW_MYDATA_FILENAME = 'my_borough.csv'
MY_LOCAL_AUTHORITY_HIGHWAY = 'E09000021'
COL_TO_FILTER_WITH = 'Local_Authority_Highway'

def dataframe_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def get_my_dataset() -> pd.DataFrame:
    df_all_data = dataframe_from_csv(CW_DATA_FILENAME)
    return df_all_data[df_all_data[COL_TO_FILTER_WITH] == MY_LOCAL_AUTHORITY_HIGHWAY].copy()