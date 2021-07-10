# @title Class Coin
class Coin:
    value = None

    # @constructor
    # @param int | float value
    def __init__(self, value):
        # @dev Checks the value is int || float || greater than 0
        if value > 0:
            if type(value) == int or type(value) == float:
                # @dev u256 type
                if value > (2**256 - 1):
                    raise Exception("[Error@Coin.__init__]: Math overflow")
                else:
                    self.value = value
        else:
            raise Exception("[Error@Coin.__init__]: Invalid value")
