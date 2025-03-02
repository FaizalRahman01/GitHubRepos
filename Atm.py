pin = 1234 #Predefined ATM PIN
money = 1000000 #Initial account balance

print("\t\t\tWelcome to BOI (Bank Of India)")

while (True): # Infinite loop to keep ATM running until user exits
    exit= int(input("If You pull your Card Then You exit in the Atm machine\nPress 0 For exit\nif press 1 Then You Can Use Atm: "))

    if (exit == 0):# If user chooses to exit
        print("Thans For Visting Our Bank\nHave a Good Day ")
        break # Exit the loop
    elif (exit == 1):# If user chooses to continue
        Atm_pin = int(input("Please Enter Your Atm Pin:\n"))

        if (Atm_pin == pin):
            print("1. Deposit\n2. Withdraw\n3. Check Wallet\n4. Exit")
        else:
            print("Please RE-Check Your Pin")
            continue
        choice = int(input(""))
        if (choice == 1):
            print("Deposit")
            deposit = int(input("How Much Amount Do you Want to Deposit: "))
            money += deposit
            print("Now Available Balance Is: ₹", money)
        elif (choice == 2):
            print("Withdraw")
            withdraw = int(input("How Much Amount Do you Want to Withdraw: "))
            if (withdraw > money):
                print("Insufficient Balance")
            else:
                money -= withdraw
                print("Now Available Balance Is: ₹", money)
        elif choice == 3:
            print("Check Wallet\nNow Available Balance Is: ₹", money)
        elif choice == 4:
            break
        else:
            print("Invalid choice..! Please Enter 1 to 4 in int value")
    else:
        print("Invalid choice...!")

