account = 0.0
amount = input() # "50.56"
while amount != "NoMoreMoney":
    amount = float(amount)

    if amount < 0:
        print("Invalid operation!")
        break

    account += amount

    print(f"Increase: {amount:.2f}")
    amount = input()
print(f"Total: {account:.2f}")