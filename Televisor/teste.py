from Televisor import Televisor
from ControleRemoto import ControleRemoto


class Teste:
  pass

tv = Televisor("Samsung", "Samsung-2023")
controle = ControleRemoto(tv)

controle.sintonizaCanal("Sbt")
controle.trocaCanal("Sbt")

controle.aumentaVolume()  # Aumenta o volume em 90 unidades
controle.diminuiVolume()  # Diminui o volume em 90 unidades
controle.trocaCanal(5)    # Troca para o canal 5
controle.sintonizaCanal(10)  # Sintoniza o canal 10

print(f"Volume atual: {tv.getVolume()}")
print(f"Canal atual: {tv.getCanalAtual()}")

print(tv._canal_atual)