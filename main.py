from alocadorLRU import AlocadorLRU

x = [3,2,1,4,3,2,1]
al = AlocadorLRU(x, 3)
al.executar()
al.escreverInformacoes("saida.txt")