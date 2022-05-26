import open_url as ou
import voice_assistant as va
import datetime
import pytz
import battery
import turnoff
from location import Location


def chat_bot():
    bot_dictionary1 = {
        "Welcome": "Hi Deepak, I'm Natasha",
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
        bot_input = input("You: ").lower()
        # for key in bot_dictionary1.keys():
        if bot_input in bot_dictionary1.keys():
            print("Natasha:", bot_dictionary1[bot_input])
            va.reply(bot_dictionary1[bot_input])
        elif bot_input in website_list:
            ou.print_choices()
        elif "date" in bot_input:
            current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            print("Natasha:", str(current_time.day)+":"+str(current_time.month)+":"+str(current_time.year))
            va.reply("Today's date is "+str(current_time.day)+" "+str(current_time.month)+" "+str(current_time.year))
        elif "time" in bot_input:
            current_date = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            current_time = str(current_date.strftime("%X")).split(':')
            print("Natasha:", current_time[0]+':'+current_time[1]+':'+current_time[2])
            va.reply("Time is "+str(current_time[0])+' hours '+str(current_time[1])+' minutes '+str(current_time[2])+' seconds')
        elif "power" in bot_input or "battery" in bot_input:
            battery.Power()
        elif "shutdown" in bot_input or "turnoff" in bot_input:
            turnoff.ShutDown()
        elif "location" in bot_input or "place" in bot_input or "find" in bot_input:
            print('Natasha: Enter the location')
            va.reply('Enter the location')
            address = input('You: ')
            loc = Location(address)
            loc.map()
        elif bot_input == "exit":
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
