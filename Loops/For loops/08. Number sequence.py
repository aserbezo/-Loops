import sys

max_num = - sys.maxsize
min_num = sys.maxsize
number = int(input())
for i in range(0,number):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")