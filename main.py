# Author: silvermpx

import tkinter as tk
import logging
from connectors.binance_futures import BinanceFuturesClient



logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("0e50e09d849493d9142089cab8681deaeff1c25d419ba39be93c121e33534058",
                                   "13b7943deef385b334c6304579dec0b4ec33213ab6739e352f46e1629b65b9a9",True)
    print(binance.get_historical_candles("BTCUSDT", "1h"))


    root = tk.Tk()
    root.mainloop()
