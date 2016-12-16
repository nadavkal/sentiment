import pandas as pd
import numpy as np
import requests


from news.models import *
from news import utils


def update_stocks_db():
    df = utils.read_stocks()
    df.columns = map(utils.db_name_format, df.columns.tolist())
    def row_to_dict(row):
        return row.to_dict()
    df['db'] = df.T.apply(row_to_dict)
    new, updated = 0, 0
    for record in df.db.values:
        s, created = Stocks.objects.get_or_create(symbol=record['symbol'])
        s.name = record["name"]
        s.lastsale = record["lastsale"]
        s.marketcap = record["marketcap"]
        s.ipoyear = record["ipoyear"]
        s.sector = record["sector"]
        s.industry = record["industry"]
        s.summary_quate = record["summary_quate"]
        s.save()
        if created:
            new +=1
        else:
            updated += 1
    print 'Stocks Added:', new, '& updated:', updated


if __name__ == '__main__':
    update_stocks_db()