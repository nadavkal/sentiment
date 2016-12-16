import datetime
import glob

import pandas as pd

from news.AppConfigs import KMB_KEYS, STOCK_LISTS



def kmb_converter(value, convert_to=float):
    value = value.lower()
    keys = set(KMB_KEYS.keys()) & set(value)
    multiplier = 1.0
    for key in keys:
        multiplier *= KMB_KEYS[key]
    value = "".join([v for v in value if v in '0123456789.'])
    value = convert_to(float(value) * multiplier(value))
    return value


def strdate_to_datetime(strdate, format='%m/%d/%y'):
    return datetime.datetime.strptime(strdate, format)


def read_stocks():
    df = pd.concat([pd.read_csv(link) for link in STOCK_LISTS])
    df.drop("Unnamed: 8", axis=1, inplace=True)
    return df


def db_name_format(text):
    return text.lower().replace(' ', '_')


def read_stock_lists_from_files():
    df = pd.concat([pd.read_csv(filename) for filename in glob.iglob('../companylist*.csv')])
    df.drop("Unnamed: 8", axis=1, inplace=True)
    return df
