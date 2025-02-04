#Python har ett paket med inbyggda, enkla funktioner för grafik: turtle.
# Tänk dig att du har en robotarm som håller en penna mot ett papper.
# Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:
#forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
#backward - gå bakåt
#left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
#dot - sätt ut en prick med en viss storlek
#speed - normal=6, fast=10, maximal=0

#Läs mer här: Turtle graphics — Python 3.13.1 documentation
#Kodexempel:
#import turtle as t

# Upprepa 3 gånger
#for x in range(3):
#    t.forward(100)
#    t.left(120)

# Lyft pennan för att flytta utan att rita
#t.penup()
#t.forward(200)
#t.pendown()
#t.dot(10, "red")
#t.color("blue"
#t.forward(50)

# Låt fönstret stanna kvar tills användaren stänger det
#t.mainloop()

import turtle as t
#1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
def square(length):
    for x in range(4):
        t.forward(length)
        t.left(90)

square(100)

#2 Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempel:
#for x in range(5):
#    t.square()
#    t.move_next()
def move_next():
    t.penup()
    t.forward(100)
    t.pendown()

move_next()
square(50)
move_next()

#3 Bygg om koden så att den ingår i en funktion, som ritar en komplett cirkel.
# Använd parametrar i stället för värdena 7, 40 och 30.
#Tips 1: vad händer om man varierar värdet på range?
#Tips 2: 360 grader motsvarar ett helt varv.
#for x in range(7):
#    t.forward(40)
#    t.right(30)
def circle(range_, smoothing):
    for x in range(smoothing): #x1
        t.forward(range_) #radius
        t.right(360/smoothing) #x2, x1*x2 = 360

circle(15, 30)


#4 Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen.
# Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.

















t.mainloop()