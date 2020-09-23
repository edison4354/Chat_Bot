from random import choice

def get_bot_response(user_response):
    bot_response_yes = ["Omg! No Way!", "I play too!", "We should play together!"]
    bot_response_no = ["Awww if you ever decide to get it let me know!", "sending good vibes", ""]

    if user_response == "yes":
        return choice(bot_response_yes)
    elif user_response == "no":
        return choice(bot_response_no)
    else:
        return "Hmmm not what I expect but ok!"





