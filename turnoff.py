import os
import voice_assistant as va


class ShutDown:
    def __init__(self):
        print('Natasha: Turning off the system')
        va.reply('Turning off the system')
        os.system("shutdown /s /t 1")