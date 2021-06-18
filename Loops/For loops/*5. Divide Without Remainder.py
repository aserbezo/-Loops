n = int(input())
group1 = 0
group2 = 0
group3 = 0
for i in range(0, n):
    number = int(input())
    if number % 2 == 0:
        group1 += 1
    if number % 3 == 0:
        group2 += 1
    if number % 4 == 0:
        group3 += 1

percent1 = (group1 / n) * 100
percent2 = (group2 / n) * 100
percent3 = (group3 / n) * 100

print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")