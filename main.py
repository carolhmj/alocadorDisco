#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from alocadorLRU import AlocadorLRU
from alocadorFIFO import AlocadorFIFO
from alocadorOtimo import AlocadorOtimo
from inputReader import inputReader

class Escalonador():

	def __init__(self, args):
		self.args = args

	def executar(self):
		try:
			f = self.args[1]
		except IndexError:
			print "Número de argumentos incorreto\nFinalizando..."

		try:
			reader = inputReader(f)
		except IOError:
			print "O arquivo de entrada não existe.\nFinalizando..."
			sys.exit()

		listacsv = reader.executar()
		LRU = None
		FIFO = None
		OPT = None
		try: 
			LRU = AlocadorLRU(listacsv, int(self.args[2]))
			FIFO = AlocadorFIFO(listacsv, int(self.args[2]))
			OPT = AlocadorOtimo(listacsv, int(self.args[2]))
		except IndexError:
			print "Especifique o número de páginas.\nFinalizando..."
			sys.exit()

		saidaN = "saida.txt"
		saida = open(saidaN, 'w')
		saida.close()

		if (LRU and FIFO and OPT):
			LRU.executar()
			FIFO.executar()
			OPT.executar()
			FIFO.escreverInformacoes(saidaN)
			LRU.escreverInformacoes(saidaN)
			OPT.escreverInformacoes(saidaN)		

if __name__ == "__main__":
     e = Escalonador(sys.argv)
     e.executar()