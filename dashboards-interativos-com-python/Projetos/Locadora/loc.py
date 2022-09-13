import os

# Criando a lista de Carros
carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]

alugados = []

# Criando a função para imprimir a lista de Carros
def imprimirCarros(listaCarros):
    for i, car in enumerate(listaCarros):
        print("[{}] {} - R$ {}/dia".format(i,car[0],car[1]))


while True:

    os.system("cls")
    print("==============================")
    print("Bem-vindo a locadora de carros")
    print("==============================")
    print("[0] - MOSTRAR PORTFÓLIO")
    print("[1] - ALUGAR UM CARRO")
    print("[2] - DEVOLVER UM CARRO")
    print("\nO que deseja fazer?")
    op = int(input())
    if op == 0:
        os.system("cls")
        print("LISTA DOS CARROS DISPONÍVEIS")
        print("============================")
        imprimirCarros(carros)
        print("============================")
    elif op == 1:
        os.system("cls")
        imprimirCarros(carros)
        print("================")
        print("Qual carro você deseja alugar?")
        id = int(input())
        os.system("cls")
        print("===================================")
        print("Você escolheu o {}".format(carros[id][0]))
        print("===================================")
        print("\nPor quantos dias você deseja alugar?")
        dias = int(input())
        os.system("cls")
        print("===================================")
        print("Você escolheu {} dias".format(dias))
        print("Valor total do aluguel: R${}".format(carros[id][1] * dias))
        print("===================================")
        print("\nDeseja alugar?")
        print("[0] - SIM")
        print("[1] - NÃO")
        conf = int(input())
        if conf == 0:
            os.system("cls")
            
            print("Parabéns, você alugou um carro!")
            print("================================")
            print("Modelo: {} | Dias alugados: {} | Total: R${}".format(carros[id][0], dias, carros[id][1] * dias))
            print("=================================")
            alugados.append(carros.pop(id))            
            
    elif op == 2:
        if len(alugados) == 0:
            os.system("cls")
            print("Voce não possui nenhum carro para devolver!")
            print("Encerrando...")
        else:
            os.system("cls")
            imprimirCarros(alugados)
            print("==========")
            print("Qual carro você deseja devolver?")
            cod = int(input())
            print("================")
            print("Você devolveu o {}".format(alugados[cod][0]))
            print("================")
            carros.append(alugados.pop(cod))

        

    print("\n===============================")
    print("[0] - VOLTAR AO MENU PRINCIPAL")
    print("[1] - SAIR")
    print("===============================")
    if int(input()) == 1:
        os.system("cls")
        print("Encerrando...")
        break

