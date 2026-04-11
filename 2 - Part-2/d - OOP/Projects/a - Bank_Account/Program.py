from Account import Account

print("Initializing your bank account.")

titular = input("Type your name: ")

account = Account(titular)

print("Hello,", account.name + ". Type the amount to deposit:")
Account.deposit(account, float(input()))
print("Your balance, after the deposit, is: $ %.2f" % account.balance)
print()

# 1 -> deposit | 2 -> withdraw | 0 -> getOut
action = 1
while action != 0:
    print(f"Type the operation you want to do: \n1 deposit \n2 withdraw \n0 get out of your account.")
    action = int(input())

    if action == 1:
        print("Ok! Now, tyoe the amount you want to deposit: ")
        deposit = float(input())
        account.deposit(deposit)
        print("Your balance, after the deposit, is: $ %.2f" % account.balance)
        print()

    elif action == 2:
        print("Ok! Now, type the amount you want to withdraw:")
        withdraw = float(input())
        account.withdraw(withdraw)
        print("Your balance, after the withdraw, is: $ %.2f" % account.balance)
        print()

    elif action == 0:
        break

    else:
        print(f"This operation does not exist.")
        print(f"Please, type 1 to deposit, 2 to withdraw or 3 to get out of your account.\n")

print("Your balance, after all the operations, is $ %.2f" % account.balance)
print("Thanks for using your bank account!")