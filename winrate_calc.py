multiplicadores_coletados = []
multiplicadores_possiveis = 0.99
valor_apostado = 10
winrates = []

#Coleta os multiplicadores do txt
with open('./databaseCrash.txt', 'r') as file:
    for linha in file:
        linha = linha.rstrip()
        palavras = linha.split()
        multiplicador = float(palavras[0])
        multiplicadores_coletados.append(multiplicador)


#Iteração de multiplicadores possíveis
while multiplicadores_possiveis < 10:
    win = 0
    multiplicadores_possiveis = multiplicadores_possiveis + 0.01
    multiplicadores_possiveis = float(f'{round(multiplicadores_possiveis, 2)}')

    lucro = (multiplicadores_possiveis * valor_apostado) - valor_apostado
    lucro = float(f'{round(lucro, 2)}')
    perda = valor_apostado
    winrate_minimo = (perda * 100) / (lucro + perda)
    winrate_minimo = float(f'{round(winrate_minimo, 2)}')

    for number in multiplicadores_coletados:
        if multiplicadores_possiveis <= number:
            win += 1
        else:
            pass

    winrate = (win / len(multiplicadores_coletados)) * 100
    winrate = float(f'{round(winrate, 2)}')

    print(f'multiplicador: {multiplicadores_possiveis}, lucro: {lucro}, perda: {perda}, wins: {win}, winrate mínimo: {winrate_minimo}%, winrate: {winrate}%')
    # print(f'multiplicador: {multiplicadores_possiveis}, winrate: {winrate}%')
    
    winrates.append(winrate)

# print(f'números coletados: {len(multiplicadores_coletados)}')
print(winrates)