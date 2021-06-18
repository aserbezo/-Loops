#number_a = ord("a")
#number_A = ord("A")
#number_1 = ord("1")

#print(number_a)
#print(number_A)
#print(number_1)
# ord() => приема символ и връща число на стойността му в ASCII

n = int(input())
l = int(input())
for first_char in range(1, n + 1):
    for second_char in range(1, n + 1):
        for third_char in range(ord("a"), ord("a") + l):
            for fourth_char in range(ord("a"), ord("a") + l):
                for fifth_char in range(1, n + 1):
                    if first_char < fifth_char and second_char < fifth_char:
                        print(f"{first_char}{second_char}{chr(third_char)}{chr(fourth_char)}{fifth_char}",end=" ")
