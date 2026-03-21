from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
        nieuwe_prijs = prijs * (1 - korting)    
        zin = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
        return zin
print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal(inkomsten):
        return sum(inkomsten)
week_inkomsten = [220, 430, 125, 160, 205, 90, 341]
totaal = inkomsten_totaal(week_inkomsten)
print(totaal)

def inkomsten_totaal(inkomsten, btw):
        totaal = sum(inkomsten)
        btw_bedrag = totaal * btw
        return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarvoor nu {btw_bedrag} staat"
resultaat = inkomsten_totaal([220, 430, 125, 160, 205, 90, 341], 0.09)
print(resultaat)

def inkomsten_totaal(inkomsten, btw):
        totaal = sum(inkomsten)
        btw_bedrag = totaal * btw
        return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarvoor nu {btw_bedrag} euro btw betaald dient te worden"
resultaat = inkomsten_totaal([220, 430, 125, 160, 205, 90, 341], 0.09)
print(resultaat)

def laag_en_hoog(mijn_lijst):
        laagste = min(mijn_lijst)
        hoogste = max(mijn_lijst)
        return [hoogste, laagste]
inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten)
print(resultaat) 

def gemiddelde(mijn_lijst):
        gem_bedrag = sum(mijn_lijst) / len(mijn_lijst)
        return f"de gemiddelde inkomsten deze week zijn {gem_bedrag} euro"
inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten))

def meervoudig(invoer_lijst):    
        return laag_en_hoog(invoer_lijst)
def laag_en_hoog(mijn_lijst):
        return [max(mijn_lijst), min(mijn_lijst)]
print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

def laag_en_hoog(lijst):
    if not lijst:
        return []
    return [min(lijst), max(lijst)]

def mijn_functie_2(korte_lijst):
    return sum(korte_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

getallen = [10, 5, 3, 2, 1, 2, 9]
resultaat = combinatie(getallen)
print(resultaat) 