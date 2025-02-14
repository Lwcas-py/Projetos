import os

def calcular ():
    print("Operadores.\na : Adição\ns : Subtração\nm : Multiplicação\nd : Divisão\np : Potenciação\n")
    op=input("Insira aqui o Operador:").lower() #((Comando lower bota tudo em lowercase))
    x=float(input("insira aqui um número:"))
    y=float(input("Insira aqui o outro número:"))
    if op=="a":
        return x + y
    elif op=="s":
        return x - y
    elif op=="m":
        return x * y
    elif op=="d":   
        while y == 0:
                print("Erro, Divisão por Zero não é possivel, insira novamente os números.")
                x=float(input("insira aqui um número:"))
                y=float(input("Insira aqui o outro número:"))
        return x / y
    elif op=="p":
        return x ** y
os.system('cls' if os.name == 'nt' else 'clear')    
print("Bem vindo á calculadora em python!")
result=calcular()
print("=============================")
print("O seu resultado é: {}".format(result))
print("_____________________________")
while True:
    ans=input("Você deseja continuar calculando? (sim=S/não=N)").lower()
    if ans=="s":
        print("___________________________")
        print("Continuando o programa...")
        result=calcular()
        print("=============================")
        print("O seu resultado é: {}".format(result))
        print("_____________________________")
    else:
        print("_____________________________")
        print("Encerrando o programa...")
        break