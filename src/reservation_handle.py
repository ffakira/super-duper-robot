from functools import reduce
from wallet import Wallet


# @title Class ReservationHandle
class ReservationHandle:
    # @constructor
    # @param boolean obj
    def __init__(self, obj=False):
        self.__obj = obj

        # @dev handles all addresses
        self.__handle_list = {}

    # @param Coins[] | int[] | float amount
    # @param Wallet wallet
    def reserve(self, amount, wallet: Wallet) -> None or Exception:
        total = None

        if type(amount) == list:
            total = reduce(lambda x, y: x + y, amount)
        else:
            total = amount

        if total <= wallet.available():
            try:
                # @dev if the address exist
                if self.__handle_list[wallet.get_address()]["amount"] > 0:
                    self.__handle_list[wallet.get_address()]["total"] += total
                    self.__handle_list[wallet.get_address()]["amount"] += amount

                # @dev if the address does not exist
                else:
                    self.__handle_list["wallet.get_address()"] = {
                        "total_reserve": total,
                        "coins_reserve": amount
                    }

            except KeyError:
                raise Exception("[Error@ReservationHandle.reserve]: Invalid key address")

        else:
            raise Exception("[Error@ReservationHandle.reserve]: Not enough balance")

    def reservation_spend(self, amount, wallet: Wallet) -> None:
        pass

    # @dev Will delete the reserve back to None and transfer back to wallet instance
    # @param Wallet wallet
    def reservation_cancel(self, wallet: Wallet) -> None:
        try:
            wallet.add(self.__handle_list[wallet.get_address()]["coins_reserve"])
            del self.__handle_list[wallet.get_address()]

        except KeyError:
            raise Exception("[Error@ReservationHandle.reserve]: Invalid key address")
