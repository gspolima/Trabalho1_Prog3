def calcular_retorno_investimento():
    investimento_mensal = float(input('Insira o valor inicial a investir: '))
    juros_inteiro = float(input('Insira percentual de juros ao mês: '))
    juros_ao_mes = juros_inteiro / 100

    acumulado_anual = 0
    acumulado_total = 0

    while (True):
        contador = 0
        acumulado_anual = acumulado_total
        while (contador < 12):
            if (contador == 0):
                if (acumulado_anual == 0):
                    acumulado_anual = investimento_mensal
                contador += 1
                continue

            acumulado_anual += (investimento_mensal + (acumulado_anual * (juros_ao_mes)))
            contador += 1

        print('O retorno após um ano é de: R$', format(acumulado_anual, '.2f'))
        deseja_continuar = input('Deseja calcular por mais um ano? (S ou N): ')
        if (deseja_continuar.upper() == 'N'):
            print('*** O retorno total somados todos os anos é de: R$', format(acumulado_total, '.2f'), '***')
            print('Encerrando...')
            break

        acumulado_total += acumulado_anual
        if (acumulado_total == acumulado_anual):
            continue

        print('*** O retorno total somados todos os anos é de: R$', format(acumulado_total, '.2f'), '***')
        print('--------------------------------------------------------------------------')

calcular_retorno_investimento()