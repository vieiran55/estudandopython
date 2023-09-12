class Main:
  pass

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.get_nome(), 1222)

conta.deposita(1000)
conta.saque(50)
conta.extrato()

print(c1._nome)
print(c1._telefone)