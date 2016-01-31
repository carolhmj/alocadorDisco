#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


"""Leitor de inputs"""
class inputReader():
	def __init__(self,arquivo):
		self.arquivo = arquivo

	def executar(self): 
		r = []
		line = ""
		try:
		    reader = open(self.arquivo, 'r')
		    line = reader.readline()	
		finally:
			reader.close()
			r = line.split(',')
			r = [int(i) for i in r]
			return r
