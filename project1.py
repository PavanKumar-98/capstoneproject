'''Just Ask'''

import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import string
from tabulate import tabulate

'''The dictionary contains the items and the locations where they are present as key: value pairs in the shopping centre'''

shop_items = {"milk" : "End of Aisle 1", "chocolates" : "Aisle 1 section 4", "biscuits" : "Aisle 1 section 3",
"chips" : "Aisle 1 section 2", "bread" : "Aisle 1 section 1","icecream" : "End of Aisle 2",
"soaps": "Aisle 2 section 4", "toothpaste" : "Aisle 2 section 3", "bodywash" : "Aisle 2 section 2",
"shampoo" : "Aisle 2 section 1","softdrinks" : "End of Aisle 3", "spices" : "Aisle 3 section 4",
"readytomix" : "Aisle 3 section 3", "grains" : "Aisle 3 section 2", "flours" : "Aisle 3 section 1",
"cleaningitems" : "Aisle 4 section 4", "liquids" : "Aisle 4 section 3", "detergents" :"Aisle 4 section 2", "disinfectents" : "Aisle 4 section 1" }

num = 1
cart = [] 
#cart is used to show what the user has bought whie checking out

def assistant_speaks(output): 
	global num 
  
	# num to rename every audio file  
	# with different name to remove ambiguity 
	num += 1
	print("Friday : ", output) 
  
	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3 " 
	toSpeak.save(file) 
	  
	# playsound package is used to play the same file. 
	playsound.playsound(file, True)  
	#removes the saved file 
	os.remove(file) 


def get_audio(): 
  
	rObject = sr.Recognizer() 
	audio = '' 
	while True:  
		with sr.Microphone() as source: 
			print("Speak...") 
			  
			# recording the audio using speech recognition 
			audio = rObject.listen(source, phrase_time_limit = 5)  
		print("Stop.") # limit 5 secs 
	  
		try: 
	  
			text = rObject.recognize_google(audio, language ='en-US') 
			print("You : ", text)   #to show the conversation between the user and the assistant
			break
	  
		except: 
	  
			assistant_speaks("Could not understand your audio, PLease try again !") 
	return text

#seaches the product asked by the user and returns the location of the product
def searching(user_input1):

	items = False
	for item in shop_items:
		if user_input1.lower().replace(" ","") == item :
			assistant_speaks(shop_items[item])
			cart.append(str(user_input1))
			items = True
			break
	
	if user_input1.lower().replace(" ","") == "exit" or "nothing" or "done":
		break

	if items == True:
		return
	else:
		print("not available please enter valid product")
		return
	





