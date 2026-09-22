Nomes = ["Dipirona", "Paracetamol", "Loratadina"]
Precos = [12.50, 9.90, 18.75]
Estoques = [20, 15, 8]

def pesquisar(nomes):
    pesq = input("Qual remédio deseja buscar? ")
    indice = []
    for indice in range(len(nomes)):
        print("")
while True:
    print("\n1 - Listar medicamentos\n2 - Pesquisar medicamento\n3 - Registrar venda\n4 - Repor estoque\n5 - Mostrar estoque baixo\n6 - Encerrar\n")

    escolha = int(input("Digite uma das opções: \n"))

    if escolha == 1:
        for i in range(0,3):
            print(f"Medicamento: {Nomes[i]}\nPreços: R${Precos[i]}\n")
    elif escolha == 6:
        break
    else:
        print("Valor inválido!!")   