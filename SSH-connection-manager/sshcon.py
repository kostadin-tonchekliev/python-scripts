#!/usr/bin/env python3

import subprocess
from simple_term_menu import TerminalMenu

print("SSH Connection Manager ver 2.0")
conn_dict = {}

with open('/Users/kostadintonchekliev/Desktop/scripts/Python/SSH Connection/connections.txt', 'r') as conns:
    connections = [x.rstrip() for x in conns.readlines()]

with open('/Users/kostadintonchekliev/Desktop/scripts/Python/SSH Connection/labels.txt', 'r') as lbl:
    labels = [x.rstrip() for x in lbl.readlines()]
labels.extend(("Add New", "Remove connection"))

for i in range(len(connections)):
    conn_dict[i] = labels[i], connections[i]

print("Please select a desired connection:")
choice = TerminalMenu(labels).show()
if choice == len(labels) - 2:
    server = input("Please enter server: ")
    username = input("Please enter username: ")
    label = input("Please select label:")
    subprocess.run(f"echo \"ssh {username}@{server} -p18765\" >> /Users/kostadintonchekliev/Desktop/scripts/Python/SSH\ Connection/connections.txt", shell=True)
    subprocess.run(f"echo \"{label}\" >> /Users/kostadintonchekliev/Desktop/scripts/Python/SSH\ Connection/labels.txt", shell=True)

elif choice == len(labels) - 1:
    print("Please select which connection to remove:")
    choice2 = TerminalMenu(labels[:-2]).show()
    subprocess.run(f"sed -i '' '/{conn_dict[choice2][0]}/d' /Users/kostadintonchekliev/Desktop/scripts/Python/SSH\ Connection/labels.txt", shell=True)
    subprocess.run(f"sed -i '' '/{conn_dict[choice2][1]}/d' /Users/kostadintonchekliev/Desktop/scripts/Python/SSH\ Connection/connections.txt", shell=True)
else:
    print(f"Connecting to \"{conn_dict[choice][0]}\"...")
    subprocess.run(conn_dict[choice][1], shell=True)
