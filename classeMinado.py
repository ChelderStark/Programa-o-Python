import random

class CampMinado:
    def __init__(self, linha, coluna, minas):
        self.linha = linha
        self.coluna = coluna
        self.minas = minas

    def criaCampo(self, matriz):
        for i in range(0, self.linha):
            linha = []
            for j in range(0,self.coluna):
                linha.append(0)

            matriz.append(linha)
        return matriz

    def poeMinas(self, matriz):
        for i in range(1,self.minas+1):
            p = random.randint(0,self.linha-1)
            q = random.randint(0,self.coluna-1)
            if matriz[p][q] != '*':
                matriz[p][q] = '*'

        return matriz

    def mostraCampoSMinas(self, campo):
        cont = 1
        col = "\a| "
        for i in range(1, self.coluna + 1):
            col += ("\t%s" % i)
        print(col)
        for i in campo:
            linha = i
            l1 = ("%d| " % cont)
            for j in linha:
                l1 += ("\t%s" % j)
            print(l1)
            cont += 1

    def mostraCampoComMinas(self, campo):
        cont = 1
        col = "\a| "
        for i in range(1, self.coluna + 1):
            col += ("\t%s" % i)
        print(col)
        for i in campo:
            linha = i
            l1 = ("%d| " % cont)
            for j in linha:
                l1 += ("\t%s" % j)
            print(l1)
            cont += 1


    def escolha(self,linha, coluna, matrizB, matrizM):
        if matrizM[linha-1][coluna-1] == "*":
            return False
        else:
            matrizM[linha-1][coluna-1] = "#"
            matrizB[linha-1][coluna-1] = "#"
            return True
