#!-*- conding: utf8 -*-
#coding: utf-8

from src.main import Main

if __name__ == '__main__':
	try:
		main = Main()
		print("-- Bot Running --")
		main.start()
	except Exception as e:
		print("-- Main Error --")
		print(e)