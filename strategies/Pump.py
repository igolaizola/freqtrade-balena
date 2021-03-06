# --- Do not remove these libs ---
from freqtrade.strategy import IStrategy, merge_informative_pair
from datetime import datetime, timedelta
from freqtrade.persistence import Trade
from pandas import DataFrame
import pandas
# --------------------------------


class Pump(IStrategy):
    """
    author@: igolaizola
    pumps with external buy signals using /force_buy
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
        dataframe.loc[
            (
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
            ),
            'sell'] = 1
        return dataframe
