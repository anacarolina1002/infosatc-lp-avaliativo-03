#Ler do teclado a idade e o sexo de 10 pessoas. Calcule e imprima:
# A.Idade média das numMulheres.
# B.Idade média dos numHomens.
# C.Idade média do grupo.

idadeMulheres=0
idadeHomens=0
numMulheres=0
numHomens=0
for x in range(0,10):
    sexo=(input("Digite seu sexo (F-Feminino M-Masculino): "))
    if sexo=="F":
         numMulheres=numMulheres+1
         idadeMulheres=idadeMulheres+(int(input("Insira sua idade: ")))
    elif sexo=="M":
        numHomens=numHomens+1
        idadeHomens=idadeHomens+(int(input("Insira sua idade: ")))

mediaMulheres=(idadeMulheres/numMulheres)
mediaHomens=(idadeHomens/numHomens)
mediaGeral =(idadeMulheres+idadeHomens)/(numMulheres+numHomens)

print("A média de idade feminina é:",mediaMulheres)
print("A média de idade masculina é:",mediaHomens)
print("A média geral de idade é:",mediaGeral)
         
         
        

