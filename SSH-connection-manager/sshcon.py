#!/usr/bin/env python3

import json
import subprocess
from simple_term_menu import TerminalMenu
from pathlib import Path

print("SSH Connection Manager ver 5.0")

#Main path to the json file
json_path = "/Users/kostadintonchekliev/Desktop/scripts/Python/SSH_Connection/conn_data.json"

menu_options = []

#Functions
def json_check():
    if not Path(json_path).exists():
        print("File doesn't exist, creating it for you")
        Path(json_path).touch()
def return_key(option):
    return list(conn_dict.keys())[option]
def return_value(option):
    return list(conn_dict.values())[option]
def read_data():
    with open(json_path, 'r') as json_data:
        try:
            main_dict = json.load(json_data)
            for result in main_dict.keys():
                menu_options.append(result)
        except:
            main_dict = {}

        return main_dict
def update_data():
    with open(json_path, 'w') as json_file:
        json.dump(conn_dict, json_file)

def add_conn():
    label = input("Please select label: ")
    username = input("Please enter username: ")
    hostname = input("Please enter hostname: ")
    conn_dict[label] = f"ssh {username}@{hostname} -p18765"
    update_data()

def remove_conn():
    choice2 = TerminalMenu(menu_options[:-3] + ["Exit"], title="Please select which connection to remove:").show()
    if choice2 == len(menu_options) - 3:
        print("Returning")
    else:
        del conn_dict[return_key(choice2)]
        update_data()
def build_menu():
    if len(menu_options) > 0:
        menu_options.extend(("Remove Connections", "Add New", "Exit"))
    elif len(menu_options) == 0:
        menu_options.extend(("Add New", "Exit"))

if __name__ == '__main__':
    json_check()

    while True:
        conn_dict = read_data()
        build_menu()
        choice = TerminalMenu(menu_options, title="Please select an action:").show()
        if choice == len(menu_options) - 1:
            exit("Exiting script. Goodbye")
        elif choice == len(menu_options) - 2:
            add_conn()
        elif choice == len(menu_options) - 3:
            remove_conn()
        else:
            subprocess.run(return_value(choice), shell=True)
            exit()

        menu_options = []