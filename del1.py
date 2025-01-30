#1a: test
def foo(t):
    print("test")

foo("hej")

#1b: 3, 5
def fun1(x, y):
    return x * y

print(3, 5)

#1c: 15
def fun2(x, y):
    return x * y

print(fun2(3, 5))

#1d:5*(5*2 + 5*3) = 125
def fun3(i):
    return 5 * i

x = 2
y = 3
a = fun3(fun3(x) + fun3(y))
print(a)


#1e: 5+2 = 7
a = 5
def fun4(a):
    a += 1

a += 2
print(a)

#1f: goo(foo, 3) = 2*3*3 = 18
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

#1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
#is_number sayer True om parameter x är int eller float, annars sayer det False
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False


print(is_number(5.5))
print(is_number(42))

#1h: [how's, going, coding]
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    print(found)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

#1i En uppgift i tre delar:
#Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
#->Hitta det minsta värdet mellan de angivna.
#Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
#->-11,
#->
#100
#Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = float('inf')
    if numbers:
        for item in numbers:
            if item < counter:
                counter = item
        print(f"The smallest item is: {counter}")
        return counter
    else:
        print("List of numbers is empty")
        return

find_min([10, 3, -4, -11])
find_min([])
find_min([100])