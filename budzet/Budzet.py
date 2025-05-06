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


def oblicz_Ldcf(smf: Swiatlowod, dcf: Swiatlowod) -> float:
    dyspersja_smf = -(smf.dyspersja * smf.dlugosc) / dcf.dyspersja
    return dyspersja_smf


def oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoiny, t_zlacz):
    return t_lad + t_woda + t_spoiny + t_zlacz


# obliczenie dlugosci na podstawie Lsmf = cala dlugosc trasy, Ldcf = dlugosc w szpuli
smf_lad = Swiatlowod(tlumienie=0.16, dlugosc=437, dyspersja=18, szpula=50.4)
dcf_lad = Swiatlowod(tlumienie=0.265, dlugosc=0, dyspersja=-38, szpula=50.4)
dlugosc_dcf = oblicz_Ldcf(smf_lad, dcf_lad)
dcf_lad.dlugosc = dlugosc_dcf

# tu dlugosci policzylem na kartce
smf_woda = Swiatlowod(tlumienie=0.154, dlugosc=40, dyspersja=21, szpula=30)
dcf_woda = Swiatlowod(tlumienie=0.198, dlugosc=210, dyspersja=-4, szpula=30)

# uzupelnienie parametrow wzmocnienia/tlumienia elementow
wzmacniacz = WZMACNIACZ()
wzmacniacz.wzmocnienie = 30  # dB

zlaczka = ZLACZE()
zlaczka.tlumienie = 0.25  # dB/złącze

spoina = SPOINY()  # na ladzie co 50.4km oraz na wodzie co 30km
spoina.tlumienie = 0.03  # dB/spoina

ilosc_spoin_lad = int(smf_lad.dlugosc / smf_lad.szpula)
ilosc_spoin_woda = int(smf_woda.dlugosc / smf_woda.szpula)

tlumienie_swiatlowodu_lad_smf = smf_lad.tlumienie * smf_lad.dlugosc
tlumienie_swiatlowodu_lad_dcf = dcf_lad.tlumienie * dcf_lad.dlugosc
t_lad = tlumienie_swiatlowodu_lad_smf + tlumienie_swiatlowodu_lad_dcf

tlumienie_swiatlowodu_woda_smf = smf_woda.tlumienie * smf_woda.dlugosc
tlumienie_swiatlowodu_woda_dcf = dcf_woda.tlumienie * dcf_woda.dlugosc
t_woda = tlumienie_swiatlowodu_woda_smf + tlumienie_swiatlowodu_woda_dcf

tlumienie_spoin_lad = ilosc_spoin_lad * spoina.tlumienie
tlumienie_spoin_woda = ilosc_spoin_woda * spoina.tlumienie
t_spoin = tlumienie_spoin_lad + tlumienie_spoin_woda

# wartosc przykladowa - tymczasowy bufor
ilosc_zlacz = 2 + 2 + 2 # 2 zlacza na odcinek ladowy, 2 na wodny, 2 na jeden wzmacniacz
t_zlacz = zlaczka.tlumienie * ilosc_zlacz

print(oblicz_tlumienie_calkowite(t_lad, t_woda, t_spoin, t_zlacz))

