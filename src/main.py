#!-*- conding: utf8 -*-
#coding: utf-8

from src.bot import Bot
from src.commons import Commons
from tinydb import Query

from dotenv import dotenv_values
from datetime import datetime
import time, sys, os


class Main(Bot):
	""" Lógica para execução do BOT """

	def __init__(self):
		self.env = dotenv_values("{}\\.env".format(os.path.abspath(os.getcwd())))
		self.viewBrowser = self.env.get("VIEW_BROWSER")
		self.commons = Commons()

	def start(self):
		"""
		Método responsável por conter a lógica de execução do BOT
		:return:
		"""
		while True:
			currenttimestamp = datetime.now()
			bot = Bot(self.viewBrowser, currenttimestamp)

			if 0 <= currenttimestamp.isoweekday() <= 5:
				if bot.checkIfItsTimeToMarking():
					marking = Query()
					result = bot.connectionWithDatabase.search(
						marking.date == currenttimestamp.strftime("%d/%m/%Y %H:%M")
					)

					if len(result) == 0:
						self.commons.logg("INIT BOT")

						bot.start()
						bot.login()
						bot.navigateToMenu()
						bot.switchWindowBetweenMainAndMarking("marking")

						if bot.checkingMarkingHour():
							bot.setMarking()
							bot.closeMarkingWindow()

						bot.switchWindowBetweenMainAndMarking("main")
						bot.logout()
						bot.close()

						self.commons.logg("FINISHED BOT")
					else:
						self.commons.logg(
							"An appointment has already been made at this time {}".format(
								currenttimestamp.strftime("%H:%M")
							)
						)
						time.sleep(30)
				else:
					self.commons.logg("It is not time {}".format(currenttimestamp.strftime("%H:%M")))
					time.sleep(30)
			else:
				self.commons.logg("It is not week day".format(currenttimestamp.strftime("%H:%M")))
				sys.out()