import os
from classeMinado import *

print("\t\t------- Jogo Campo Minado -------")

linha = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))
minas = int(input('Digite a qtd de Minas: '))

campoMinado = CampMinado(linha,colunas,minas)
campoComMinas = []
campoSemMinas = []

campoComMinas = campoMinado.criaCampo(campoComMinas)
campoSemMinas = campoMinado.criaCampo(campoSemMinas)
campoComMinas = campoMinado.poeMinas(campoComMinas)


game = True
cont = 0
while game:
    campoMinado.mostraCampoSMinas(campoSemMinas)

    print("\nJogadas: %d" % cont)
    cont += 1

    hitL = int(input('Escolha a linha: '))
    hitC = int(input("Escolha a Coluna: "))

    game = campoMinado.escolha(hitL, hitC, campoSemMinas, campoComMinas)
    if game:
        os.system("cls")
        continue
    else:
        print("\n---- \a Você Acertou uma mina em %d jogadas\n" %cont)
        campoMinado.mostraCampoComMinas(campoComMinas)
        break

print('------ Obrigado por jogar -----')


