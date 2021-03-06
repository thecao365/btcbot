import threading
from depth import trade
import logging
log = logging.getLogger(__name__)


class ExAPI(object):
    curdepth = {}
    name = ''

    def __init__(self, refresh_rate=0.0):
        self.refresh_rate = refresh_rate
        self.refresh_lock = threading.Lock()
        self.last_update = 0.0
        self.last_depth = None
        self.depth = None
        self.balance_bid = 0.0
        self.balance_ask = 0.0

    def execute(self, order, pair):
        if order.typ == trade.BID:
            order_type = "buy"
        elif order.typ == trade.ASK:
            order_type = "sell"

        self.add_order(order=order_type,
                       price=order.value,
                       vol=order.volume,
                       pair=pair)
        log.debug("[%s] %s vol=%f val=%f",
                  self.name, order_type, order.volume, order.value)
        print("[%s] %s vol=%f val=%f" %
              (self.name, order_type, order.volume, order.value))

    def update_balance(self):
        self.balance = self.get_balance()
        self.balance_bid = self.balance['btc']
        self.balance_ask = self.balance['eur']

    #def cipher_key(self, dummy=None):
    #    pass

    #def decipher_key(self, dummy=None):
    #    pass

    #def get_balance(self, dummy=None):
    #    pass

    #def add_order(self, order, price, vol):
    #    pass

    #def get_trades(self, **kwargs):
    #    pass

    def get_min_bid(self):
        return self.current_depth[-1][0].get_min_bid()

    def get_fees(self, **kwargs):
        pass

    def get_max_ask(self):
        return self.current_depth[-1][0].get_max_ask()

    #def depth(self, **kwargs):
    #    pass
