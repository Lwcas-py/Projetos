import os
import random


def play():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("|PEDRA PAPEL TESOURA EM PYTHON|\n(por Lwcas-py)")  
        start_ans = input("Deseja jogar? (s/n): ").strip().lower()

        if start_ans == "s":
            print("O jogo está iniciando...\n")
            return True
        elif start_ans == "n":
            print("Encerrando o jogo...")
            return False
        else:
            print("Opção inválida! Digite 's' para continuar ou 'n' para sair.")


# Vez do jogador, armazena a escolha do jogador.
def playerturn():
    print("------------------------------")
    print("É sua vez, escolha sua jogada!")
    while True:
        try:
            player_choice = int(input("Insira aqui a jogada selecionada (\n |1- Pedra|\n |2- Tesoura|\n |3- Papel|\n "))
            if player_choice in [1, 2, 3]:
                choices = {1: "Pedra", 2: "Tesoura", 3: "Papel"}
                print(f"Você escolheu: {choices[player_choice]}")
                return player_choice  # Retorna a jogada do jogador
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


# Escolha do computador
def computerturn():
    print("------------------------------------")
    print("Agora é a vez do sistema, aguarde...")
    
    computer_choice = random.choice([1, 2, 3])  # Escolha aleatória entre 1, 2 e 3
    choices = {1: "Pedra", 2: "Tesoura", 3: "Papel"}
    print(f"O sistema escolheu: {choices[computer_choice]}")
    
    return computer_choice  # Retorna a jogada do computador


# Determina o resultado do jogo
def gameraw():
    player_choice = playerturn()  # Armazena a jogada do jogador
    computer_choice = computerturn()  # Armazena a jogada do computador

    if player_choice == computer_choice:
        print("----------------\nEmpate!\nOs dois escolheram a mesma opção.")
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        print("----------------\nVocê ganhou!\nParabéns!")
    else:
        print("----------------\nVocê perdeu!\nQue Pena... :(")


# Início do jogo

while play():
    gameraw()
    input("Pressione ENTER para jogar novamente...")

