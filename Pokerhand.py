#När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas.
# Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
#poker_hand(cards)
#"Du fick ett par med valören: 5"

#1 Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element:
# färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess,
# för enkelhets skull använder vi talen 2 till 14.
#Exempel på ett kort: ["hjärter", 12]

#2 Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

#3 Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna
# ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

#Fortsätt att lägga till fler kontroller till funktionen.
#Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
#pretty_print_card(["hjärter", 5]) → "hjärter fem"
#Lista med pokerhänder.
#Ett par (två lika kort)
#Två par
#Tretal (tre lika)
#Straight (5 kort i följd, t.ex. 7-8-9-10-11)
#Flush / färg (alla kort har samma färg)
#Hus (par och tretal med olika valörer)
#Fyrtal
#Straight flush (5 kort i följd, med samma färg)
#Femtal



import random

def shuffle_card():
    card_suit = ["diamonds", "hearts", "spades", "clubs"]
    card_denomination = random.randint(2, 14)
    return [random.choice(card_suit), card_denomination]

def are_cards_same(card1, card2):
    if card1 == card2:
        return True
    else:
        return False

#Check if the list of 5 cards contains at least one pair (two cards with the same rank).
def poker_hand():
    my_cards = []
    same_rank_cards = []
    for i in range(5):
        card = shuffle_card()
        for j in range(len(my_cards)):
            if card[1] == my_cards[j][1]:
                same_rank_cards.append(card)
                print(f"Du fick ett par med valören: {card[1]}")
        my_cards.append(card)
    print(my_cards)
    if len(same_rank_cards) == 0:
        print("Inga par idag, tyvärr...")
    else:
        print("Du har tur!")

poker_hand()