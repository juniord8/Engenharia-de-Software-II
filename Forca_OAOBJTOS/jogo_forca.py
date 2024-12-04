
import random
from exibidor_de_palavra import ExibidorDePalavra



def carregar_palavras():
    with open('palavras.txt', 'r') as f:
        palavras = [linha.strip() for linha in f.readlines()]
    return palavras


def mostrar_ranking():
    try:
        with open('ranking.txt', 'r') as f:
            ranking = f.readlines()
            if ranking:
                print("\nRanking:")
                for i, linha in enumerate(ranking, start=1):
                    nome, pontos = linha.strip().split(", ")
                    print(f"{i}. {nome} - {pontos} tentativas")
            else:
                print("\nRanking vazio!")
    except FileNotFoundError:
        print("\nRanking não encontrado, criando novo ranking.")
        

def salvar_ranking(nome, tentativas):
    with open('ranking.txt', 'a') as f:
        f.write(f"{nome}, {tentativas}\n")


def jogar():
    palavras = carregar_palavras()  
    palavra_secreta = random.choice(palavras)  
    exibidor = ExibidorDePalavra(palavra_secreta)

    tentativas = 6
    letras_adivinhadas = []

    print("Bem-vindo ao jogo da Forca!")

    
    nome_jogador = input("Qual o seu nome? ").strip()

    while tentativas > 0:
        print("\nPalavra: ", exibidor.exibir())
        letra = input(f"Você tem {tentativas} tentativas restantes. Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra!")
            continue
        
        letras_adivinhadas.append(letra)
        exibidor.adicionar_letra_adivinhada(letra)

        if letra not in palavra_secreta:
            tentativas -= 1
            print(f"A letra '{letra}' não está na palavra!")
        
        if "_" not in exibidor.exibir():
            print(f"\nParabéns, {nome_jogador}, você acertou a palavra '{palavra_secreta}'!")
            break
    else:
        print(f"\n{nome_jogador}, você perdeu! A palavra era '{palavra_secreta}'.")

    #
    salvar_ranking(nome_jogador, 6 - tentativas)
    mostrar_ranking()

if __name__ == "__main__":
    jogar()
