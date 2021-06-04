#!-*- conding: utf8 -*-
# coding: utf-8

from src.commons import Commons

from tinydb import TinyDB
from dotenv import dotenv_values
import os


class Database:
    """Classe responsável por gerenciar o Database"""

    def __init__(self, currenttimestamp):
        self.env = dotenv_values("{}\\.env".format(os.path.abspath(os.getcwd())))
        self.commons = Commons()
        self.currenttimestamp = currenttimestamp

    def open(self):
        """
        Método responsável por abrir e criar a conexão com o database
        :return:
        """
        try:
            database = TinyDB(
                "{}\\{}.json".format(self.env.get("PATH_DATABASE"), self.currenttimestamp.strftime("%d%m%Y"))
            )
        except Exception as e:
            self.commons.logg(e, 3)
        else:
            return database
