KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._tarkista_parametri(kapasiteetti, KAPASITEETTI, "kapasiteetti")
        self.kasvatuskoko = self._tarkista_parametri(kasvatuskoko, OLETUSKASVATUS, "kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _tarkista_parametri(self, arvo, oletus, nimi):
        if arvo is None:
            return oletus
        if not isinstance(arvo, int) or arvo < 0:
            raise ValueError(f"Virheellinen {nimi}: {arvo}")
        return arvo

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm >= len(self.ljono):
            self._kasvata_taulukkoa()

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def _kasvata_taulukkoa(self):
        uusi_koko = len(self.ljono) + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        self._kopioi_lista(self.ljono, uusi_lista)
        self.ljono = uusi_lista

    def poista(self, n):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == n:
                self._siirra_vasemmalle(i)
                self.alkioiden_lkm -= 1
                return True
        return False

    def _siirra_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]
        self.ljono[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, alkuperainen, kohde):
        for i in range(len(alkuperainen)):
            kohde[i] = alkuperainen[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list() + b.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for luku in a_taulu:
            if luku in b_taulu:
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for luku in a.to_int_list():
            if luku not in b.to_int_list():
                tulos.lisaa(luku)
        return tulos

    def __str__(self):
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
