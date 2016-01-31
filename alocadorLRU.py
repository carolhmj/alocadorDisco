#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
from alocador import AlocadorDisco

"""Alocador LRU de disco"""
class AlocadorLRU(AlocadorDisco):
	"""docstring for AlocadorLRU"""
	def __init__(self, referencias, nPag):
		super(AlocadorLRU, self).__init__(referencias, nPag)
		#print self.referencias
		self.nome = "ALOCADOR LRU"
	def executar(self):
		
		quantidadePaginasReferenciadas = len(Counter(self.referencias).keys())
		#print quantidadePaginasReferenciadas
		#Guarda o instante da referência mais recente de cada página 
		referenciaMaisRecente = [0 for i in range(quantidadePaginasReferenciadas)]
		#Guarda as páginas que estão em memória
		paginasMemoria = []
		#Conta o número total de page faults
		nPageFaults = 0
		#História de alocação das páginas
		historiaPaginas = []
		timeCounter = 0
		for ref in self.referencias:
			#print "REF: " + str(ref)
			timeCounter = timeCounter + 1
			referenciaMaisRecente[ref-1] = timeCounter

			#As referências iniciais todas causam page fault
			if timeCounter <= self.nPag:
				nPageFaults = nPageFaults + 1
				paginasMemoria.append(ref)
			else:
				if ref not in paginasMemoria:
					nPageFaults = nPageFaults + 1
					#Página que vai ser substituída
					LRUPage = 0
					for i in range(1, self.nPag):
						if referenciaMaisRecente[paginasMemoria[i]-1] < referenciaMaisRecente[paginasMemoria[LRUPage]-1]:
							LRUPage = i
					#print "LRUPAGE: " + str(LRUPage)
					paginasMemoria[LRUPage] = ref

			print "PAGINASMEM: " + str(paginasMemoria)
			historiaPaginas.append(paginasMemoria[:])
			print "HISTORIAPAGINAS: " + str(historiaPaginas)

		self.nPageFaults = nPageFaults
		self.historiaPaginas = historiaPaginas
		self.nTotalReferencias = len(self.referencias) 		

