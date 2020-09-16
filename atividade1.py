#Leia  um  número  inteiro  entre  1  e  12 e  escreva  o  mês  correspondente.
#Caso  o usuário  digite  um  número  fora  desse  intervalo,
# deverá  aparecer  uma  mensagem informando que não enumeroiste mês com esse número.

numero=int(input("Insira um número entre 1 e 12:"))
if (numero == 1):
 print("O número digitado foi:",numero,", equivalente ao mês de Janeiro")

elif (numero == 2):
 print("O número digitado foi:",numero,", equivalente ao mês de Fevereiro")

elif (numero == 3):
 print("O número digitado foi:",numero,", equivalente ao mês de Março")

elif (numero == 4):
 print("O número digitado foi:",numero,", equivalente ao mês de Abril")

elif (numero == 5):
 print("O número digitado foi:",numero,", equivalente ao mês de Maio")

elif (numero == 6):
 print("O número digitado foi:",numero,", equivalente ao mês de Junho")

elif (numero == 7):
 print("O número digitado foi:",numero,", equivalente ao mês de Julho")

elif (numero == 8):
 print("O número digitado foi:",numero,", equivalente ao mês de Agosto")

elif (numero == 9):
 print("O número digitado foi:",numero,", equivalente ao mês de Setembro")

elif (numero == 10):
 print("O número digitado foi:",numero,", equivalente ao mês de Outubro")

elif (numero == 11):
 print("O número digitado foi:",numero,", equivalente ao mês de Novembro")

elif (numero == 12):
 print("O número digitado foi:",numero,", equivalente ao mês de Dezembro")

else: 
 print("Mês inválido!")