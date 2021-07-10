from wallet import *
from coin import *
# from distribition import Distribution


def main():
    b = [Coin(1234), Coin(5), Coin(67), Coin(7261), Coin(1_000_001)]
    # b = [1_000_001, 1234, 5, 67, 7261]
    alice = Wallet(b)

    # c = Distribution(alice.get_coins()).distribution(False)
    alice.spend(50000, True)
    print(alice.get_coins())
    # print(a.spend(5))


if __name__ == '__main__':
    main()
