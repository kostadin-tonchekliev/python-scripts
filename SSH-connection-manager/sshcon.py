#!/usr/bin/env python3

import subprocess
from simple_term_menu import TerminalMenu
from pathlib import Path

print("SSH Connection Manager ver 3.0")

#Main paths to the connections.txt and labels.txt files used throughout the script
connections_path = "/Users/kostadintonchekliev/Desktop/scripts/Python/SSH_Connection/connections.txt"
labels_path = "/Users/kostadintonchekliev/Desktop/scripts/Python/SSH_Connection/labels.txt"
conn_dict = {}

#Check if the connections.txt and labels.txt file exist
if Path(connections_path).exists() == False :
    print("Connections file is missing, creating it for you")
    Path(connections_path).touch()
if Path(labels_path).exists() == False :
    print("Labels file is missing, creating it for you")
    Path(labels_path).touch()

#Reads files and stores them into lists
with open(connections_path, 'r') as conns:
    connections = [x.rstrip() for x in conns.readlines()]
with open(labels_path, 'r') as lbl:
    labels = [x.rstrip() for x in lbl.readlines()]

#Shows options to add or remove connections based on stored connections
if len(connections) == 0 and len(labels) == 0 :
    labels.append("Add New")
else:
    labels.extend(("Remove connection", "Add New"))

#Creates main dictionary
for i in range(len(connections)):
    conn_dict[i] = labels[i], connections[i]

#Menus and options to add/remove connections
choice = TerminalMenu(labels, title="Please select an action:").show()
if choice == len(labels) - 1:
    server = input("Please enter server: ")
    username = input("Please enter username: ")
    label = input("Please select label: ")
    subprocess.run(f"echo \"ssh {username}@{server} -p18765\" >> {connections_path}", shell=True)
    subprocess.run(f"echo \"{label}\" >> {labels_path}", shell=True)
elif choice == len(labels) - 2:
    choice2 = TerminalMenu(labels[:-2], title="Please select which connection to remove:").show()
    subprocess.run(f"sed -i '' '/{conn_dict[choice2][1]}/d' {connections_path}", shell=True)
    subprocess.run(f"sed -i '' '/{conn_dict[choice2][0]}/d' {labels_path}", shell=True)
else:
    print(f"Connecting to \"{conn_dict[choice][0]}\"...")
    subprocess.run(conn_dict[choice][1], shell=True)
