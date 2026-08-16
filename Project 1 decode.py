# ==========================================
# Rule-Based AI Chatbot
# Project 1 - DecodeLabs AI Internship
# Developed by: Sawera Mushtaq
# ==========================================

from datetime import datetime

print("=" * 45)
print("       Welcome to SmartBot")
print("=" * 45)
print("Hello! I am SmartBot.")
print("Type 'help' to see available commands.\n")

while True:

    user = input("You: ").strip().lower()

    # Greeting
    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! Nice to meet you.")

    # Name
    elif user == "what is your name" or user == "name":
        print("Bot: My name is SmartBot.")

    # How are you
    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    # Creator
    elif user == "who made you":
        print("Bot: I was created by Sawera.")

    # Capabilities
    elif user == "what can you do":
        print("Bot: I can answer simple questions,")
        print("     perform calculations,")
        print("     tell jokes,")
        print("     show date & time,")
        print("     and motivate you.")

    # Date
    elif user == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", today)

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Calculator - Addition
    elif user == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Result =", num1 + num2)

    # Calculator - Subtraction
    elif user == "subtract":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Result =", num1 - num2)

    # Calculator - Multiplication
    elif user == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Bot: Result =", num1 * num2)

    # Calculator - Division
    elif user == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("Bot: Cannot divide by zero.")
        else:
            print("Bot: Result =", num1 / num2)

    # Joke
    elif user == "joke":
        print("Bot: Why do programmers love Python?")
        print("     Because it's easy to learn!")

    # Motivation
    elif user == "motivation":
        print("Bot: Believe in yourself.")
        print("     Small steps every day lead to big success.")

    # Fact
    elif user == "fact":
        print("Bot: Artificial Intelligence is changing many industries.")

    # Help
    elif user == "help":
        print("\n===== Available Commands =====")
        print("hi")
        print("hello")
        print("hey")
        print("what is your name")
        print("how are you")
        print("who made you")
        print("what can you do")
        print("date")
        print("time")
        print("add")
        print("subtract")
        print("multiply")
        print("divide")
        print("joke")
        print("motivation")
        print("fact")
        print("bye")
        print("==============================")

    # Exit
    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I don't understand that command.")
        print("     Type 'help' to see available commands.")