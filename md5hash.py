# Importação da Hashlib, a biblioteca que vai nos permitir transformar o texto em md5.
import hashlib
# Rich, biblioteca que permite usar a progressbar, simples de instalar.
from rich.progress import track
# Biblioteca TIME para conseguirmos usar o comando sleep.
from time import sleep

while True:  # Permite que o programa possa rodar várias vezes.
    # Configuração para converter o texto.
    # O input que permite que você escreva o que deseja converter.
    textoinit = input("Digite o que deseja converter: ")
    print('----------------------------------------------------------------------')
    # ProgressBar enquanto ele encoda seu MD5
    for tarefa in track(range(2), 'Convertendo...'):
        sleep(1)  # Comando sleep apenas para dar um intervalo na progressbar.
        # Resultado da conversão do encode.
        result = hashlib.md5(textoinit.encode())

# Parte Final.
    print('----------------------------------------------------------------------')
    print("O seu texto em md5 é: ", end="")  # O Que mostra seu md5 na tela.
    resultado = result.hexdigest()
    print(resultado)  # Print que mostra o resultado na tela do usuário..
    print('----------------------------------------------------------------------')

# Gera um arquivo .txt que armazena suas strings e seus md5 convertidos.
    arquivo = open("md5.txt", "a", newline='')
    arquivo.write('Sua String inicial: ')
    arquivo.write(textoinit)
    arquivo.write('\nSeu md5 convertido: ')
    arquivo.write(str(resultado))
    arquivo.write('\n\n')
    arquivo.close()


# Correção para não finalizar o programa de uma vez.
    print('1 = Sim \n2 = Não')  # Decisão do Usuário!
    # Input aonde o usuário vai digitar se quer fazer o código rodar denovo ou não!
    enter = input('Deseja encodar outro md5: ')

# Opção 2: Sair do Programa.
    if enter == '2':
        sleep(2)
        print('Saindo...')
        break

# Opção 1: Fazer o código rodar novamente!
    elif enter == '1':
        sleep(1)

# Caso não seja 1 ou 2, o programa fecha automáticamente, mostrando uma mensagem!
    else:
        print('Opção Incorreta!')
        sleep(2)
        break
