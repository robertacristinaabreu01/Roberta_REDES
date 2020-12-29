
nome = input("Digite um funcionário: " )
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)                 #string usa (+) string
print("Possui: ", qtde_funcionarios, " funcionários.")          #string usa ( , var num , ) número
print("A média da mensalidade é de : " + str(mediaMensalidade))
print("===================Verifique os tipos de dados abaixo: ======================")
print("O tipo de variável [nome] é: ", type(nome))
print("O tipo de variável [empresa] é: ", type(empresa))
print("O tipo de variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de variável [mediaMensalidade] é: ", type(mediaMensalidade))

# nome="Roberta Cristina de Abreu"
# empresa="FIAP"
# qtde_funcionarios=500
# mediaMensalidade=856.50
# print(nome+" trabalha na empresa " + empresa)
# print("Possui: " + qtde_funcionarios, "funcionários.")
# print("A média da mensalidade é de : " + str(mediaMensalidade))