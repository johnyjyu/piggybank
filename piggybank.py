__author__ = 'MD'
from blockchain.wallet import Wallet
import urllib
import json
import smtplib
import webbrowser

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


def pay(id, key):
    wallet = Wallet(id, key)
    add = wallet.list_addresses()
    newadd = add[0].address
    #q1 = "https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=" + newadd
    qr_api = 'https://blockchain.info/qr?data={}&size=300'
    qr_code = qr_api.format(newadd)
    webbrowser.open_new(qr_code)


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


#print getBTC(id1, key1)
#c = currentUSD(id1, key1)
#txt('piggybankbit', 'piggybank12345', 0000000000, id1, key1)
#pay(id1, key1)

