from algemene_functies import mijn_functie_2

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
inkomsten = mijn_lijst
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
invoer_lijst2 = [3, 5, 8, 7, 9, 6]

#vraag 5
def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = prijs*(1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de de smaak {smaak}, van {prijs} euro voor {kortingsprijs:.2f} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

#vraag 6 en 7
def inkomsten_totaal(btw, inkomsten):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    btwtotaal = btw*totaal
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btwtotaal} euro btw betaald dient te worden"
    return uitvoer

print(inkomsten_totaal(0.09, inkomsten))

# vraag 8 
def laag_en_hoog(mijn_lijst):
    maxmin = [max(mijn_lijst), min(mijn_lijst)]
    return maxmin
#print(laag_en_hoog(mijn_lijst))

#vraag 9 en 10
def gemiddelde(mijn_lijst):
    avg = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {avg:.2f} euro."
    return uitvoer

print(gemiddelde(mijn_lijst))

#vraag 11
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

#print (meervoudig(invoer_lijst))

#vraag 12 
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    #print(korte_lijst)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie(invoer_lijst2))