"""
En este programa, creamos un modelo de asistencia bancaria en el que tras iniciar sesión contu número de cuenta, te da la opción de ver tu balance, introducir/sacar dinero y cerrar la consola
"""



#Creamos la clase Bank_Account

class Bank_Account:
    



    #Utilizamos el comando __init__ para definir las variables account number y el balance = 1500

    def __init__ (self, account_number, Balance=1500): 
        self.account_number = account_number
        self.balance = Balance
    


    #Damos en número de cuenta
    def get_account_number(self):
        return self.account_number
    


    #Creamos los comandos para la extracciión e intoducción de dinero

    def deposit(self, amount):
        self.balance += amount

    def extract(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuficient founds")


            
    #Devolvemos el balance según los trámites realizados
    def get_balance(self):
        return self.balance
    


#Creamos una función y sus variables

def main():
    account_number = input("Enter your account number: ")
    account = Bank_Account(account_number)



    #Creamos un bucle para reproducir una consola y las opciones de la consola
    while True:
        print("\n1. Deposit\n2. Extract\n3. Check Balance\n4. Quit")
        awnser = input("\n Enter your awnser : ")
        


        #Según las respuesta dada, se realiza la operación

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



        #Manejo de errores al introducir un número/caracter inválido
        else:
            print("Invalid awnser. Please try again.")



#Manejo de errores de repetición
if __name__ == "__main__":
    main()
main()