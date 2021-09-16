#Importação da Hashlib, a biblioteca que vai nos permitir transformar o texto em md5.
import hashlib

convert = input("Encode or Decode?")

if convert == 'Decode':
    textoinit = input("Digite o que deseja converter: ") #O input que permite que você escreva o que deseja converter.
    result = hashlib.md5(textoinit.encode())
    print("O seu texto em md5 é: ", end ="")
 
elif convert == 'Encode':
    textoinit = input("Insira seu texto em MD5: ")
    result = hashlib.md5(textoinit.encode())
    print("Sua conversão em texto é: ", end ="")


print(result.hexdigest()) #Print que mostra o resultado na tela do usuário.

