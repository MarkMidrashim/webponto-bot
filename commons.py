#!-*- conding: utf8 -*-
#coding: utf-8

from dotenv import dotenv_values
from datetime import datetime

import os, time, argparse, sys


class Commons(object):
	"""Métodos comuns para o BOT"""

	def __init__(self):
		self.env = dotenv_values(".env")

	def isEmpty(self, value):
		"""
		Método responsável por verificar se a variável está vazia
		:return:
		"""
		if value:
			return False
		else:
			return True

	def logTypeToString(self, logType=0):
		"""
		Método responsável por verificar o tipo de log
		:param type:
		:return:
		"""
		if logType == 0:
			return "INFO"
		elif logType == 1:
			return "DEBUG"
		elif logType == 2:
			return "WARNING"
		elif logType == 3:
			return "ERROR"
		else:
			return "UNKNOW"


	def logg(self, message="", logType=0):
		"""
		Método responsável por gerar log de execução
		:param message:
		:return:
		"""
		currenttimestamp = datetime.now()

		try:
			f = open("{}\\{}.log".format(self.env.get("PATH_LOG"), currenttimestamp.strftime("%d%m%Y")) , "a")
			f.write("[{0}] {1} - {2}".format(
				currenttimestamp.strftime("%d/%m/%Y %H:%M"),
				self.logTypeToString(logType),
				message
			))
		except IOError as e:
			print("-- ERROR --")
			print(e)
		finally:
			f.close()
