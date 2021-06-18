import sys

max_number = -sys.maxsize
n = int(input())
sum = 0

for i in range(1, n + 1):
    number = int(input())
    sum += number
    if number > max_number:
        max_number = number
sum -= max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(sum - max_number)}")
