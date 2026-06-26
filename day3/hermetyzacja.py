# hermetyzacja - ukrywanie pól
# enkapsulacja - hermetyzowanie pol i wystawianie metod do odczytu i zapisu

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # name mangling
        # ala private
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

if __name__ == '__main__':

    account = BankAccount("Radek", 2500)
    # print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?
    print(account.owner)
    #
    # account.__balance = 78000
    # print(account.__balance)  # 78000

    print(account.get_balance())  # 78000
    account.deposit(0)  # Invalid deposit amount
