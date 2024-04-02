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
	try:
		def extractednums(url):
			import requests
			from bs4 import BeautifulSoup
			response = requests.get(url)
			soup = BeautifulSoup(response.txt,'html.parser')
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
	except Exception as e:
		print("Something went wrong.")
		print(f"Here is what went wrong: ({e})")
extractor()
while again():
	extractor()
		
