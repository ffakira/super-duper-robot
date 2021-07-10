from math import log, floor


# @title Class Distribution
class Distribution:
    # @constructor
    # @param Coin | Coin[] coin
    def __init__(self, coins):
        self.__coins = coins

    # @dev Distribution of coins scale 1000.
    # @param Coin | int | float coin
    # @param obj boolean
    # @returns Coin[] | int[] | float[] | Exception
    def distribution(self, obj=False):
        if len(self.__coins) >= 1:
            # O(x^2) complexity -> appending values based of indices
            dist = lambda x: [[j for i, j in enumerate(x) if index(x)[i] == b] for b in range(max(index(x)) + 1)]

            # @dev used if is Coin[]
            if obj:
                # O(x) complexity -> finding the indices by using logarithmic
                index = lambda x: [floor(log(i.value, 1000)) for i in x]

            # @dev used if is primitive list float[] || int[]
            else:
                index = lambda x: [floor(log(i, 1000)) for i in x]

            return dist(self.__coins)

        else:
            raise Exception("[Distribution@Wallet.distribution]: No balance")
