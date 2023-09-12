class Televisor:
    def __init__(self, fabricante, modelo):
        self._fabricante = fabricante
        self._modelo = modelo
        self._canal_atual = None
        self._lista_de_canais = []
        self._volume = 20

    def aumentaVolume(self, valor):
        if valor < 0:
            raise ValueError("O valor de aumento do volume deve ser positivo.")
        if self._volume + valor <= 100:
            self._volume += valor
        else:
            self._volume = 100

    def diminuiVolume(self, valor):
        if valor < 0:
            raise ValueError("O valor de diminuição do volume deve ser positivo.")
        if self._volume - valor >= 0:
            self._volume -= valor
        else:
            self._volume = 0

    def trocaCanal(self, canal):
        if canal in self._lista_de_canais:
            self._canal_atual = canal

    def sintonizaCanal(self, canal):
        if canal not in self._lista_de_canais:
            self._lista_de_canais.append(canal)

    def getFabricante(self):
        return self._fabricante

    def getModelo(self):
        return self._modelo

    def getVolume(self):
        return self._volume

    def getCanalAtual(self):
        return self._canal_atual
