__author__ = 'MD'
import piggybank

if __name__ == '__main__':
    dict = {'33d99a82-2463-458f-96b5-20fbf0ec36dc': 'piggybank123456789'};
    if __name__ == '__main__':
        id = raw_input("id: ")
        number = raw_input("tmo number: ")
        key = dict[id]
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