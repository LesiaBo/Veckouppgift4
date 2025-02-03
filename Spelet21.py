import random
def next_after_21():
    sum = 0
    i = 1
    j = 1
    while sum <= 21:
        sum += i
        j = i
        i += 1
    print(f"The number which made amount more than 21 is: {j} and amount is: {sum}")

def next_after_21_with_random_numbers():
    sum = 0
    i = 1
    j = 1
    while sum <= 21:
        i = random.randint(1, 13)
        sum += i
        print(i, sum)
        j = i
        i += 1
    print(f"The number which made amount more than 21 is: {j} and amount is: {sum}")

next_after_21()
next_after_21_with_random_numbers()
