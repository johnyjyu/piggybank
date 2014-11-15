__author__ = 'MD'
import piggybank

if __name__ == '__main__':
    piggybank.init()
    w2id = piggybank.mkWallet()
    piggybank.printu()
    print piggybank.userData(w2id)
    id = raw_input("id: ")
    number = raw_input("tmo number: ")
    key = piggybank.userData(id)
    while True:
        inputx = raw_input(">>> ")
        if inputx == 'pay':
            piggybank.pay(id, key)
        elif inputx == 'btc':
            print piggybank.getBTC(id, key)
        elif inputx == 'usd':
            print piggybank.currentUSD(id, key)
        elif inputx == 'txt':
            piggybank.inittimer('piggybankbit', 'piggybank12345', number, id, key)
        else:
            print " wrong input"