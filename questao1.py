from inspect import _void


def exibir_tabuada():
    numero = int(input('Insira o número para mostrar a tabuada: '))
    for i in range(1, 11):
        print(numero,'*', i, '=', numero * i)

exibir_tabuada()