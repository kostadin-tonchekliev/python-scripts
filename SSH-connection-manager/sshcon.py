#!/usr/bin/env python3

import json
import subprocess
from simple_term_menu import TerminalMenu
from pathlib import Path

print("SSH Connection Manager ver 4.0")

#Main path to the json file
json_path = "/Users/kostadintonchekliev/Desktop/scripts/Python/SSH_Connection/conn_data.json"

menu_options = []

#Functions
def return_key(option):
    return list(conn_dict.keys())[option]
def return_value(option):
    return list(conn_dict.values())[option]
def update_data():
    with open(json_path, 'w') as json_file:
        json.dump(conn_dict, json_file)

#Check if the json file exist
if not Path(json_path).exists():
    print("File doesn't exist, creating it for you")
    Path(json_path).touch()

with open(json_path, 'r') as json_data:
    try:
        conn_dict = json.load(json_data)
        for result in conn_dict.keys():
            menu_options.append(result)
    except:
        conn_dict = {}

if len(menu_options) > 0:
    menu_options.extend(("Remove Connections", "Add New"))
else:
    menu_options.append("Add New")

choice = TerminalMenu(menu_options, title="Please select an action:").show()
if choice == len(menu_options) - 1:
    label = input("Please select label: ")
    username = input("Please enter username: ")
    hostname = input("Please enter hostname: ")
    conn_dict[label] = f"ssh {username}@{hostname} -p18765"
    update_data()
elif choice == len(menu_options) - 2:
    choice2 = TerminalMenu(menu_options[:-2], title="Please select which connection to remove:").show()
    del conn_dict[return_key(choice2)]
    update_data()
else:
    subprocess.run(return_value(choice), shell=True)