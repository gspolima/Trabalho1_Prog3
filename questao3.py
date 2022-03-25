def enesima_sequencia_de_fibonacci():
    limite = int(input('Insira quantos elementos quer ter na sequência: '))
    print('Sequência de Fibonacci com', limite, 'elementos:')
    primeiro = 0
    segundo = 1
    contador = 2
    print(primeiro, segundo, end=" ")
    while (contador < limite):
        proximo_elemento = primeiro + segundo
        print(proximo_elemento, end=" ")
        primeiro = segundo
        segundo = proximo_elemento
        contador += 1

enesima_sequencia_de_fibonacci()