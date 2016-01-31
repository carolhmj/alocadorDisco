#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Classe abstrata do alocador de disco"""
class AlocadorDisco(object):
	def __init__(self, referencias, nPag):
		self.referencias = referencias
		self.nPag = nPag
	def executar(self):
		"""Aqui executamos o algoritmo de alocação"""
		pass
	def escreverInformacoes(self, saida):
		"""Aqui escrevemos em um arquivo o resultado da execução"""
		arq = open(saida, "a+")
		formString = "Número de falhas de página: {:d} \n".format(self.nPageFaults)
		arq.write(formString)
		formString = "Razão entre troca e execução: {:f} \n".format((self.nPageFaults*0.0002)/(self.nPageFaults*0.0002+self.nTotalReferencias*2))
		arq.write(formString)
		arq.write("Alocações: \n")
		for hist in self.historiaPaginas:
			arq.write(str(hist))
			arq.write("\n")
		arq.close()	