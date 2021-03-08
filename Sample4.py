# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:46:53 2021

@author: SushiMahi
"""

from blockchain import exchangerates

ticker = exchangerates.get_ticker()

print("BitCoin Prices in various currencies")


for k in ticker :
    print(k, ticker[k].p15min)
    
    
    

btc = exchangerates.to_btc('EUR', 100)

print("100 euros to bitcoin :" , btc)