
prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
aanbieding = 0.8 * prijzen["aardbei"]
#print(aanbieding)
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding:.2f}"
#print(reclame_tekst)
reclame_tekst2 = reclame_tekst[:62]
#print(reclame_tekst2)
reclame_tekst3 = reclame_tekst2.upper()
#print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split(" ")
#print(reclame_tekst4)

#Opdracht8
#el = ""
# for item in reclame_tekst4:
#    el += f"{item}" + "\n"
#print(el)

#opdracht 9
#el= el.lower()
#print(el)

#opdracht10
el = ""
for item in reclame_tekst4:
    el =f"{item}"
    if  len(el)<5:
        print(el.lower())
    else:
        print(el)
