import glob
from pandas_datareader import data
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

pd.core.common.is_list_like = pd.api.types.is_list_like

START_DAY = "2024-01-01"
END_DAY = "2024-08-01"
brand = '^N225'

df = yf.download(brand, START_DAY, END_DAY )

print(df.head(10))

# 陽線；赤色，陰線：青色
mc = mpf.make_marketcolors(up="red", down="blue", inherit=True)

# チャートの色，背景の色
style = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, title="N225", type="candle", figratio=(10,5), mav=(5, 25, 75), volume=True, style=style)