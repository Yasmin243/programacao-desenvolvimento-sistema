import random
numero_secreto = random.randint (1,10)

tentativas = 0
max_tentativas = 3

print("Bem vindo ao jogo")
print("Tente adivinhar o numero entre 1 a 10")

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite:"))
    tentativas +=1

    if palpite == numero_secreto:
        print("Parabéns, voce acertou!")

    elif palpite < numero_secreto:
        print("Muito baixo,tente novamente.")
    else:
        print("Muito alto. Tente novamente.")
     #encerramento
    if palpite != numero_secreto:
        print ("Fim do jogo. O mumero era:" ,numero_secreto)

