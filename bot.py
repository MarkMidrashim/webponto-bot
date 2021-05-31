#!-*- conding: utf8 -*-
#coding: utf-8

from webdriver import WebDriver
from tinydb import TinyDB, Query

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import dotenv_values
import time

class Bot:
    """Actions e methods para realizar o propósito do BOT"""

    def __init__(self, viewBrowser, datetime):
        self.env = dotenv_values(".env")
        self.db = TinyDB(self.env.get("PATH_AND_DBNAME"))
        self.viewBrowser = viewBrowser
        self.datetime = datetime

    def start(self):
        """
        Método responsável por inicializar o BOT
        :return:
        """
        self.driver = WebDriver(self.viewBrowser).open()

    def close(self):
        """
        Método resposável por finalizar o BOT
        :return:
        """
        self.driver.close()

    def login(self):
        """
        Método responsável por realizar o login no portal de apontamento de hora
        :return:
        """
        try:
            time.sleep(1)
            self.driver.get(self.env.get("URL"))
            self.driver.implicitly_wait(5)
        except Exception as e:
            print("-- ERROR --")
            print("{}".format(e))
            return None

        time.sleep(1)
        self.driver.find_element(By.ID, 'CodEmpresa').send_keys(self.env.get("COMPANY"))
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'requiredusuario').send_keys(self.env.get("REGISTRATION"))
        self.driver.find_element(By.ID, 'requiredsenha').send_keys(self.env.get("PASSWD"))
        self.driver.find_element(By.CLASS_NAME, 'BotaoAchatado').click()

        self.navigateToMenu()

    def navigateToMenu(self):
        """
        Método responsável por realizar a navegação no menu e abrir popup de marcação
        :return:
        """
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.ID, 'menu2')).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element(
            By.CSS_SELECTOR,
            'a[class="MenuItem"][onmouseover*=MudarStatus]')
        ).click().perform()

    def checkIfItsTimeToMarking(self, hour=None):
        """
        Método responsável por verificar se a hora informada pertence aos horários de marcação
        :param hour:
        :return:
        """
        if hour is None:
            if self.datetime.strftime("%H:%M") == self.env.get("START_SHIFT") or \
                    self.datetime.strftime("%H:%M") == self.env.get("LUNCH_OUT") or \
                    self.datetime.strftime("%H:%M") == self.env.get("BACK_LUNCH") or \
                    self.datetime.strftime("%H:%M") == self.env.get("END_SHIFT"):
                return True
            else:
                return False
        else:
            if hour == self.env.get("START_SHIFT") or \
                    hour == self.env.get("LUNCH_OUT") or \
                    hour == self.env.get("BACK_LUNCH") or \
                    hour == self.env.get("END_SHIFT"):
                return True
            else:
                return False

    def checkingMarkingHour(self):
        """
        Método responsável por capturar a hora do portal e verificar se está de acordo com o horário de apontamento
        :return:
        """
        hour = self.driver.find_element(By.CSS_SELECTOR, 'input[name="hora"]').get_attribute('value')
        return self.checkIfItsTimeToMarking(hour)

    def setMarking(self):
        """
        Método responsável por realizar a marcação do ponto no portal
        :return:
        """
        try:
            self.driver.find_element(By.CLASS_NAME, 'BotaoAchatado').click()
            data = {"date": self.datetime.strftime("%d/%m/%Y %H:%M"), "set": True}
            self.db.insert(data)
        except Exception as e:
            data = {"date": self.datetime.strftime("%d/%m/%Y %H:%M"), "set": False}
            self.db.data(dictionary=data)

    def closeMarkingWindow(self):
        """
        Método responsável por fechar o popup de marcação
        :return:
        """
        try:
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, 'button[value*=Fechar]').click()
            self.driver.close()
        except Exception as e:
            self.driver.close()

    def switchWindowBetweenMainAndMarking(self, whichWindow):
        """
        Método responsável por realizar a troca do webdriver entre as janelas do portal
        :param whichWindow:
        :return:
        """
        time.sleep(2)
        main_window = self.driver.window_handles[0]

        if len(self.driver.window_handles) >= 2:
            new_window = self.driver.window_handles[1]

        if whichWindow == "marking":
            self.driver.switch_to_window(new_window)
        else:
            self.driver.switch_to_window(main_window)

    def logout(self):
        """
        Método responsável por realizar o logout do portal
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="LinkOpcao"][href="../saida.asp"]').click()
