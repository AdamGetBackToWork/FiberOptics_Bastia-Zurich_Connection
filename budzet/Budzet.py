# Projekt lacza:
# Tx -> smf_woda + dcf_woda -> AMP -> 2 szpule smf_lad (100km) -> AMP -> 4 szpule smf_lad (200km) -> AMP -> 137km smf_lad + 38km dcf_lad -> AMP -> 169km dcf_lad -> AMP -> Rx

# Klasy reprezentujace poszczegolne elementy - nazwy tlumacza sie cale
class Swiatlowod:
    def __init__(self, tlumienie, dlugosc, dyspersja, szpula):
        self.tlumienie = tlumienie
        self.dlugosc = dlugosc
        self.dyspersja = dyspersja
        self.szpula = szpula


class ZLACZE:
    def __init__(self):
        self.tlumienie = None


class WZMACNIACZ:
    def __init__(self):
        self.wzmocnienie = None


class SPOINY:
    def __init__(self):
        self.tlumienie = None


class FOTODIODA:
    def __init__(self):
        self.czulosc = None

# Funkcje do liczenia:
# dlugosc swiatlowodu kompensujacego DCF
def oblicz_Ldcf(smf: Swiatlowod, dcf: Swiatlowod) -> float:
    dlugosc_dcf = -(smf.dyspersja * smf.dlugosc) / dcf.dyspersja
    return dlugosc_dcf

# calkowite tlumienie
def oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoiny, t_zlacz):
    return t_lad + t_woda + t_spoiny + t_zlacz

# finalne liczenie budzetu
def oblicz_budzet(tlumienie, wzmocnienie):
    return tlumienie - wzmocnienie


# obliczenie dlugosci na podstawie Lsmf = cala dlugosc trasy, Ldcf = dlugosc w szpuli
smf_lad = Swiatlowod(tlumienie=0.16, dlugosc=437, dyspersja=18, szpula=50.4)
dcf_lad = Swiatlowod(tlumienie=0.265, dlugosc=0, dyspersja=-38, szpula=50.4)
dcf_lad.dlugosc = oblicz_Ldcf(smf_lad, dcf_lad)
print(dcf_lad.dlugosc)

# tu dlugosci policzylem na kartce
smf_woda = Swiatlowod(tlumienie=0.154, dlugosc=40, dyspersja=21, szpula=30)
dcf_woda = Swiatlowod(tlumienie=0.198, dlugosc=210, dyspersja=-4, szpula=30)

# Wzmocnienie wzmacniacza
wzmacniacz = WZMACNIACZ()
wzmacniacz.wzmocnienie = 32 # dB

# Tlumienie zlaczek
zlaczka = ZLACZE()
zlaczka.tlumienie = 0.25  # dB/złącze

# Tlumienie spoin
spoina = SPOINY()  # na ladzie co 50.4km oraz na wodzie co 30km
spoina.tlumienie = 0.03  # dB/spoina

# Obliczenie tlumienia spoin
ilosc_spoin = 17 # okreslone na podstawie projektu lacza na gorze pliku
t_spoin = ilosc_spoin * spoina.tlumienie

# Obliczenie tlumienia zlaczek (connector-ow)
ilosc_zlacz = 12 
t_zlacz = zlaczka.tlumienie * ilosc_zlacz

# Obliczenie wzmocnienia wzmacniaczy -  okreslona na podstawie kompensacji tlumienia do poziomu akcpetowalnego <20dB
ilosc_wzmacniaczy = 5
wzmocnienie_wzmacniaczy = ilosc_wzmacniaczy * wzmacniacz.wzmocnienie

# Obliczenie tlumienia swiatlowodow na ladzie
tlumienie_swiatlowodu_lad_smf = smf_lad.tlumienie * smf_lad.dlugosc
tlumienie_swiatlowodu_lad_dcf = dcf_lad.tlumienie * dcf_lad.dlugosc
t_lad = tlumienie_swiatlowodu_lad_smf + tlumienie_swiatlowodu_lad_dcf

# Obliczenie tlumienia swiatlowodow pod woda
tlumienie_swiatlowodu_woda_smf = smf_woda.tlumienie * smf_woda.dlugosc
tlumienie_swiatlowodu_woda_dcf = dcf_woda.tlumienie * dcf_woda.dlugosc
t_woda = tlumienie_swiatlowodu_woda_smf + tlumienie_swiatlowodu_woda_dcf

# obliczenia tlumienia calkowitego na podstawie wylicoznych tlumien swiatlowodow orz wzmocnienia
calk_tlumienie = oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoin, t_zlacz)
calk_wzmocnienie = wzmocnienie_wzmacniaczy

# Obliczenie budzetu
budzet =  oblicz_budzet(calk_tlumienie, calk_wzmocnienie)

# dodanie marginesu M = 3dB
budzet_margines = budzet - 3

# Printowanie wynikow
print("\n--- Podsumowanie wyników ---\n")
print("Wyliczony budżet mocy, tłumienie na poziomie:", int(budzet) ,"dB na wrotach Rx (tu fotodiody)")
print("Wyliczony budżet mocy, z dodanym marginesem na poziomie 3dB:", int(budzet_margines), "dB na wrotach Rx ")


print("\n--- Szczegółowe obliczenia ---\n")
print("Długość DCF (ląd):", round(dcf_lad.dlugosc, 2), "km\n")

print("Tłumienie SMF lądowego:", round(tlumienie_swiatlowodu_lad_smf, 2), "dB")
print("Tłumienie DCF lądowego:", round(tlumienie_swiatlowodu_lad_dcf, 2), "dB")
print("Tłumienie SMF wodnego:", round(tlumienie_swiatlowodu_woda_smf, 2), "dB")
print("Tłumienie DCF wodnego:", round(tlumienie_swiatlowodu_woda_dcf, 2), "dB\n")

print("Tłumienie spoin:", round(t_spoin, 2), "dB (", ilosc_spoin, "spoin )")
print("Tłumienie złączy:", round(t_zlacz, 2), "dB (", ilosc_zlacz, "złączy )\n")
print("Całkowite tłumienie toru:", round(calk_tlumienie, 2), "dB")
print("Całkowite wzmocnienie wzmacniaczy:", calk_wzmocnienie, "dB\n")

