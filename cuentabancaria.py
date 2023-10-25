#Creación de la clase y de sus variables
class Bank_Account:
    
    def __init__ (self, account_number, Balance=1500): 
        self.account_number = account_number
        self.balance = Balance
    
    def get_account_number(self):
        return self.account_number
    
    def deposit(self, amount):
        self.balance += amount

    def extract(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuficient founds")

    def get_balance(self):
        return self.balance


def main():
    account_number = input("Enter your account number: ")
    account = Bank_Account(account_number)

    while True:
        print("\n1. Deposit\n2. Extract\n3. Check Balance\n4. Quit")
        awnser = input("\n Enter your awnser : ")
        
        if awnser == "1":
            amount = float(input("Enter the amount you want to deposit: "))
            account.deposit(amount)
        elif awnser == "2":
            amount = float(input("Enter the amount you want to withdraw: "))
            account.extract(amount)
        elif awnser == "3":
            print("Current balance:", account.get_balance())
        elif awnser == "4":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid awnser. Please try again.")


if __name__ == "__main__":
    main()
main()