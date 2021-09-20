#Importação da Hashlib, a biblioteca que vai nos permitir transformar o texto em md5.
import hashlib
#Rich, biblioteca que permite usar a progressbar, simples de instalar.
from rich.progress import track
#Biblioteca TIME para conseguirmos usar o comando sleep.
from time import sleep

while True: #Permite que o programa possa rodar várias vezes.
#Configuração para converter o texto.
 textoinit = input("Digite o que deseja converter: ")#O input que permite que você escreva o que deseja converter.
 print('----------------------------------------------------------------------')
 for tarefa in track(range(2), 'Convertendo...'):  #ProgressBar enquanto ele encoda seu MD5
    sleep(1) #Comando sleep apenas para dar um intervalo na progressbar.
    result = hashlib.md5(textoinit.encode()) #Resultado da conversão do encode.    
    
#Parte Final.
 print('----------------------------------------------------------------------')
 print("O seu texto em md5 é: ", end ="")#O Que mostra seu md5 na tela.
 print(result.hexdigest()) #Print que mostra o resultado na tela do usuário..
 print('----------------------------------------------------------------------')

#Correção para não finalizar o programa de uma vez.
 print('1 = Sim \n2 = Não') #Decisão do Usuário!
 enter = input('Deseja encodar outro md5: ') #Input aonde o usuário vai digitar se quer fazer o código rodar denovo ou não!

#Opção 2: Sair do Programa.
 if enter == '2':
    print('Saindo...')
    break

#Opção 1: Fazer o código rodar novamente!
 elif enter == '1':
   sleep(1)

#Caso não seja 1 ou 2, o programa fecha automáticamente, mostrando uma mensagem!        
 else:
    print('Opção Incorreta!')
    sleep(3)
    break

#Criando um arquivo que armazena seus MD5 e a Palavra que você converteu.