# import the random function to generate a random number/response/string
from random import choice

# creating a function to responsed to the given user response
def get_bot_response(user_response):
    bot_response_yes = ["Omg! No Way!", "I play too!", "We should play together!", "Here's my user name! edison4354"]
    bot_response_no = ["Awww if you ever decide to get it let me know!", "It's ok your not missing anything", "GET THE GAME NOW!"]

    if user_response == "yes":
        return choice(bot_response_yes)
    elif user_response == "no":
        return choice(bot_response_no)
    else:
        return "Hmmm not what I expect but ok!"

# print a greeting message explaing what the chat box in about
print("Welcome to Valorant Bot")
print("Please enter if you play or not")

user_response = ""

# while loop that keeps running the question and bot response till 'done' is entered
while True:
    user_response = input("Do you play valorant?: ").lower()

    if user_response == 'done':
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)



