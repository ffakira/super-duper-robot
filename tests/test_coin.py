# ▄              ▄
# ▌▒█           ▄▀▒▌
# ▌▒▒█        ▄▀▒▒▒▐
# ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
# ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
# ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
# ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌            such test
# ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐            pls dont fail
# ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌          wow much passes
# ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌          ¯\_(ツ)_/¯
# ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐         tests/test_coin.py -> src/coin.py
# ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
# ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
# ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
# ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
# ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
# ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
# ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
# ▒▒▒▒▒▒▒▒▒▒▀▀

import unittest
from src import coin


class CoinTestCase(unittest.TestCase):
    def test_coin_instantiate(self):
        print("Expect value to be 10")
        c = coin.Coin(10)
        self.assertEqual(c.value, 10)

    def test_coin_negative(self):
        print("Expect to throw an Exception for negative int")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin(-10)
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_invalid_string(self):
        print("Expect to throw an Exception for strings")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin("abcd")
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_invalid_char(self):
        print("Except to throw an Exception for char")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin('a')
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_float_instantiate(self):
        print("Expect value to be 1.27")
        c = coin.Coin(1.27)
        self.assertEqual(c.value, 1.27)

    def test_coin_float_neg_instantiate(self):
        print("Expect to throw an Exception for negative float")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin(-8.11)
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_none_instantiate(self):
        print("Expect to throw an Exception for None value")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin(None)
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_zero_value(self):
        print("Expect to throw an Exception for zero")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin(0)
            self.assertTrue("[Error@Coin.__init__]: Invalid value" in ctx.exception)

    def test_coin_max_value_overflow(self):
        print("Expect to throw an Exception for max int overflow")
        with self.assertRaises(Exception) as ctx:
            c = coin.Coin(222**256)
            self.assertTrue("[Error@Coin.__init__]: Math overflow" in ctx.exception)


if __name__ == '__main__':
    unittest.main()
