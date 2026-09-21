jogadores = ["Pipi", "Baiano", "Berber", "Luquinhas", "Auda"]
gols = [12, 20, 15, 19, 26]

def calc_gols(gols):
    total_gols = 0 
    for gol in gols:
        total_gols += gol
    return total_gols 

def med_gols(gols, jogadores):
    total_gols = 0 
    for gol in gols:
        total_gols += gol
    return total_gols / len(jogadores)    

media = med_gols(gols, jogadores)
print(media)

total = calc_gols(gols)
print(total)