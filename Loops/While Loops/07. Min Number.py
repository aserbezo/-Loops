import sys
min_num = sys.maxsize

num = input()

while num != "Stop":
    num = int(num)
    if num < min_num:
        min_num = num
    num = input()

print(min_num)