import os
import pandas as pd

from finance_basics.settings.settings import PRICES_FOLDER, RENAMING_DICT


def load_returns_from_yahoo_file(ticker: str) -> pd.DataFrame:
    """
    Method to compute the returns of a stock from the prices file

    :param ticker: str
    :return: pd.DataFrame
    """
    data_file = os.path.join(PRICES_FOLDER, f'{ticker}.csv')
    df = pd.read_csv(
        filepath_or_buffer=data_file,
        converters={'Date': pd.to_datetime}
    )
    df = df.rename(columns=RENAMING_DICT)
    df = df.set_index('trading_date')
    df['return'] = df['adj_close'].pct_change()
    returns = df[['return']].rename(columns={'return': f'return_{ticker}'})
    return returns