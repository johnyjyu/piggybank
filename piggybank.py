__author__ = 'MD'
from blockchain.wallet import Wallet
import urllib
import json
import smtplib
import webbrowser
import datetime
import multiprocessing
import hashlib


def passGen(password):
    passkey = hashlib.sha512(password).hexdigest()
    return passkey

def mkWallet(password):
    from blockchain import  createwallet
    wallet = createwallet.create_wallet(password, 'api', label = 'piggybank')

def getBTC(id, key):
    wallet = Wallet(id, key)
    sbtc = 100000000
    bal = float(wallet.get_balance())
    btc = bal/sbtc
    return btc


def currentUSD(id, key):
    b = getBTC(id, key)
    ticker = "https://btc-e.com/api/2/btc_usd/ticker"
    data = urllib.urlopen(ticker)
    jdata = json.loads(data.read())
    usdVal = jdata['ticker']['sell']
    return usdVal*b


def pay(id, key):
    wallet = Wallet(id, key)
    add = wallet.list_addresses()
    newadd = add[0].address
    qr_api = 'https://blockchain.info/qr?data={}&size=300'
    qr_code = qr_api.format(newadd)
    webbrowser.open_new(qr_code)


def txt(user, password, number, id, key):
    user = user + '@gmail.com'
    number = str(number) + '@tmomail.net'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    #sending the id
    server.sendmail(user, number, str(id))
    #sending the key
    server.sendmail(user, number, str(key))
    server.quit()


def timer(user, password, number, id, key):
    now = datetime.datetime.now()
    now = now.second
    nextmin = now + 5
    while True:
        if datetime.datetime.now().second == nextmin:
            txt(user, password, number, id, key)
            break


def inittimer(user, password, number, id, key):
    process = multiprocessing.Process(target=timer(user, password, number, id, key))
    process.start()
    return
if __name__ == '__main__':
    '''
desert cross town crackdown neuroscience cedar dui mozart campion unkempt customizable imperceptibly havoc jerseys grahams hofstra corporately crawling cultivates darnell
    '''





