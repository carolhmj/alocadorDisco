#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from alocadorLRU import AlocadorLRU
from inputReader import inputReader

class Escalonador():

	def __init__(self, args):
		self.args = args

	def executar(self):
		try:
			f = open(self.args[1], 'rt')
		except IOError:
			print "O arquivo de entrada não existe.\nFinalizando..."
			sys.exit()

		reader = inputReader(f)
		listacsv = reader.executar()
		LRU = None
		FIFO = None
		OPT = None
		try: 
			LRU = AlocadorLRU(listacsv, int(self.args[2]))
		except IndexError:
			print "Especifique o número de páginas.\nFinalizando..."
			sys.exit()

		saidaN = "saida.txt"
		saida = open(saidaN, 'w')
		saida.close()

		if (LRU and FIFO and OPT):
			LRU.executar()
			LRU.escreverInformacoes(saidaN)		

if __name__ == "__main__":
     e = Escalonador(sys.argv)
     e.executar()