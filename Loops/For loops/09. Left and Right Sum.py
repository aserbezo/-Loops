n = int(input())
# left side
left = 0
for i in range(0,n):
  current = int(input())
  left = left + current

# right side
right = 0
for i in range(0,n):
    current = int(input())
    right = right + current

if left == right:
    print(f"Yes, sum = {left}")
else:
    diff = abs(left - right)
    print(f"No, diff = {diff}")