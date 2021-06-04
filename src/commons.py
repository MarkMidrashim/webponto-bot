#!-*- conding: utf8 -*-
#coding: utf-8

from dotenv import dotenv_values
from datetime import datetime

import os


class Commons(object):
	"""Métodos comuns para o BOT"""

	def __init__(self):
		self.env = dotenv_values("{}\\.env".format(os.path.abspath(os.getcwd())))

	def isEmpty(self, value):
		"""
		Método responsável por verificar se a variável está vazia
		:param value:
		:return:
		"""
		if value:
			return False
		else:
			return True

	def logTypeToString(self, logType=0):
		"""
		Método responsável por verificar o tipo de log
		:param logType:
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
		:param logType:
		:return:
		"""
		currenttimestamp = datetime.now()

		try:
			file = open("{}\\{}.log".format(self.env.get("PATH_LOG"), currenttimestamp.strftime("%d%m%Y")), "a")
			file.write("[{0}] {1} - {2}\n".format(
				currenttimestamp.strftime("%d/%m/%Y %H:%M"),
				self.logTypeToString(logType),
				message
			))
		except IOError as e:
			print("-- Log Error --")
			print(e)
		finally:
			file.close()
