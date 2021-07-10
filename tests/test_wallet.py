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
# ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐         tests/test_wallet.py -> src/wallet.py
# ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
# ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
# ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
# ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
# ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
# ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
# ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
# ▒▒▒▒▒▒▒▒▒▒▀▀

import unittest
from src.wallet import Wallet
from src.coin import Coin


class WalletTestCase(unittest.TestCase):
    def test_wallet_instantiate_int(self):
        print("Expect value to be [1, 2, 3, 4]")
        w = Wallet([1, 2, 3, 4])
        self.assertEqual(w.get_coins(), [1, 2, 3, 4])

    def test_wallet_instantiate_obj(self):
        print("Expect value to compare two exact list objects [Coin(10), Coin(27), Coin(871), Coin(999)]")
        w = Wallet([Coin(10), Coin(27), Coin(871), Coin(999)])
        w2 = Wallet([Coin(10), Coin(27), Coin(871), Coin(999)])
        self.assertListEqual(w.get_coins(), w2.get_coins())


if __name__ == '__main__':
    unittest.main()
