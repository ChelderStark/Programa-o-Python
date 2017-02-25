from classeMinado import *

print("\t\t------- Jogo Campo Minado -------")

linha = int(input('Diite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))
minas = int(input('Digite a qtd de Minas: '))

campoMinado = CampMinado(linha,colunas,minas)
campoComMinas = []
campoSemMinas = []

campoComMinas = campoMinado.criaCampo(campoComMinas)
campoSemMinas = campoMinado.criaCampo(campoSemMinas)
campoComMinas = campoMinado.poeMinas(campoComMinas)


game = True
while game:
    campoMinado.mostraCampoSMinas(campoSemMinas)
    hitL = int(input('\nEscolha a linha: '))
    hitC = int(input("Escolha a Coluna: "))

    game = campoMinado.escolha(hitL, hitC, campoSemMinas, campoComMinas)
    if game:
        continue
    else:
        print("\n---- \a Você Acertou uma mina!!!\n")
        campoMinado.mostraCampoComMinas(campoComMinas)
        break

print('------ Obrigado por jogar -----')
