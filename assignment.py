Balance = 1000
print("Welcome to the ATM")
print("Your balance is: ", Balance)

while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")

    choose = int(input("Choose one of these four options: "))
    if choose == 1:
        print(Balance)
    elif choose == 2:
        cash = int(input("Enter the amount of deposit: "))
        Balance = Balance + cash
        print("Deposit successful. New balance is: ", Balance)
    elif choose == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw >= Balance:
            print("Insufficient funds!")
        elif withdraw < Balance:
            Balance = Balance - withdraw 
            print("Withdrawal successful. New balance = ", Balance)
    else:
        print("Goodbye!")




        

