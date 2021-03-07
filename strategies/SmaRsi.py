# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import datetime

# --------------------------------


class SmaRsi(IStrategy):
    """

    author@: Iñigo Garcia Olaizola

    """

    # ROI table:
    minimal_roi = {
        "0": 0.15,
        "35": 0.04,
        "65": 0.01,
        "115": 0
    }

    # Optimal timeframe for the strategy
    timeframe = '5m'

    startup_candle_count = 1500
    
    stoploss = -0.15
    use_custom_stoploss = True

    def custom_stoploss(self, pair: str, trade: 'Trade', current_time: datetime,
                        current_rate: float, current_profit: float, **kwargs) -> float:

        diff = current_time - trade.open_date
        secs = diff.days * 3600 + diff.seconds
        limit = 75 * 60
        if secs > limit:
            return -0.01
        stop = (-0.14 * (limit - secs)/limit) - 0.01
        return stop

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        dataframe['smaShort'] = ta.SMA(dataframe, timeperiod=144)
        dataframe['smaLong'] = ta.SMA(dataframe, timeperiod=2016)

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                    ((dataframe['rsi'] < 21) & (dataframe['smaShort'] > dataframe['smaLong']))
                    |
                    ((dataframe['rsi'] < 9) & (dataframe['smaShort'] <= dataframe['smaLong']))
            ),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                    (dataframe['rsi'] > 70)
            ),
            'sell'] = 1
        return dataframe
