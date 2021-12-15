#from  random  import  randint  # IMPORTAR FUNÇÃO QUE GERA NUMERO ALEATÓRIO

from random import randint
numero=randint(1,100)

print("----ACERTE O NÚMERO----")
def chutes():
    chute=int(input(print("Digite um número de 1 à 100: ")))
    try:
        if -1<chute<101:
            if chute<numero:
                print("Chute um numero ->MAIOR<-")
            elif chute>numero:
                print("Chute um número ->MENOR<-")
            else:
                print("Você ACERTOU... Parabéns!!!")
            return chute
    except ValueError:
        print("\nErro: digite uma opção válida!")
        chutes()

while True:
    chutes()
