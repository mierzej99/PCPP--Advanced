class AccountException(Exception):
    pass


class BankAccount():
    latestAccountNumber = 0

    def __init__(self):
        self.__accountNumber = BankAccount.latestAccountNumber
        self.accountBalance = 0
        BankAccount.latestAccountNumber += 1

    @property
    def accountNumber(self):
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self):
        raise AccountException

    @accountNumber.deleter
    def accountNumber(self):
        if self.balance != 0:
            raise AccountException
