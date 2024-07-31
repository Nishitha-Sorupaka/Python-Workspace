#atmexceptions.py

class DepositError(Exception):pass
class WithDrawError(BaseException):pass
class InsufficientFundError(Exception):pass