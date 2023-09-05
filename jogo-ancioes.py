def checar_empate(tabuleiro):
    for linha in tabuleiro:
        if '_' in linha:
            return False
    return True

def checar_vitoria(tabuleiro):
    for num in range(3):
        # CHECA SE HÁ VENCEDORES EM CADA LINHA
        if tabuleiro[num][0] == tabuleiro[num][1] == tabuleiro[num][2] and tabuleiro[num][0] != '_': 
            return tabuleiro[num][0]
        # CHECA SE HÁ VENCEDORES EM CADA COLUNA
        elif tabuleiro[0][num] == tabuleiro[1][num] == tabuleiro[2][num] and tabuleiro[0][num] != '_': 
            return tabuleiro[0][num]
    # CHECA AS DUAS DIAGONAIS
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != '_':
        return tabuleiro[0][0]
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != '_':
        return tabuleiro[0][2]

def minimax(tabuleiro, jogador):
    ganhador = checar_vitoria(tabuleiro)
    if ganhador == 'x':
        return 1
    elif ganhador == 'o':
        return -1
    elif checar_empate(tabuleiro):
        return 0
    
    if jogador == 'x':  # ESTRATÉGIA MAX
        melhor_ponto = -1000*1000
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == '_':
                    tabuleiro[linha][coluna] = 'x'
                    ponto = minimax(tabuleiro, 'o')
                    tabuleiro[linha][coluna] = '_'
                    melhor_ponto = max(ponto, melhor_ponto)
    else:  # ESTRATÉGIA MIN
        melhor_ponto = 1000*1000
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == '_':
                    tabuleiro[linha][coluna] = 'o'
                    ponto = minimax(tabuleiro, 'x')
                    tabuleiro[linha][coluna] = '_'
                    melhor_ponto = min(ponto, melhor_ponto)
    return melhor_ponto

quadro = []
player = ''
numeros_de_x = numeros_de_o = 0
vazio = False
for row in range(3):
    linha = input().split('|')
    quadro.append(linha)

for linha in quadro:
    numeros_de_x += linha.count('x')
    numeros_de_o += linha.count('o')

if numeros_de_x <= numeros_de_o:
    player = 'x'
else:
    player = 'o'

if numeros_de_x == 0 and numeros_de_o == 0:
    vazio = True

if not vazio:
    game = minimax(quadro, player)
    if game == 0:
        print('As previsões indicam que o resultado é empate. Aperte o botão correspondente')
    elif game == 1:
        print(f'As previsões indicam que o resultado é vitória do x. Aperte o botão correspondente')
    else:
        print(f'As previsões indicam que o resultado é vitória do o. Aperte o botão correspondente')
else:
    print('As previsões indicam que o resultado é empate. Aperte o botão correspondente')