print('________________NOSSA TABUADA________________')

tabuada=int(input("Digite qual tabuada que deseja: \n"))
print("\tA Tabuada escolhida foi do número ", tabuada)
#for valor in range(1,11,1):
#    print(tabuada, " x ", valor, " = ", (tabuada*valor))
for valor in range(1,11,1):
   print(str(tabuada) + " x " + str(valor) + " = " + str(tabuada*valor))