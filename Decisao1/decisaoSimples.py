nome=input("Digite o nome: ")
idade = int(input("Digite a sua idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O paciente " +  nome + " possui atendimento prioritário? " + prioridade)

#decisão simples