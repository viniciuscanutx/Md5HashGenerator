
#Importação da Hashlib, a biblioteca que vai nos permitir transformar o texto em md5.
import hashlib

#Configuração para converter o texto.
textoinit = input("Digite o que deseja converter: ") #O input que permite que você escreva o que deseja converter.
result = hashlib.md5(textoinit.encode()) #Resultado da conversão do encode.
    
#Parte Final.
print("O seu texto em md5 é: ", end ="")#O Que mostra seu md5 na tela.
print(result.hexdigest()) #Print que mostra o resultado na tela do usuário..

#Correção para não finalizar o programa de uma vez.
input()