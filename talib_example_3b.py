import talib as ta 
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf 
aapl = yf.download('AAPL', '2022-1-1','2023-03-01')

aapl['upper_band'], aapl['middle_band'], aapl['lower_band'] = ta.BBANDS(aapl['Close'], timeperiod =20)

aapl[['Close','upper_band','middle_band','lower_band']].plot(figsize=(15,15)) 
plt.show()