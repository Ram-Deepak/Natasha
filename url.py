import webbrowser
import voice_assistant as va


def send_link(option):
    if option == "1":
        return "https://docs.google.com/spreadsheets/d/1dPCs90NXbDa55WZ0i5s7zU63QlytCve2oeFOsB__99M/edit#gid=0"
    elif option == "2":
        return "https://drive.google.com/drive/u/0/my-drive"
    elif option == "3":
        return "https://www.onlinedegree.iitm.ac.in/"
    elif option == "4":
        return "https://www.youtube.com/"
    elif option == "5":
        return "https://onlinecourses.nptel.ac.in/"
    elif option == "6":
        return "https://www.udemy.com/"
    elif option == "7":
        return "https://classroom.google.com/u/0/h"
    elif option == "8":
        return "https://mail.google.com/mail/u/0/#inbox"
    elif option == "9":
        return "amazon.in"
    elif option == "10":
        return "https://www.linkedin.com"
    elif option == "11":
        return "https://sece.ac.in"
    elif option == "12":
        return "https://ed-matrix.com/"
    elif option == "13":
        return "https://www.skillrack.com/faces/login.xhtml"
    elif option == "14":
        return "https://www.hackerrank.com/"
    else:
        return "Invalid option"


def open_link(url, website):
    if url != "Invalid option":
        va.reply("opening "+website)
        webbrowser.register("chrome", None,
                        webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get("chrome").open(url)
    else:
        print("Invalid")
        va.reply("Invalid")
