class AccountException(Exception):
    pass


class BankAccount():
    latestAccountNumber = 0

    def __init__(self, balance):
        self.__accountNumber = BankAccount.latestAccountNumber
        self.__accountBalance = balance
        BankAccount.latestAccountNumber += 1

    @property
    def accountBalance(self):
        return self.__accountBalance

    @accountBalance.setter
    def accountBalance(self, amount):
        if amount < 0:
            raise AccountException('Balance cant be negative')
        else:
            if abs(amount-self.__accountNumber) > 100000:
                print("Very big operation of ", amount-self.__accountBalance)
            self.__accountBalance = amount

    @property
    def accountNumber(self):
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self, number):
        raise AccountException('You caant change account number')

    @accountNumber.deleter
    def accountNumber(self):
        if self.accountBalance != 0:
            raise AccountException('You cant delete account with positive balance')
        else:
            del self


firstAccount = BankAccount(1000)
try:
    firstAccount.accountBalance -= 1200
except AccountException as E:
    print(E)
try:
    firstAccount.accountNumber = 17
except AccountException as E:
    print(E)
try:
    firstAccount.accountBalance += 1000000
except AccountException as E:
    print(E)
try:
    del firstAccount.accountNumber
except AccountException as E:
    print(E)

