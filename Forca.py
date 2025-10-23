#forca
import random
print(f"Vamos brincar de forca, a dica é frutas!\n")

palavras= ["MAÇA", "BANANA", "UVA", "LARANJA", "ABACAXI", "LIMAO", "PERA"]


# Escolhe uma palavra aleatória
palavra = random.choice(palavras)

# Inicializa as variáveis do jogo
letras_adivinhadas = []
tentativas = 6

print("Bem-vindo ao Jogo da Forca!\n")

# Loop principal do jogo
while tentativas > 0:
    # Mostra a palavra com _ para letras não adivinhadas
    exibicao = ''
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '

    print('\nPalavra:', exibicao.strip())

    # Verifica se o jogador venceu
    if all(letra in letras_adivinhadas for letra in palavra):
        print("\n Parabéns! Você adivinhou a palavra:", palavra)
        break

    # Pede uma letra
    palpite = input("Digite uma letra: ").upper()

    if not palpite.isalpha() or len(palpite) != 1:
        print(" Por favor, digite apenas UMA letra.")
        continue

    if palpite in letras_adivinhadas:
        print(" Você já tentou essa letra.")
        continue

    # Verifica se a letra está na palavra
    if palpite in palavra:
        print(" Boa! A letra está na palavra.")
        letras_adivinhadas.append(palpite)
    else:
        print(" A letra não está na palavra.")
        tentativas -= 1
        print(f"Você ainda tem {tentativas} tentativa(s).")

# Se acabar as tentativas
if tentativas == 0:
    print("\n Fim de jogo! A palavra era:", palavra)
