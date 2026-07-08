def chatbot():
    print("Welcome to ChatBot!")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "good morning":
            print("Bot: Good morning! Have a great day.")

        elif user == "good evening":
            print("Bot: Good evening!")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()