def definir_quantos_digitos_tem():
    numero = int(input('Informe um número inteiro positivo: '))
    numero_str = str(numero)
    print('O numero', numero, 'tem', numero_str.__len__(), 'digitos')

definir_quantos_digitos_tem()