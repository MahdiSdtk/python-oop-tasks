class Bank:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.bank = []
        return cls._instance
    
    _accounts = [] # store the accounts

    # model
    class BankAccount:
        def __init__(self, accNumber, ownerName, password, balance):
            self.accNumber = accNumber
            self._ownerName = ownerName
            self._password = password
            self._balance = balance

        def withdraw(self, amount):
            if self._balance > amount:
                self._balance -= amount
                return True
            return False

        def deposit(self, amount):
            self._balance += amount
        
    class BankTemplate:
        def printBalance(accNumber, password):
            for i in Bank._accounts:
                if accNumber == i.accNumber and password == i._password:
                    print(f'Account number: {i.accNumber}\nAccount Owner: {i._ownerName}\nBalance: {i._balance}')
        
        def errorMsg():
            print('account not found.')

    class BankFuncs:

        def __init__(self, template):
            self.template = template

        def createAccount(self, accNumber, ownerName, password, balance):
            account = Bank.BankAccount(accNumber, ownerName, password, balance)
            Bank._accounts.append(account)
            print('account created successfully.')

        def deleteAccount(self, accNumber, password):
            for i in Bank._accounts:
                if accNumber == i.accNumber and password == i._password:
                    Bank._accounts.remove(i)
                    print('account closed successfully.')

        def updateInfo(self, accNumbInp, accPasswordInp, accNumber: int = None, ownerName=None, password=None):
            for i in Bank._accounts:
                if accNumbInp == i.accNumber and accPasswordInp == i._password:
                    if accNumber: i.accNumber = accNumber
                    if ownerName: i._ownerName = ownerName
                    if password: i._password = password
                    if not accNumber and not ownerName and not password: print('there is nothing to edit.')
                else: Bank.BankTemplate.errorMsg()
        
        def withdraw(self, accNumber, password, amount):
            for i in Bank._accounts:
                if accNumber == i.accNumber and password == i._password:
                    i.withdraw(amount)
                    print('withdraw, successful.')
        
        def deposit(self, accNumber, password, amount):
            for i in Bank._accounts:
                if accNumber == i.accNumber and password == i._password:
                    i.deposit(amount)
                    print('deposit, successful.')

        def getBalance(self, accNumber, password):
            """ print the balance of the account with account number and password. """
            for i in Bank._accounts:
                if accNumber == i.accNumber and password == i._password:
                    Bank.BankTemplate.printBalance(accNumber, password)


template = Bank.BankTemplate
atm = Bank.BankFuncs(template)


atm.createAccount(123, 'matak', 'mowl', 255)
atm.getBalance(123, 'mowl')
atm.updateInfo(123, 'mowl', ownerName='nato')
atm.withdraw(123, 'mowl', 200)
atm.deposit(123, 'mowl', 50)
atm.getBalance(123, 'mowl')

print(Bank._accounts)
