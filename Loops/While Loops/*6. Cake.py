width = int(input())
length = int(input())

cake_size = width * length

while cake_size > 0:
      line = input()
      # lene e text но може да го кастнем с int за да може да изчислим
      if line == "STOP":
          print(f"{cake_size} pieces are left.")
          break
      else:
          pieces = int(line)
          cake_size -= pieces

if cake_size <= 0:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
