import os
from classeMinado import *

os.system("color 0E")

game = True
cont = 0

campoMinado = CampMinado()
campoComMinas = []
campoSemMinas = []

print("\t\t------- Jogo Campo Minado -------")
flag = campoMinado.verificaArq()

if flag == True:
    print("Existe um jogo em abeto...")
    cont, campoComMinas, campoSemMinas = campoMinado.carregaJogo()
else:
    linha = int(input('Digite a quantidade de linhas: '))
    colunas = int(input('Digite a quantidade de colunas: '))
    minas = int(input('Digite a qtd de Minas: '))
    campoMinado.insereDados(linha, colunas, minas)

    campoComMinas = campoMinado.criaCampo(campoComMinas)
    campoSemMinas = campoMinado.criaCampo(campoSemMinas)
    campoComMinas = campoMinado.poeMinas(campoComMinas)


while game:
    campoMinado.mostraCampoSMinas(campoSemMinas)

    print("\nJogadas: %d" % cont)
    cont += 1

    #jogas de linha e coluna, e são armazenadas nas variáveis
    hitL = int(input('Escolha a linha: '))
    hitC = int(input("Escolha a Coluna: "))

    game = campoMinado.escolha(hitL, hitC, campoSemMinas, campoComMinas)
    if game:
        os.system("cls")
        campoMinado.salvar(str(cont), campoComMinas)
        continue
    else:
        os.system("color 0C")
        print("\n---- \a Você Acertou uma mina em %d jogadas\n" %cont)
        campoMinado.mostraCampoComMinas(campoComMinas)
        campoMinado.zeraArquivo()
        break

print('------ Obrigado por jogar -----')


