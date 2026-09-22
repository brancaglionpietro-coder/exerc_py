jogadores = ['Baiano', 'Pipi', 'Bernardo', 'Luquinhas', 'Caliel']
gols= [37, 12, 25, 2, 0]
indices= []

def calcTGol(gols):
    total_gols = 0
    for gol in gols:
        total_gols += gol
    return total_gols

def mediaGols(gols, jogadores):
    total_gols = 0
    for gol in gols:
        total_gols += gol
    return total_gols / len(jogadores)

def maisqMedia(gols, jogadores):
    maisMedia= []
    total_gols = 0
    for gol in gols:
        total_gols += gol
    mediag = total_gols/len(jogadores)
    for gol in gols:
        if gol > mediag:
            i = gols.index(gol)
            maisMedia.append(jogadores[i])
    return maisMedia

def artilharia(gols, jogadores):
    gols_art = max(gols)
    index_art = gols.index(gols_art)
    return jogadores[index_art]
    
while True:
    print("1-Dados por jogador\n2-Media do Time\n3-Total de Gols\n4-Artilheiro\n5-Acima da Média\n6-Sair")
    escolha = int(input("Digite o Número da opção que deseja:"))
                            
    if escolha == 1:
        for i in range(0,5):
            print(f"\nJogador: {jogadores[i]};\nGols: {gols[i]}\n")

    elif escolha == 2:
        media = mediaGols(gols, jogadores)
        print(f"\nMedia do Time: {media}\n")

    elif escolha == 3:
        total = calcTGol(gols)
        print(f"\nTotal da equipe: {total}\n")

    elif escolha == 4:
        artilheiro = artilharia(gols, jogadores)
        print(f"O artilheiro foi {artilheiro}")

    elif escolha == 5:
        mais = maisqMedia(gols, jogadores)
        ind = len(mais)
        for i in range(0, ind):
            print(f"{mais[i]}\n")
            
    elif escolha == 6:
        break
    
    else:
        print("escolha uma opção válida")
    


