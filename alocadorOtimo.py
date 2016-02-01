from collections import Counter
from alocador import AlocadorDisco

"""Alocador Ótimo de disco"""
class AlocadorOtimo(AlocadorDisco):

	def __init__(self, referencias, nPag):
		super(AlocadorLRU, self).__init__(referencias, nPag)
		#print self.referencias
		self.nome = "ALOCADOR OTIMO"

	def buscarPrimeiraOcorrencia(self,p,t=0):
		for i in range(t,len(self.referencias)):
			if (self.referencias[i] == p):
				return i


	def executar(self):

		quantidadePaginasReferenciadas = len(Counter(self.referencias).keys())

		#Guarda o instante da referência mais recente de cada página 
		#referenciaMaisRecente = [0 for i in range(quantidadePaginasReferenciadas)]

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
			
			#As referências iniciais todas causam page fault
			if timeCounter <= self.nPag:
				nPageFaults = nPageFaults + 1
				paginasMemoria.append(ref)
			else:
				if ref not in paginasMemoria:
					nPageFaults = nPageFaults + 1
					paginaOtima = 0
					for i in range(1, self.nPag):
						if (buscarPrimeiraOcorrencia(paginasMemoria[i],timeCounter) > buscarPrimeiraOcorrencia(paginaMemoria[paginaOtima],timeCounter))
							paginaOtima = i
					paginasMemoria[patinaOtima] = ref


			print "PAGINASMEM: " + str(paginasMemoria)
			historiaPaginas.append(paginasMemoria[:])
			print "HISTORIAPAGINAS: " + str(historiaPaginas)

		self.nPageFaults = nPageFaults
		self.historiaPaginas = historiaPaginas
		self.nTotalReferencias = len(self.referencias) 		
