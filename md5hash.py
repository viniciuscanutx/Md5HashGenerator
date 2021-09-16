#Importação da Hashlib, a biblioteca que vai nos permitir transformar o texto em md5.
import hashlib
  
#Váriaveis que vão fazer nosso aplicativo funcionar.
textoinit = input("O que deseja converter?") #O input que permite que você escreva o que deseja converter.
result = hashlib.md5(textoinit.encode()) #Essa parte faz a conversão do texto pra md5.

#Resultado e o que vai aparecer na tela do usuário.
print("O seu texto em md5 é: ", end ="") #Esse Print é de orientação ao usuário.
print(result.hexdigest()) #Print que mostra o resultado na tela do usuário.

