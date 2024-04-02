import re
import time

def again():
	respond = input("Scan again? [yes/no]:\n")
	respond = respond.lower()
	if respond == "yes":
		return True
	else:
		return False
def extractor():
	def txt():
		def extractednums(text):
			regex = r"(\+\d{1,4}\s?)?((\(\d{3}\)|\d{3}))[\s.-]?\d{3}[\s.-]?\d{3,4}( x\d{1,5})"
			phonelist = re.findall(regex,text)
			return phonelist
		text = input("Paste text containing phone numbers here")
		text = text.upper()
		phones = extractednums(text)
		print("Extracted Phone numbers: \n")
		for phone in phones:
			time.sleep(1)
			print(phone)
			time.sleep(1)
			print("Successfully done!")
	def url():
		def extractednums(url):
			import requests
			from bs4 import BeautifulSoup
			response = requests.get(url)
			soup = BeautifulSoup(response.text,'html.parser')
			regex = r"(\+\d{1,4}\s?)?((\(\d{3}\)|\d{3}))[\s.-]?\d{3}[\s.-]?\d{3,4}( x\d{1,5})"
			phonelist = re.findall(regex,str(soup))
			return phonelist
		url = input("Paste Url Containing phone numbers here: \n")
		phones = extractednums(url)
		print("Extracted phone numbers:\n")
		for phone in phones:
			time.sleep(1)
			print(phone)
			time.sleep(1)
			print("Successfully done!")
	user_input = input("""
	How do you wish to extract the phone numbers:
	1: Through text
	2: Through a url
	[reply with text/url]
	""")
	user_input = user_input.lower()
	if user_input == "text":
		txt()
		again()
		while again():
			extractor()
	elif user_input == "url":
		url()
		again()
		while again():
			extractor()
	else:
		print("That is invalid")
		again()
		while again():
			extractor()
extractor()
while again():
	extractor()
		
