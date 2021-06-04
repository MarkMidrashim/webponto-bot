#!-*- conding: utf8 -*-
#coding: utf-8

from bot import Bot
from commons import Commons
from tinydb import Query

from dotenv import dotenv_values
from datetime import datetime
import time, sys


class Main(Bot):
	""" Lógica para execução do BOT """

	def __init__(self):
		self.env = dotenv_values(".env")
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
					Marking = Query()
					result = bot.connectionWithDatabase.search(Marking.date == currenttimestamp.strftime("%d/%m/%Y %H:%M"))

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
						self.commons.logg("An appointment has already been made at this time {}".format(currenttimestamp.strftime("%H:%M")))
						time.sleep(30)
				else:
					self.commons.logg("It is not time {}".format(currenttimestamp.strftime("%H:%M")))
					time.sleep(30)
			else:
				self.commons.logg("It is not week day".format(currenttimestamp.strftime("%H:%M")))
				sys.out()


if __name__ == '__main__':
	try:
		main = Main()
		main.start()
	except Exception as e:
		print("-- Main Error --")
		print(e)