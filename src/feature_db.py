#!/usr/bin/python

import json
from share_info import get_shares
from market_log import get_daily_prices
from price_detail import get_price_details
import my_util

def store_day_features(stock_no, date_str, row):
    pass

def get_day_features(stock_no, date_str):
    pass

def get_stock_features(stock_no, date_str):
    ashare = get_shares(stock_no, time_str)
    prices = get_daily_prices(stock_no, date_str, date_str)
    if not prices: 
        return []
    up_volume, down_volume = get_up_down_volume(stock_no, date_str, float(prices[0][0]))
    history_list = get_history_features(stock_no, date_str, 30)
    row = calc_day_features(ashare, prices[0], up_volume, down_volume, history_list)
    if row:
        store_day_features(stock_no, date_str, row)
    return row

def calc_day_features(ashare, price, up_v, down_v, history_list):
    if not price or not ashare: return []
    ashare = float(ashare)
    v_open, v_close, v_high, v_low, v_volume, v_turnover = [float(v) for v in price[1:]]

    features = []    

    #if arg_name == '1': # high - open
    features.append( v_high - v_open )
    #elif arg_name == '2': # high - low
    features.append( v_high - v_low )
    #elif arg_name == '3': # high - close
    features.append( v_high - v_close )
    #elif arg_name == '4': # open - low
    features.append( v_open - v_low )
    #elif arg_name == '5': # open - close
    features.append( v_open - v_close )
    #elif arg_name == '6': # low - close
    features.append( v_low - v_close )
    #elif arg_name == '7': # above_volume - last_above_volume
    features.append( v_low - v_close )
        #elif arg_name == '8': # above_volume - average_above_volume
        features.append( 0 )
        #elif arg_name == '9': # under_volume - last_under_volume
        features.append( 0 )
        #elif arg_name == '10': # under_volume - average_under_volume
        features.append( 0 )
        #elif arg_name == '11': # above_turnover - last_above_turnover
        features.append( 0 )
        #elif arg_name == '12': # above_turnover - average_above_turnover
        features.append( 0 )
        #elif arg_name == '13': # under_turnover - last_under_turnover
        features.append( 0 )
        #elif arg_name == '14': # under_turnover - average_under_turnover
        features.append( 0 )
    #elif arg_name == '15': # up_rate = (close - open) / open; down_rate = (open - close) / open
    features.append( (v_close - v_open) / v_open )
        #elif arg_name == '16': # up_rate / average_up_rate; down_rate / average_down_rate 
        features.append( 0 )
    #elif arg_name == '17': # up_amp_rate = (high - open) / open; down_amp_rage = (open - low) / open 
    features.append( (v_high - v_open) / v_open )
    features.append( (v_open - v_low) / v_open )
        #elif arg_name == '18': # up_amp_rate / average_up_amp_rage; down_amp_rage / average_down_amp_rate
        features.append( 0 )
        #elif arg_name == '19': # turnover_rate = volume / ashare; A = average_volume / average_turnover_rate; B = volume / turnover_rage; B / A
        features.append( 0 )
        #elif arg_name == '20': # A = average_turnover / (ashare * average_close); B = turnover / (ashare * close); B / A
        features.append( 0 )

    return features

def test():
    print get_stock_features(600000, '2014-11-12')

if __name__ == '__main__':
    test()
