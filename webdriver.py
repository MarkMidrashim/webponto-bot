#!-*- conding: utf8 -*-
#coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from commons import Commons

import subprocess
from dotenv import dotenv_values


class WebDriver:
	"""Configuração do WebDriver para utilização no Selenium com BOT"""

	def __init__(self, headless=True):
		self.env = dotenv_values(".env")
		self.pathDownload = self.env.get("PATH_DOWNLOAD")
		self.headless = headless
		self.commons = Commons()

	def setOptions(self):
		"""
		Método responsável por definir as opções do browser no webdriver
		:return:
		"""
		options = Options()
		options.add_argument("--disable-notifications")
		options.add_argument('--no-sandbox')
		options.add_argument('--verbose')
		options.add_experimental_option("prefs", {
			"download.default_directory": self.pathDownload,
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False,
			"profile.default_content_setting_values.automatic_downloads": 1
		})
		options.add_argument('--disable-gpu')
		options.add_argument('--disable-software-rasterizer')

		if self.headless:
			options.add_argument('--headless')

		return options

	def versionGoogle(self):
		"""
		Método responsável por verificar a versão do google chrome
		Válido somente para OS Windows
		:return:
		"""
		version = subprocess.check_output(
			r'wmic datafile where name="{}" get Version /value'.format(self.env.get("PATH_CHROME")),
			shell=True
		).decode('utf-8').strip()

		try:
			if self.env.get("BROWSER_VERSION") in version:
				driver = "./drivers/chromedriver"
		except Exception as e:
			self.commons.logg(e, 3)
		else:
			return driver

	def open(self):
		"""
		Método reponsável por inicializar o webdriver
		:return:
		"""
		params = {
			'cmd': 'Page.setDownloadBehavior',
			'params': {
				'behavior': 'allow',
				'downloadPath': self.pathDownload
			}
		}

		self.driver = webdriver.Chrome(executable_path=self.versionGoogle(), chrome_options=self.setOptions())
		self.driver.maximize_window()
		self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
		self.driver.execute("send_command", params)
		return self.driver

	def close(self):
		"""
		Método responsável por fechar o webdriver
		:return:
		"""
		self.driver.quit()