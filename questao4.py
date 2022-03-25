from typing import List


def encontrar_divisores_numero():
    while (True):
        numero = int(input('Digite um número para encontrar seus divisores: '))
        divisores: List = list()
        is_primo = True

        for i in range(1, numero + 1).__reversed__():
            if (i == numero or i == 1):
                divisores.append(i)
                continue
            elif (numero % i == 0):
                is_primo = False
                divisores.append(i)

        if (is_primo):
            print("O número", numero, 'é PRIMO')
        else:
            print('Os divisores de', numero, 'são:', divisores)

        decisao = input('Deseja analisar outro número? (S ou N): ')
        if (decisao.upper() == 'N'):
            print('Encerrando...')
            break
        else:
            print('-----------------------------------------------')
            continue

encontrar_divisores_numero()