def showBalance(balance):
    print("<---------------------------------------->")
    print(f"Your current balance is ${balance: .2f}")
    print("<---------------------------------------->")
def deposit():
    print("<---------------------------------------->")
    amount = float(input("Enter the amount to be deposited = "))
    print("<---------------------------------------->")
    if(amount < 0) :
        print("<---------------------------------------->")
        print("This an valid amount!")
        print("<---------------------------------------->")
        return 0
    else :
        return amount
    
def withdraw(balance):
    print("<---------------------------------------->")
    amount = float(input("Enter the amount to be withdrawn = "))
    if(amount > balance) :
        print("<---------------------------------------->")
        print("Insufficient funds!")
        print("<---------------------------------------->")
        return 0
    elif(amount < 0) : 
        print("<---------------------------------------->")
        print("This an valid amount!")
        print("<---------------------------------------->")
        return 0
    else :
        return amount
    
def main():
    balance = 0 
    isRunning = True 

    while isRunning : 
        print("<---------------------------------------->")
        print("Welcome to GNC Bank ! ")
        print("<---------------------------------------->")
        print("1. Show Balance")
        print("2. Deposit ")
        print("3. Withdrawl ")
        print("4. Exit ")
        print("<---------------------------------------->")

        choice = input("Enter your choice from 1-4 : ")

        if choice == '1':
            showBalance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            isRunning = False
        else : 
            print("<---------------------------------------->")
            print("Invalid choice")
            print("<---------------------------------------->")

    print("<---------------------------------------->")
    print("Thank you ! Have a nice day...") 
    print("<---------------------------------------->")

if __name__ == "__main__" :
    main()
