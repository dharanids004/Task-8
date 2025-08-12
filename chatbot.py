print("🤖 Chatbot: Hello! I am your friendly chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()  # Collect input and make it lowercase

    # Exit condition
    if user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break

    # Responses using if-elif-else
    if "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")
    elif "your name" in user_input:
        print("🤖 Chatbot: I am ChatBot-9000, your virtual assistant.")
    elif "help" in user_input:
        print("🤖 Chatbot: Sure! You can ask me about my name, how I’m doing, or just say hello.")
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        print(f"🤖 Chatbot: The current time is {now.strftime('%H:%M:%S')}.")
    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        print(f"🤖 Chatbot: Today's date is {today}.")
    else:
        print("🤖 Chatbot: Sorry, I didn’t understand that. Can you try asking something else?")