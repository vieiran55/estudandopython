from funcionarios import Funcionario

funcionario= Funcionario('Gabriela', 'gabi@goxtosa.com.br')

funcionario.cadastro_hora('jan', 300)
funcionario.cadastro_hora('fev', 200)
funcionario.cadastro_salario_hora('jan', 30)
funcionario.cadastro_salario_hora('fev', 30)
print(funcionario)
print(funcionario.calcula_salario('jan'))
print(funcionario.calcula_salario('fev'))