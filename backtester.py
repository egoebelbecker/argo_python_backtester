import sys
from backtesting import Backtest
from smacross import SmaCross
import pandas as pd


if __name__ == "__main__":

    ticker = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]

    data = pd.read_csv(f'/tmp/marketdata_{ticker}_{start}_{end}.csv', index_col="Date", parse_dates=True)
    bt = Backtest(data, SmaCross, cash=10_000, commission=.002)
    stats = bt.run()

    stats.to_csv(f'/tmp/results_{ticker}_{start}_{end}.csv')
