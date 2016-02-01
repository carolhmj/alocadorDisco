#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


"""Leitor de inputs"""
class inputReader():
	def __init__(self,arquivo):
		self.arquivo = arquivo

	def executar(self): 
		r = []
		with open(self.arquivo, 'r') as reader:
			line = reader.readline()
			r = line.split(',')
			r = [int(i) for i in r]
		
		return r
			
