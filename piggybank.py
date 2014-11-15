__author__ = 'MD'
from blockchain.wallet import Wallet
import urllib
import json

def getBTC(id,key):
    wallet = Wallet(id, key)
    sbtc = 100000000
    bal = float(wallet.get_balance())
    btc = bal/sbtc
    return btc


def currentUSD(id,key):
    b = getBTC(id,key)
    ticker = "https://btc-e.com/api/2/btc_usd/ticker"
    data = urllib.urlopen(ticker)
    jdata = json.loads(data.read())
    usdVal = jdata['ticker']['sell']
    return usdVal*b

phrase = '''
desert cross town crackdown neuroscience cedar dui mozart campion unkempt customizable imperceptibly havoc jerseys grahams hofstra corporately crawling cultivates darnell
'''
id1 = '33d99a82-2463-458f-96b5-20fbf0ec36dc'
key1 = 'piggybank123456789'


print getBTC(id1, key1)
print currentUSD(id1, key1)
