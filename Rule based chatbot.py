print("--------------------")
print("Rule Based Chatbot")
print("--------------------")
name=input("What is your name:")
print("\n Hello",name,"!Nice to meet with you")
print("You can start chatting with me")
print("You can type bye to exit")


while True:
    question=input("\nYou:").lower().strip()
    if (question=="hi" or question=="hello"):
        print("BOT:Hello!")
        
    elif(question=="what is python"):
        print("Python is a Programming Language...It is high level language and easy syntax")
    
    elif(question=="how are you"):
         print("BOT: I am fine! What about you?")
         
    elif(question=="what is aI"):
        print("BOT: It is branch of computer science that enables machines to perform tasks that seem intelligent")
        
    elif(question=="bye"):
        print("BOT: Bye..See you later")
        break
    else:
        print("Sorry..I can't understand your questions")
        