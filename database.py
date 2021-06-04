#!-*- conding: utf8 -*-
# coding: utf-8

from tinydb import TinyDB
from commons import Commons
from dotenv import dotenv_values


class Database:
    """Classe responsável por gerenciar o Database"""

    def __init__(self, currenttimestamp):
        self.env = dotenv_values(".env")
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