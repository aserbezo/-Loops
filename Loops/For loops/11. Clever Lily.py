lilly_age = int(input()) # age 21
machine_price = float(input()) # price 1570.98
single_toy_price = int(input()) # price 3
toy_count = 0
money_spend = 0
birthay_money = 9

for age in range(1 , lilly_age + 1):
    if age % 2 == 0:
        money_spend = money_spend + birthay_money
        birthay_money = birthay_money + 10
    else:
        toy_count = toy_count + 1
total_toys = toy_count * single_toy_price
final = money_spend + total_toys
if final >= machine_price:
    money_left = final - machine_price
    print(f"Yes! {money_left:.2f}")
else:
    money_need = machine_price - final
    print(f"No! {money_need:.2f}")