def user_name():
    return input("What is your name? ")

def eko(users_data, count = None):
    result = ""
    if count:
        try:
            count_int = int(count)
            for i in range(count_int):
                result += users_data
        except ValueError:
            print("Please, provide count in integer format")
    else:
        result = users_data + users_data
    print (result)

def exponentiering():
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        # avsluta loopen med en if-sats här
        if x == end:
            break
    print(y)

def last(my_list):
    last_element= my_list[-1]
    print(last_element)
    return last_element

def cut_edges(my_list):
    #my_list.pop(0)
    #my_list.pop(-1)
    #print(my_list)
    new_list = my_list[1:-1]
    print(new_list)

def increase(x):
    x += 1
    return x

def average(x, y):
    result = (x + y)/2
    return result

def pretty_print(my_list):
    list_len = len(my_list)
    if list_len == 0:
        print("Your list is empty")
    else:
        print(f"You list has {list_len} elements:")
        for i in range(list_len):
            print(f"{i}: {my_list[i]}")



