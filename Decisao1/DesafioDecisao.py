nivelAcesso=input("Qual o seu nível de acesso [ADM e USR ou GUEST] : ").upper()
genero=input("Digite seu genêro [FEMININO ou MASCULINO] : ").upper()

#PROBLEMA ADM
if nivelAcesso=="ADM":
    if genero=="FEMININO" or "FEM":
        print("Olá Administradora!")
    else:
        print("Olá Administrador!")

#PROBLEMA USR
elif nivelAcesso=="USR":
    if genero=="FEMININO" or "MASC":
        print("Olá usuária! ")
    else:
        print("Olá usuário!")

#PROBLEMA GUEST
elif nivelAcesso=="GUEST":
   print("Olá visitante!")

else:
    print("Olá desconhecido(a)! ")
