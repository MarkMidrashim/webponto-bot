#!-*- conding: utf8 -*-
#coding: utf-8

from bot import Bot
from tinydb import Query

from dotenv import dotenv_values
from datetime import datetime
import time

class Main(Bot):
	""" Lógica para execução do BOT """

	def __init__(self):
		self.env = dotenv_values(".env")
		self.viewBrowser = self.env.get("VIEW_BROWSER")

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
					result = bot.db.search(Marking.date == currenttimestamp.strftime("%d/%m/%Y %H:%M"))

					if len(result) == 0:
						print("-- INIT BOT --")

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

						print("-- FINISHED BOT --")
					else:
						print("-- {}, AN APPOINTMENT HAS ALREADY BEEN MADE AT THIS TIME --".format(
							currenttimestamp.strftime("%H:%M")))
						time.sleep(30)
				else:
					print("-- {}, IT IS NOT TIME --".format(currenttimestamp.strftime("%H:%M")))
					time.sleep(30)
			else:
				print("-- IT IS NOT WEEK DAY --")
				time.sleep(60)


if __name__ == '__main__':
	try:
		main = Main()
		main.start()
	except Exception as e:
		print("-- ERROR --")
		print(e)