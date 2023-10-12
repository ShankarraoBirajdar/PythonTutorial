

class Atm:

    def __init__(self):
        self.pin: str = ''
        self.balance: float = 0
        self.menu()

    def menu(self):
        while True:
            user_input: str = input("""
                  Welcome To The Digital Bank
                  1.Enter 1 to create a pin
                  2.Enter 2 to deposit
                  3.Enter 3 to withdraw
                  4.Enter 4 to check the balance
                  5.Enter 5 to exit
                  """)
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            else:
                print('Bye')
                break

    def create_pin(self):
        self.pin =input('Enter the pin\n')
        print('pin set successfully')

    def deposit(self):
        temp = input('Enter the pin\n')
        if temp == self.pin:
            amount: float = float(input('Enter the deposit Amount\n'))
            self.balance += amount
            print('Deposit Successful')
        else:
            print('invalid pin, Please Try Again')

    def withdraw(self):
        temp = input('Enter the pin\n')
        if temp == self.pin:
            amount: float = float(input('Enter the withdraw Amount\n'))
            if amount<self.balance:
                self.balance-=amount
                print('operation successful')
            else:
                print('insufficient fund')

        else:
            print('invalid pin, Please Try Again')

    def check_balance(self):
        temp = input('Enter the pin\n')
        if temp == self.pin:
            print('Available Balance is: ',self.balance)
        else:
            print('invalid pin, Please Try Again')

