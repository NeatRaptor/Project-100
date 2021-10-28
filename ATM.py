class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is 1000")

    def withdrawl(self, amount):
        newAmount = 1000 - amount
        print("you have withdrawn amount "+str(amount) + " and your remaining balance is " + str(newAmount))


def main():
    cardNumber = input("Insert your card number: ")
    pinNumber = input("Enter your pin number: ")
    newUser = Atm(cardNumber, pinNumber)
    print("Choose your activity ")
    print("1.Balance Enquiry   2.Withdrawal")
    activity = int(input("enter activity number: "))

    if (activity==1):
        newUser.checkBalance()
    elif (activity==2):
        amount = int(input("enter the amount: "))
        newUser.withdrawl(amount)
    else:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()