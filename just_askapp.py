from project import *
from tabulate import tabulate


if __name__ == "__main__":
    assistant_speaks("Hello, I am Friday Your personal Assistant.")
    assistant_speaks("Whats your name ?") 
    name =''
    name = get_audio() 
    assistant_speaks("Hello, " + name + '.') 
    speak = "I am here to make your life easier. You can ask me what you want to buy "
    assistant_speaks(speak)

data = [["milk", "icecream", "softdrinks","cleaningitems"],["chocolates","soaps","spices","liquids"],
["biscuits", "toothpaste","readytomix","detergents"],["bread","shampoo","flours","disinfectents"]]
print(tabulate(data,headers=["Aisle_1","Aisle_2","Aisle_3","Aisle_4"],tablefmt="fancy_grid"))


while True :
    assistant_speaks("What would you like to buy ") 
    user_input = get_audio().lower() 
    searching(user_input)
  
    if user_input == "": 
        continue
    #this part is used exit the shopping and check out the words 'exit','nothing', 'done' and 'bye' to do so
    if "exit" in str(user_input) or "bye" in str(user_input)  or "nothing" in str(user_input) or "done" in str(user_input): 
        assistant_speaks("would you like to check out ?")
        user_input_1 = get_audio().lower()
        #here the assistant asks for confirmation of leaving. It accepts the phrases "yep", "yeah", "sure" and "yes".
        if "yes" in str(user_input_1) or "yeah" in str(user_input_1) or "yep" in str(user_input_1) or "sure" in str(user_input_1):
            print("\nYour Cart\n")
            for i in cart:
                print(i)
            break

    else :
        continue


assistant_speaks("Ok bye, "+ name+'.')
