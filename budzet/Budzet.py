
# Projekt zlacza:
# Tx -> smf_woda + dcf_woda -> AMP -> 2 szpule smf_lad (100km) -> AMP -> 4 szpule smf_lad (200km) -> AMP -> 137km smf_lad + 38km dcf_lad -> AMP -> 169km dcf_lad -> AMP -> Rx


from BudzetElementy import *

def oblicz_Ldcf(smf: Swiatlowod, dcf: Swiatlowod) -> float:
    dyspersja_smf = -(smf.dyspersja * smf.dlugosc) / dcf.dyspersja
    return dyspersja_smf


def oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoiny, t_zlacz):
    return t_lad + t_woda + t_spoiny + t_zlacz


def oblicz_budzet(tlumienie, wzmocnienie):
    return tlumienie - wzmocnienie


# obliczenie dlugosci na podstawie Lsmf = cala dlugosc trasy, Ldcf = dlugosc w szpuli
smf_lad = Swiatlowod(tlumienie=0.16, dlugosc=437, dyspersja=18, szpula=50.4)
dcf_lad = Swiatlowod(tlumienie=0.265, dlugosc=0, dyspersja=-38, szpula=50.4)
dcf_lad.dlugosc = oblicz_Ldcf(smf_lad, dcf_lad)

# tu dlugosci policzylem na kartce
smf_woda = Swiatlowod(tlumienie=0.154, dlugosc=40, dyspersja=21, szpula=30)
dcf_woda = Swiatlowod(tlumienie=0.198, dlugosc=210, dyspersja=-4, szpula=30)

# uzupelnienie parametrow wzmocnienia/tlumienia elementow
wzmacniacz = WZMACNIACZ()
wzmacniacz.wzmocnienie = 32 # dB

zlaczka = ZLACZE()
zlaczka.tlumienie = 0.25  # dB/złącze

spoina = SPOINY()  # na ladzie co 50.4km oraz na wodzie co 30km
spoina.tlumienie = 0.03  # dB/spoina

# to niewazne
# ilosc_spoin_lad = int(smf_lad.dlugosc / smf_lad.szpula)
# ilosc_spoin_woda = int(smf_woda.dlugosc / smf_woda.szpula)
# tlumienie_spoin_lad = ilosc_spoin_lad * spoina.tlumienie
# tlumienie_spoin_woda = ilosc_spoin_woda * spoina.tlumienie
# t_spoin = tlumienie_spoin_lad + tlumienie_spoin_woda

# tu wazne
ilosc_spoin = 17 # okreslone na podstawie projektu lacza na gorze pliku
t_spoin = ilosc_spoin * spoina.tlumienie

tlumienie_swiatlowodu_lad_smf = smf_lad.tlumienie * smf_lad.dlugosc
tlumienie_swiatlowodu_lad_dcf = dcf_lad.tlumienie * dcf_lad.dlugosc
t_lad = tlumienie_swiatlowodu_lad_smf + tlumienie_swiatlowodu_lad_dcf

tlumienie_swiatlowodu_woda_smf = smf_woda.tlumienie * smf_woda.dlugosc
tlumienie_swiatlowodu_woda_dcf = dcf_woda.tlumienie * dcf_woda.dlugosc
t_woda = tlumienie_swiatlowodu_woda_smf + tlumienie_swiatlowodu_woda_dcf

# wartosc przykladowa - tymczasowy bufor
ilosc_zlacz = 12 # 2 zlacza na odcinek ladowy, 2 na wodny, 2 na jeden wzmacniacz
t_zlacz = zlaczka.tlumienie * ilosc_zlacz

ilosc_wzmacniaczy = 5
wzmocnienie_wzmacniaczy = ilosc_wzmacniaczy * wzmacniacz.wzmocnienie

calk_tlumienie = oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoin, t_zlacz)
calk_wzmocnienie = wzmocnienie_wzmacniaczy

calk_wzmocnienie_margines = calk_wzmocnienie + 3

print("Wyliczony budżet mocy: ", int(oblicz_budzet(calk_tlumienie, calk_wzmocnienie)), "dB na wrotach Rx (tu fotodiody)")


