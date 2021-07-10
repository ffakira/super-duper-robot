from wallet import Wallet
# from coin import *
# from distribition import Distribution
from reservation_handle import ReservationHandle


def main() -> None:
    print("0x")

    # b = [Coin(1234), Coin(5), Coin(67), Coin(7261), Coin(1_000_001)]
    b = [1_000_001, 1234, 5, 67, 7261]
    alice = Wallet(b)

    rh = ReservationHandle()
    rh.reserve([100, 200, 300], alice)

    # c = Distribution(alice.get_coins()).distribution()
    # print(c)
    # alice.spend(50000)
    # print(alice.get_coins())
    # print(a.spend(5))


if __name__ == '__main__':
    main()
