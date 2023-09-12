class Pessoa:
  "Isto é uma classe nova chamada Pessoa"
  idade = 15
  
  def saudacao(self):
    print("Olá Pessoas!")
    
    
print(Pessoa.idade)

print(Pessoa.saudacao)

print(Pessoa.__doc__)

gabi = Pessoa()

print(gabi.idade)
print(gabi.saudacao)
gabi.saudacao()
