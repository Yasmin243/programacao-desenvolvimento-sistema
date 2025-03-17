import random


print("*********************************")
print("bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 10)
total_de_tentativas = 0
pontos = 1000
#print(numero_secreto)

print("Qual o nível de dificuldade?")
print("[1] Fácil [2] Médio [3] Difícil")
nivel = int(input("Defina um nível: "))

if(nivel == 1):
    total_de_tentativas = 10
elif(nivel == 2):
    total_de_tentativas = 5
else:
    total_de_tentativas = 3



for rodadas in range (1, total_de_tentativas + 1):
    print("tentativas {} de {}".format(rodadas, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    #print("você digitou", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute> 10):
        print("você deve digitar um número entre 1 e 10")
        continue

    acertou = (chute == numero_secreto)
    maior   = (chute > numero_secreto)
    menor   = (chute < numero_secreto)

    if(acertou):
        print("você acertou e fez {} pontos :)".format(pontos))
        break

    else:
        if(maior):
            print("você errou! o seu chute foi maior que o numero secreto")
        elif(menor):
            print("você errou! o seu chute foi menor que o numero secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    print("fim do jogo!")