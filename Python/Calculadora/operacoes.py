def adicao(x,y):
    total =  x + y 
    return total

def subtracao(x,y):
    total = x -y
    return total

def multiplicacao(x,y):
    total = x * y
    return total

def divisao(x,y):
    try :
        total = x / y
        return total
    except ZeroDivisionError:
        print("Não é possivel fazer divisão por zero, tente novamente com outros valores!!")
        return None

    

