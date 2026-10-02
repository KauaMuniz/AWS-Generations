import os
import operacoes


controlador = 0

while True: 
    print("=========== CALCULADORA =========== ")

    print(''' 
        [1] Adição
        [2] Subtração
        [3] Divsão
        [4] Multiplicação
    ''')

    try:
        controlador = int(input("Digite a opção que deseja realizar: "))
    except ValueError:
        print("Erro: Digitou uma opção inválida, o campo só aceita números!")
    os.system('cls')

    match controlador:
        case 1:
            print("=== ADIÇÃO ===")   
            x = float(input("Digite o valor do primeiro número: ")) 
            y = float(input("Digite o valor do segundo número: "))
            total = operacoes.adicao(x,y)   
            print(f"O valor da soma é de: {total}")

        case 2: 
            print("=== SUBTRAÇÃO ===")
            x = float(input("Digite o valor do primeiro número: ")) 
            y = float(input("Digite o valor do segundo número: "))
            total = operacoes.subtracao(x,y)   
            print(f"O valor da subtração é de: {total}")
            
        case 3 :
            total = None
            while total is None:
                print("=== Divsão === ")
                x = float(input("Digite o valor do primeiro número: ")) 
                y = float(input("Digite o valor do segundo número: "))
                total = operacoes.divisao(x,y) 
            print(f"O valor da divisão é de: {total}")
            print("")

        case 4 : 
            print("=== Multiplicação ===")
            x = float(input("Digite o valor do primeiro número: ")) 
            y = float(input("Digite o valor do segundo número: "))
            total = operacoes.multiplicacao(x,y)   
            print(f"O valor da multiplicação é de: {total}")    
        case _ :
            print("Opção inválida!")

    print()

    controlador = int(input("Digite [5] para sair ou [6] para voltar ao menu: "))

    if controlador == 5:
        os.system("cls")
        print("Calculadora encerrada")

        break




