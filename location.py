from webbrowser import open
import voice_assistant as va


class Location:

    def __init__(self, add):
        self.address = add

    def map(self):
        open("http://www.google.com/maps/search/"+self.address)
