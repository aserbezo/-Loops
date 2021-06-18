first_row = int(input())
last_row = int(input())
magic = int(input())
count = 0
is_found = False
for i in range(first_row , last_row + 1):
    for j in range(first_row, last_row + 1):
        count += 1
        if i + j == magic:
            print(f"Combination N:{count} ({i} + {j} = {magic})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{count} combinations - neither equals {magic}")
