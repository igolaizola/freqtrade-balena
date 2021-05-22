# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy, merge_informative_pair
from datetime import datetime, timedelta
from freqtrade.persistence import Trade
from pandas import DataFrame
import pandas
# --------------------------------


class Doge(IStrategy):
    """
    author@: igolaizola
    strategy to backtest elon musk's tweets
    """

    # Minimal ROI designed for the strategy.
    # adjust based on market conditions. We would recommend to keep it low for quick turn arounds
    # This attribute will be overridden if the config file contains "minimal_roi"
    minimal_roi = {
        "0": 0.5
    }

    # Optimal timeframe for the strategy
    timeframe = '1m'

    # Optimal stoploss designed for the strategy
    stoploss = -0.10
    trailing_stop = True
    use_custom_stoploss = True

    def custom_stoploss(self, pair: str, trade: 'Trade', current_time: datetime,
                        current_rate: float, current_profit: float, **kwargs) -> float:

        # Make sure you have the longest interval first - these conditions are evaluated from top to bottom.
        if current_time - timedelta(minutes=120) > trade.open_date_utc:
            return -0.02
        elif current_time - timedelta(minutes=60) > trade.open_date_utc:
            return -0.05
        return -0.10

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Dates when @elonmusk twitted "doge", for backtesting
        tw = [
                "2021-04-28 06:21:00+00:00",
                "2021-04-15 04:33:00+00:00",
                "2021-04-01 10:25:00+00:00",
                "2021-03-13 23:51:00+00:00",
                "2021-03-13 23:46:00+00:00",
                "2021-03-13 23:41:00+00:00",
                "2021-03-06 04:42:00+00:00",
                "2021-03-01 19:57:00+00:00",
                "2021-02-21 21:27:00+00:00",
                "2021-02-14 23:25:00+00:00",
                "2021-02-11 09:09:00+00:00",
                "2021-02-10 15:08:00+00:00",
                "2021-02-07 22:25:00+00:00",
                "2021-02-04 08:27:00+00:00",
                "2021-02-04 08:15:00+00:00",
                "2021-02-04 07:36:00+00:00",
                "2020-12-20 09:30:00+00:00",
            ]
        dataframe.loc[
            (
                dataframe['date'].isin(tw)
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
            ),
            'sell'] = 1
        return dataframe
