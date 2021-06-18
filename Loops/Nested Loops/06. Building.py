floors = int(input())
rooms = int(input())
for flour in range(floors,0,-1):
    for room in range(0, rooms):
        if flour == floors:
            print(f"L{flour}{room} ", end="")
        elif flour % 2 == 0:
            print(f'O{flour}{room}', end=' ')
        else:
            print(f'A{flour}{room}', end=' ')

    print()