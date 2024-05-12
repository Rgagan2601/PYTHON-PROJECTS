class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.create_pin()
        self.menu()

    def menu(self):
        user_input = input("""

                        Hello! How would like to proceed?
                        1.Enter 1 to create pin
                        2.Enter 2 to deposite
                        3.Enter 3 to withdraw
                        4.Enter 4 to check balance
                        5.Enter 5 to Exit() \t""")

        if user_input == '1':
            # print('Create pin')
            self.create_pin()
        elif user_input == '2':
            # print('deposite')
            self.deposite()
        elif user_input == '3':
            # print("withdraw")
            self.withdraw()
        elif user_input == '4':
            # print("check balance")
            self.check_balace()
        else:
            print("Byye")
            pass

    def create_pin(self):
        self.pin = input("Enter your pin : ")
        print("Pin set successfully")
        self.menu()

    def deposite(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            self.balance = self.balance + amount
            print("Deposite Successful"+ self.balance)
            self.menu()
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.pin:
            amount = int(input("Enter the amount : "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Operation successful")
                self.menu()
            else:
                print("paisa hi nahi hai ")
        else:
            print("Invlid pin!!")

    def check_balace(self):
        temp = input("Enter pin ")
        if temp == self.pin:
            print(self.balance)
            self.menu()
        else:
            print("Invalid pin!")


sbi = Atm()





