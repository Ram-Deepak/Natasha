import open_url as ou
import voice_assistant as va
import datetime
import pytz


def chat_bot():
    bot_dictionary1 = {
        "Welcome": "Hi I'm Natasha",
        "tell me a joke": "Hahaha",
        "had your lunch?": "Yes of course",
        "hi": "Hi",
        "hello": "Hello",
        "how is your day?": "good",
        "how are you?": "Fine",
        "what's your name?": "Natasha",
        "who are your sisters?": "Siri and Alexa",
        "what is my name?": "Your name is Ram",
        "bye": "Bye Ram",
    }

    website_list = ["open a website"]

    print("Natasha:", bot_dictionary1["Welcome"])
    va.reply(bot_dictionary1["Welcome"])
    flag1 = True
    while flag1:
        bot_input = input("You: ")
        # for key in bot_dictionary1.keys():
        if bot_input.lower() in bot_dictionary1.keys():
            print("Natasha:", bot_dictionary1[bot_input.lower()])
            va.reply(bot_dictionary1[bot_input.lower()])
        elif bot_input.lower() in website_list:
            ou.print_choices()
        elif "date" in bot_input.lower():
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            print("Natasha:", str(current_time.day)+":"+str(current_time.month)+":"+str(current_time.year))
            va.reply(str(current_time.day)+" "+str(current_time.month)+" "+str(current_time.year))
        elif bot_input.lower() == "exit":
            return False
        else:
            print("Natasha : Sorry I could not understand")
            va.reply("Sorry I could not understand")
                

flag = True
again = input("Do you want to continue?: If yes press 1 else press 2 ")
while flag:
    if again == '2':
        flag = False
    elif again == '1':
        print("Note : If you decide to stop the conversation then type 'exit'")
        flag = chat_bot()