number = input()
simple_number = 0
not_simple = 0

while number != 'stop':
    num = int(number)
    if num < 0:
        print(f'Number is negative.')
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
               count += 1
        if count == 2 or num == 1:
            simple_number += num
        else:
            not_simple += num
    number = input()
print(f'Sum of all prime numbers is: {simple_number}')
print(f'Sum of all non prime numbers is: {not_simple}')