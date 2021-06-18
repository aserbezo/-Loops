import sys
max_num = -sys.maxsize

num = input()

while num != "Stop":
    num = int(num)
    if num > max_num:
        max_num = num
    num = input()

print(max_num)