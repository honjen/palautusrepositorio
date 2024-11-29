class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_arvo = 0

    def _tallenna_tila(self):
        self._edellinen_arvo = self._arvo

    def miinus(self, operandi):
        self._tallenna_tila()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._tallenna_tila()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._tallenna_tila()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._tallenna_tila()
        self._arvo = arvo

    def kumoa(self):
        self._arvo = self._edellinen_arvo

    def arvo(self):
        return self._arvo
