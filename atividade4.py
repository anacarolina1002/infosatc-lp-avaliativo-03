#Você foi escalado para desenvolver um sistema para um laboratório de doação de sangue.
#Para  ser  um  doador,  a  pessoa  precisa  atender  os  seguintes requisitos básicos:
# A.Ter entre 16 e 69 anos.
# B.Mais de 50kg.
# C.Ter dormido pelo menos 6h nas últimas 24horas;
# O  seu  sistema  precisa  solicitar  essas  informações  da  pessoa, 
# fazer  as  devidas verificações  e  ao  final  mostrar  se  ela  pode  ser  uma  doadora 
# ou  não. Caso  ela  não atenda algum dos requisitos, mostre qual requisito está fora do 
# escopo.

idadecont = 0
pesocont = 0
horascont =0

idade=(int(input("Insira a sua idade: ")))
peso=(float(input("Insira o seu peso: ")))
horas=(int(input("Insira quantas horas de sono tiveste na ultima noite: ")))

if idade>=16 and idade<=69:
    idadecont+=1
else:
    print("Idade fora dos requisitos!")
if peso>50:
    pesocont+=1
else:
    print("Peso fora dos requisitos!")
if horas>=6:
    horascont+=1
else:
    print("Horas de sono fora dos requisitos!")
if idadecont == 1 and pesocont == 1 and horascont == 1:
    print("Você pode ser um doador!")
else:
    print("Você não pode ser um doador.")
 