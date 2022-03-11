import url    # url is an user defined module which contains website url
import voice_assistant as va
# from prettytable import PrettyTable
# print("Hi"+"\n"+"I'm Natasha")
# print("I'll direct you to one of the websites that you visit frequently")

# Site options in a table
'''choice_table = PrettyTable(["Option", "Site"])
choice_table.add_row(["1", "Expenditure data excel sheet"])
choice_table.add_row(["2", "My drive"])
choice_table.add_row(["3", "IITMOD website"])
choice_table.add_row(["4", "You Tube"])
choice_table.add_row(["5", "NPTEL"])
choice_table.add_row(["6", "UDEMY"])
choice_table.add_row(["7", "Google Classroom"])
choice_table.add_row(["8", "Gmail"])
choice_table.add_row(["9", "Amazon"])
choice_table.add_row(["10", "LinkedIn"])
choice_table.add_row(["11", "SECE website"])'''

choice_dict = {
    "1": "Expenditure data excel sheet",
    "2": "My drive",
    "3": "IITMOD website",
    "4": "You Tube",
    "5": "NPTEL",
    "6": "UDEMY",
    "7": "Google Classroom",
    "8": "Gmail",
    "9": "Amazon",
    "10": "LinkedIn",
    "11": "SECE website",
    "12": "Ed-matrix",
    "13": "Skill rack",
    "14": "HackerRank"
}


def print_choices():
    # print(choice_table)
    for key in choice_dict.keys():
        print(key+" : "+choice_dict[key])
    direct_to_link()


def direct_to_link():
    print("Enter any one of the above mentioned options")
    va.reply("Enter any one of the above mentioned options")
    k = input()
    if k in choice_dict.keys():
        url.open_link(url.send_link(k), choice_dict[k])
    else:
        va.reply("Invalid option")