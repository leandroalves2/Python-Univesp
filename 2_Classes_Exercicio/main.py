from Bank_Account import Bank_Account

number = int(input("Entre o número da conta: "))
owner = input("Entre o titular da conta: ")
d = input("Will there be an initial deposit (y/n)? ")

if d == 'y' or d == 'Y':
    balance = float(input("Enter the initial deposit amount: $"))
    cont = Bank_Account(number, owner, balance)
else:
    balance = 0.0
    cont = Bank_Account(number, owner, balance)

print("")
print("Account information: ")
print(cont)
print("")

exit = 'y'
while exit != 'n' and exit != 'N':
    d = input("Deposit or Withdrawal (d/w)? ")
    if d == 'd' or d == 'D':
        deposit = float(input("Enter a value for deposit: $"))
        cont.Deposit(deposit)
        print("Account information updated:")
        print(cont)
    if d == 'w' or d == 'W':
        cashout = float(input("Enter a value for withdrawal: "))
        cont.Cashout(cashout)
        print("Account information updated:")
        print(cont)
    print("")
    exit = input("Do you wish to continue (y/n)? ")

print("")
print("PROGRAMA FINALIZADO")