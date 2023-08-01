def soma():
    n = int(input("Entre com o numero de termos da soma: "))
    soma = 0.0
    soma = float(input("Entre com o primeiro termo da soma: "))
    for i in range (n-1):
        x = float(input("Entre com o proximo termo da soma: "))
        soma += x
    return soma
def subtracao():
    n = int(input("Entre com o numero de termos da subtracao: "))
    subtracao = float(input("Entre com o maior termo da subtracao: "))
    for i in range (n-1):
        x = float(input("Entre com o termo que subtrai: "))
        subtracao -= x
    return subtracao
def multiplicacao():
    n = int(input("Entre com o numero de termos da multiplicacao: "))
    multiplicacao = float(input("Entre com o primeiro termo da multiplicacao: "))
    for i in range (n-1):
        x = float(input("Entre com o proximo termo da multiplicacao: "))
        multiplicacao *= x
    return multiplicacao
def divisao():
    n = int(input("Entre com o numero de divisores: "))
    divisao = float(input("Entre com o dividendo: "))
    for i in range (n):
        x = float(input("Entre com o proximo divisor: "))
        divisao /= x
    return divisao
def potencia():
    x = float(input("Entre com a base: "))
    y = int(input("Entre com o expoente: "))
    potencia = 1
    if y == 0:
        return 1
    else:
        for i in range (y):
            potencia *= x
        return potencia
def potenciaraiz(base, expoente):
    potencia1 = base
    for i in range (expoente-1):
        potencia1 *= base
    return potencia1
def raiz():
    x = int(input("Entre com o radicando: "))
    y = int(input("Entre com o indice: "))
    for i in range (x):
        if potenciaraiz(i,y) == x:
            return i
    return "Não existe raiz inteira"
def log():
    y = int(input("Entre com a base do log: "))
    x = int(input("Entre com o logaritmando: "))
    if x == y:
        return 1
    elif x == 1:
        return 0
    elif y == 1:
        if x == 1: 
            return 0
        else: 
            return "Não é possível efetuar esse log"
    else:
        for i in range (x):
            if potenciaraiz(y, i) == x:
                return i
            elif potenciaraiz(y, i) > x:
                return "Não foi possível efetuar esse log, dado a baixa complexidade do sistema de cálculo"

def calculadora():
    operacao = input("Qual a operação desejada (soma, subtracao, multiplicacao, divisao, potencia, raiz, log): ")
    operacao = operacao.lower()
    if operacao == 'soma':
        return soma()
    elif operacao == 'subtracao':
        return subtracao()
    elif operacao == 'multiplicacao':
        return multiplicacao()
    elif operacao == 'divisao':
        return divisao()
    elif operacao == 'potencia':
        return potencia()
    elif operacao == 'raiz':
        return raiz()
    elif operacao == 'log':
        return log()

if __name__== "__main__":
    x = 1
    while x == 1:
        x = int(input("Digite o comando (1 para calculadora e 0 para sair): "))
        if x == 0:
            break
        print (calculadora())
    print ("Programa encerrado")