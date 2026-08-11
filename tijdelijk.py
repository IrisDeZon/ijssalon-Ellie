from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5
    }
    aanbieding = 0.8 * prijzen["aardbei"]

    reclame_tekst = f"Vandaag in de aanbiedinng: vanille-ijs, 1 liter - slechts €{aanbieding}"
    reclame_tekst2 = reclame_tekst[:63]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split(" ")

    el = ""
    for item in reclame_tekst4:
        el =f"{item}"
        if  len(el)<5:
            print(el.lower())
        else:
            print(el)

decoreer("Aanbieding")
print_aanbieding()