tentativas = []

def registrar_t(tentativas):
    for i in range(0,10):
        t = int(input(f"Digite os pontos da tentativa {i+1}:"))
        if t < 4 and t > -1:
            tentativas.append(t)
        else:
            print("\nValor inválido")
            t = int(input(f"Digite os pontos da tentativa {i+1}:"))
            if t < 4 and t > -1:
                tentativas.append(t)
            else:
                print("\nValor inválido, tentativa será considerada como erro")
                tentativas.append(0)
    return tentativas

def pont_Total(tentativas):
    pTotal = 0
    for t in tentativas:
        pTotal += t
    return pTotal

def erros(tentativas):
    erro = []
    for t in tentativas:
        if t == 0:
            erro.append(t)
    return len(erro)

def acertos(tentativas):
    acerto = []
    for t in tentativas:
        if t != 0:
            acerto.append(t)
    return len(acerto)

def frequencia(tentativas):
    maisF =  max(set(tentativas), key=tentativas.count)
    return maisF

while True:
    print("\n1-Registrar Tentativas\n2-Ver tentativas\n3-Soma das pontuações\n4-Número de erros\n5-Número de acertos\n6-Percentual de aproveitamento\n7-Mais frequente\n8-Sair")
    escolha = int(input("Digite a opção que deseja:"))
    
    if escolha == 1:
        registrar_t(tentativas)
        print("\nTentativas registradas")
    elif escolha == 2:
        ind = len(tentativas)
        for i in range(0,ind):
            print(f"\n\nTentativa {i+1}: {tentativas[i]} pts")
    elif escolha == 3: 
        soma = pont_Total(tentativas)
        print(f"\n\nA pontuação total foi: {soma} pts")
    elif escolha == 4:
        e = erros(tentativas)
        print(f"\n\nO número de erros foi: {e}")
    elif escolha == 5:
        a = acertos(tentativas)
        print(f"\n\nO número de acertos foi: {a}")
    elif escolha == 6:
        a = acertos(tentativas)
        perc = a/len(tentativas)
        print(f"\n\nO percentual de acertos foi de: {perc*100}%")
    elif escolha == 7:
        maisF = frequencia(tentativas)
        print(f"\n\nA cesta com mais frequencia foi a de {maisF} pts")
    elif escolha == 8:
        break
    else:
        print("\n\nDigite uma opção válida")