# MD5Hash no comments by canuto.

import hashlib
from rich.progress import track
from time import sleep

while True:
    textoinit = input("Digite o que deseja converter: ")
    print('----------------------------------------------------------------------')
    for tarefa in track(range(2), 'Convertendo...'):
        sleep(1)
        result = hashlib.md5(textoinit.encode())
    print('----------------------------------------------------------------------')
    print("O seu texto em md5 é: ", end="")
    resultado = result.hexdigest()
    print(resultado)

    arquivo = open("md5.txt", "a", newline='')
    arquivo.write('Sua String inicial: ')
    arquivo.write(textoinit)
    arquivo.write('\nSeu md5 convertido: ')
    arquivo.write(str(resultado))
    arquivo.write('\n\n')
    arquivo.close()

    print('----------------------------------------------------------------------')
    print('1 = Sim \n2 = Não')
    enter = input('Deseja encodar outro md5: ')

    if enter == '2':
        print('Saindo...')
        break

    elif enter == '1':
        sleep(1)
        pass

    else:
        print('Opção Incorreta!')
        sleep(3)
        break
