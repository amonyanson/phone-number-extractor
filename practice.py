#for practice
import re
import time
def textextractor():
	def extractednums(text):
		pattern = r'\b(?:\+?254|0)?(?:7|1\d)\d{8}\b' #Kenya
		#\b is a word boundary
		#\+?254 matches optional country code (+254)
		# 0? matches optional leading 0
		#(?:7|1\d) matches either 7 or 1 followed by a digit
		# \d {8} matches 8 digits (total 10 digits including the initial 0 or +254)
		matches = re.findall(pattern,text)
		return matches
	time.sleep(0.5) 
	text = input("Paste text containing phone numbers here:\n") 
	phones = extractednums(text)
	time.sleep(0.5)
	print("Extracted Phone numbers:\n") 
	time.sleep(0.5) 
	for key in phones:
		time.sleep(1)
		print(key)
		time.sleep(1)
		print("Successfully done!")
def urlextractor():
	def extractednums(url):
		import requests
		from bs4 import BeautifulSoup
		response = requests.get(url)
		soup = BeautifulSoup(response.text,'html.parser')
		    pattern = r'\b(?:\+?254|0)?(?:7|1\d)\d{8}\b'
		    # \b is a word boundary
		    # \+?254 matches optional country code (+254)
		    # 0? matches optional leading zero
		    # (?:7|1\d) matches either 7 or 1 followed by a digit
		    # \d{8} matches 8 digits (total 10 digits including the initial 0 or +254)
		    matches = re.findall(pattern, text)
		    return matches
		time.sleep(0.5)
		url = input("Paste url containing phone numbers here:\n")
		url = url.lower()
		phones = extractednums(url)
		time.sleep(0.5)
		print("Extracted Phone numbers:\n")
		time.sleep(0.5)
		for key in phones:
			time.sleep(1)
			print(key)
			time.sleep(1)
			print("Successfully done!")
def newgame():
	user_input = input("""Hello, how do you wish to extract target phone numbers?
1: Through text
2: Through a url
reply with [text or url]:
""")
	if user_input == "text":
		time.sleep(1)
		textextractor()
	elif user_input == "url":
		time.sleep(1)
		urlextractor()
	else:
		print("invalid user input")
def again():
	respond = input("Scan again:\n[yes/no]")
	respond = respond.lower()
	if respond == "yes":
		return True 
	else:
		return False
newgame()
while again():
	newgame()
