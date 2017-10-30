# napis program, ktery vrati pocet jednicek v zadanem cisle
# zkus to vyresit i bez prace s retezci

# # reseni retezcem
# cislo=input("Zadej cislo: ")
#
# pocet_jednicek = cislo.count("1")
#
# print("Pocet jednicek v cisle {} je {}.".format(cislo, pocet_jednicek))

def pocet_jednicek(cislo):
    pocet = 0
    while cislo >0:
        # print (cislo)
        zbytek = cislo % 10
        if zbytek == 1:
            pocet = pocet + 1
        print (zbytek)
        cislo = cislo // 10
    return pocet

cislo=int(input("Zadej cislo: "))
pocet = pocet_jednicek(cislo)
print("Pocet jednicek v cisle {} je {}.".format(cislo, pocet))
