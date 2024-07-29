balance = 1000

#adding to the balance

choice = int(input("How much do you want to add to the balance"))

if choice <= 0:
    print("invalid amount")
else:
    balance += choice
    #balance = balance + choice
    print(f'Your new balance is now: ${balance}')

#withdrawing from the balance
    
choice = int(input('How much do you want to withdraw from the balance'))

if choice <= 0 or choice > balance:
    print('invalid amount or insufficient balance')

else:
    balance -= choice
    #balance = balance - choice
    print(f'Your new balance is now: ${balance}')

#checking the balance

print(f'Your current balance is: ${balance}')
