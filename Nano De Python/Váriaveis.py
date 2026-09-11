#Exemplos de variaveis, como declarar, atribuir e imprimir na tela
nome="Humberto Delgado"
empresa='FIAP'
qtde_funcionarios=500
mediaMensalidade=856.50

nome="Humberto Delgado"
empresa='FIAP'
qtde_funcionarios=500
mediaMensalidade=856.50
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

#Como atribuir declaração de variáveis com input do usuário
nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

#Mostrando o Tipo das variavais no codigo
nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("==============Verifique os tipos de dados abaixo:==============")
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

#declaração de variáveis com input do usuário e impressão de uma declaração
responsavel=input("Digite o nome do responsável: ")
funcionario=input("Digite o nome do funcionário: ")
evento=input("Digite o nome do evento: ")
valor=float(input("Digite o valor que será ressarcido: "))

print("Declaro para o senhor " + responsavel + ", que o senhor " + funcionario + " esteve presente no evento " + evento + " e gastou o valor de R$ " + str(valor) + " com a entrada.")