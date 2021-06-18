import sys
n = int(input())

even, odd = (-sys.maxsize, -sys.maxsize)
odd_min, even_min = (sys.maxsize, sys.maxsize)
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        sum_even += num
        if num > even:
            even = num
        if num < even_min:
            even_min = num

    else:
        sum_odd += num
        if num > odd:
            odd = num
        if num < odd_min:
            odd_min = num

print(f'OddSum={sum_odd:.2f},')

if odd_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')

if odd == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd:.2f},')

print(f'EvenSum={sum_even:.2f},')

if even_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even:.2f}')