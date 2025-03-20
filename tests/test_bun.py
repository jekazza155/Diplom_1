from data import Data
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        assert bun.get_name() == Data.BLACK_BUN

    def test_get_price(self):
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        assert bun.get_price() == Data.BLACK_BUN_PRICE