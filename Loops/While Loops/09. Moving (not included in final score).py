width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
command = input()

while command != "Done":
  num_of_boxes = int(command)
  free_space -= num_of_boxes

  if free_space <= 0:
     print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
     break

  command = input()
if command == "Done":
  print(f"{free_space} Cubic meters left.")
