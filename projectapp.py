from project import *

if __name__ == "__main__":
    assistant_speaks("Hello, I am Friday Your personal Assistant.")
    assistant_speaks("Whats your name ?") 
    name =''
    name = get_audio() 
    assistant_speaks("Hello, " + name + '.') 
    speak = "I am here to make your life easier. You can ask me what you want to buy "
    assistant_speaks(speak)

pprint(shop_items.keys())

while True :
    assistant_speaks("What would you like to buy ") 
    user_input = get_audio().lower() 
    searching(user_input)
  
    if user_input == "": 
        continue
  
    if "exit" in str(user_input) or "bye" in str(user_input)  or "Nothing" in str(user_input): 
        assistant_speaks("would you like to check out ?")
        user_input_1 = get_audio().lower()
        if "yes" in str(user_input_1) or "yeah" in str(user_input_1) or "yep" in str(user_input_1) or "sure" in str(user_input_1):
            pprint(cart)
            
            break

    else :
        continue


assistant_speaks("Ok bye, "+ name+'.')