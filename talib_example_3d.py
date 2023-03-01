import talib as ta 
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf 
aapl = yf.download('AAPL', '2022-1-1','2023-03-01')

aapl['slowk'], aapl['slowd'] = ta.STOCH(aapl['High'], aapl['Low'], aapl['Close'], fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0) 
aapl[['slowk','slowd']].plot(figsize=(15,15)) 
plt.show()

aapl['fastk'], aapl['fastd'] = ta.STOCHF(aapl['High'], aapl['Low'], aapl['Close'], fastk_period=14, fastd_period=3, fastd_matype=0) 
aapl[['fastk','fastd']].plot(figsize=(15,15)) 
plt.show()