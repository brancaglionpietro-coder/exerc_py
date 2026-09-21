def calcular_media(notas):
    soma = 0
    for nota in notas: 
        soma+=nota # soma = soma + nota
    return soma / len(notas)

notas = [5 , 5 , 6]
media = calcular_media(notas)

if media >= 7:
    print("Aprovado!!!")
elif media >= 5:
    print("Recuperação!!!")
else:
    print("Reprovado!!!")