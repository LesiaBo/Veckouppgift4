import inputFromUser as modul
#1:
#Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
#my_function("David") → "David är en riktig hacker"
print(f"Hello {modul.user_name()}, you are cool in programming!")

#2a:
#Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen,
# och skriva ut resultatet. Exempel: eko("hej") → skriver ut "hejhej"

word_to_repeat = input("What should I repeat for you? ")
modul.eko(word_to_repeat)

#2b: Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"
word_to_repeat = input("What should I repeat for you? ")
count = input("How many times should I repeat it? ")
modul.eko(word_to_repeat, count)

#3 Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
#end = 5
#y = 1
#for x in range(1, 100):
#    y *= 2
#    # avsluta loopen med en if-sats här
#print(y)
modul.exponentiering()

#4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
#last([1, 2, 3]) → 3
modul.last([1, 2, 3])

#5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera
# en ny lista, där den har tagit bort första och sista elementet.
#cut_edges([1, 2, 3, 4]) → [2, 3]
modul.cut_edges([1, 2, 3, 4])

#6 Lös felen i koden.
#def increase(x):
#    return x
#    x += 1

print(modul.increase(201))


#7 Bygg en funktion med namnet average. Den ska ta parametrar: x och y.
# Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel
# så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.
#Tips: det kan vara enklare att använda fler variabler.
print(modul.average(4, 8))

#8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
#pretty_print(["a", "b", 3.14])
#listan har 3 element:
#1. a
#2. b
#3. 3.14
modul.pretty_print(["a", "b", 3.14])


