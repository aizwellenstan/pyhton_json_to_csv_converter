import pandas as pd
import json
from pandas.io.json import json_normalize

df = pd.read_json('ark-fund.json')
print(df)

df.to_csv("out.csv", encoding='utf-8')