needed_steps= 10000
steps_counter = 0
steps = 0
while steps_counter < needed_steps:
    command = input()
    if command == 'Going home':
        steps = int(input())
        steps_counter += steps
        if steps_counter < needed_steps:
            print(f'{needed_steps - steps_counter} more steps to reach goal.')
        break
    steps = int(command)
    steps_counter += steps
    if steps_counter >= needed_steps:
        break
if steps_counter >= needed_steps:
    print('Goal reached! Good job!')
    print(f'{steps_counter - needed_steps} steps over the goal!')