from secrets import token_hex
from functools import reduce
from . import coin as Coin


# @title Class Wallet
class Wallet:
    __coins = []
    # @dev 32 bytes hex address
    __address = "0x" + token_hex(32)

    # @constructor
    # @param Coin | Coin[] coin
    def __init__(self, coin):
        # @dev if user passes only Coin object
        if type(coin) == Coin:
            self.__coins.append(coin)

        # @dev if user passes an array of coins, unpacking array
        elif type(coin) == list or len(coin) > 1:
            self.__coins += coin

    def __repr__(self):
        return self.__coins

    # @returns Coins[] | int[] | float[]
    def get_coins(self):
        return self.__coins

    # @returns string
    def get_address(self):
        return self.__address

    # @param obj boolean
    # @returns number (sum of self.coins)
    def available(self, obj=False):
        if len(self.__coins) == 0:
            return 0

        # @dev if is Coins[]
        if obj:
            if len(self.__coins) == 1:
                return self.__coins[0].value

            else:
                total = 0
                for v in self.__coins:
                    total += v.value
                return total

        # @dev if is int[] | float[]
        else:
            if len(self.__coins) == 1:
                return self.__coins[0]

            else:
                total = reduce(lambda x, y: x + y, self.__coins)
                return total

    # @dev coin cannot be below zero
    # @param Coin[] | int[] | float[] coin
    def add(self, coin):
        if type(coin) == list:
            if len(coin) <= 0:
                raise Exception("[Error@Wallet.add]: No coins to be added")
            else:
                self.__coins += coin

        else:
            if coin <= 0:
                raise Exception("[Error@Wallet.add]: Can't be negative value!")

            else:
                if type(coin) == Coin:
                    self.__coins.append(coin)

                else:
                    self.__coins.append(Coin(coin))

    def spend(self, value, obj=False):
        total = value

        if self.available(obj) >= value:
            if obj:
                self.__coins.sort(key=lambda x: x.value)

                for v in self.__coins:
                    if v.value <= value:
                        print(v.value)
                        total -= v.value
                        self.__coins.pop(0)

                # self.__coins.sort(key=lambda x: x.value)
                # for v in self.__coins:
                #     if v.value <= value:
                #         total -= v.value
                #         self.__coins.remove(Coin(v.value))
                #
                # for v in self.__coins:
                #     if 0 < total <= v.value:
                #         self.__coins[0] = Coin(self.__coins[0] - total)

            else:
                temp_sorted = sorted(self.__coins)
                for v in temp_sorted:
                    if v <= value:
                        total -= v
                        self.__coins.remove(v)

                for v in self.__coins:
                    if 0 < total <= v:
                        self.__coins[0] -= total

        else:
            raise Exception("[Error@Wallet.spend]: You don't have enough balance!")
