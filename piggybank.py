__author__ = 'MD'
from blockchain.wallet import Wallet
import urllib
import json
import smtplib

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

def txt(user, password, number, id, key):
    b = getBTC(id, key)
    user = user + '@gmail.com'
    number = str(number) + '@tmomail.net'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.sendmail(user, number, str(b))


phrase = '''
desert cross town crackdown neuroscience cedar dui mozart campion unkempt customizable imperceptibly havoc jerseys grahams hofstra corporately crawling cultivates darnell
'''
id1 = '33d99a82-2463-458f-96b5-20fbf0ec36dc'
key1 = 'piggybank123456789'


print getBTC(id1, key1)
c = currentUSD(id1, key1)
txt('piggybankbit', 'piggybank12345', 3479937771, id1, key1)