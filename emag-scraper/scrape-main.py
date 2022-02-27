#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3

import json
import sys
from pathlib import Path
from simple_term_menu import TerminalMenu
from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

json_path = f"{Path(__file__).parent.resolve()}/Web-Scraper/"
# Remote the below line when you're sure it is working
# json_path = '/Users/kostadintonchekliev/Desktop/scripts/Python/Web-Scraper/'

def emag_check():
    try:
        requests.get('https://www.emag.bg/')
    except:
        print("Error reaching Emag server")
        exit()


def json_check():
    # Make sure that the dir exists
    Path(json_path).mkdir(parents=True, exist_ok=True)
    if not Path(f'{json_path}products.json').exists():
        print("File doesn't exists, created it for you")
        Path(f'{json_path}products.json').touch()


def read_json():
    global products_list
    with open(f'{json_path}products.json', 'r') as json_data:
        try:
            products_list = json.load(json_data)
        except:
            products_list = {}


def update_json():
    with open(f'{json_path}products.json', 'w') as json_data:
        json.dump(products_list, json_data)


def build_menu():
    global menu_options
    menu_options = []
    if len(products_list.keys()) > 0:
        menu_options.extend(("Add new product", "Remove existing product", "Show all products", "Exit"))
    else:
        menu_options.extend(("Add new product", "Exit"))


def read_menu(listt):
    choice = TerminalMenu(listt, title="Please select:").show()
    return choice


def return_action(dictt, selection):
    return dictt[selection]


def data_scrape(link):
    page_content = requests.get(link)
    soup = BeautifulSoup(page_content.content, 'lxml')
    title = soup.find('h1', class_='page-title').text.strip().split(',')[0]
    price = soup.find('p', class_='product-new-price').text.strip()
    try:
        soup.find('span', class_='label label-out_of_stock').text.strip()
        price = 0
    except:
        price = beautify(price)
    return title, price


def add_data():
    label = input("Please enter label:")
    while label in products_list:
        label = input("Label already exists, please enter a new one: ")
    url = input("Please enter url:")
    try:
        requests.get(url)
    except:
        print("Incorrect or broken link, exiting without adding data")
        exit()
    product_title, product_price = data_scrape(url)
    products_list[label] = product_title, product_price, url


def remove_data():
    choice = read_menu(list(products_list.keys()) + ["Exit"])
    if choice == len(products_list.keys()):
        exit()
    else:
        del products_list[list(products_list)[choice]]


def beautify(original_price):
    new_price = ""
    original_price = original_price.replace('.', '')
    original_price = list(original_price.split()[0])
    original_price.insert(-2, '.')
    for char in original_price:
        new_price = new_price + str(char)
    return float(new_price)


def main_actions():
    if action == "Add new product":
        add_data()
        update_json()
    elif action == "Remove existing product":
        remove_data()
        update_json()
    elif action == "Show all products":
        for object in products_list:
            print(
                f'Label: {object}, Name: {products_list[object][0]}, Price: {products_list[object][1]}, URL: {products_list[object][2]}')
        exit()
    elif action == "Exit":
        exit()


def check_argument():
    try:
        option = sys.argv[1]
    except IndexError:
        option = 'none'
    return option


def show_prices_compared():
    for product in products_list:
        new_price = data_scrape(products_list[product][2])[1]
        if new_price == 0:
            print(f"{product}: Not in stock")
        elif new_price == products_list[product][1]:
            print(f"{product}: {new_price} =")
        elif new_price > products_list[product][1]:
            print(f"{product}: {new_price} \u1403")
        elif new_price < products_list[product][1]:
            print(f"{product}: {new_price} \u1401")


def xbar_show():
    if len(products_list.keys()) > 0:
        print("View Scrape")
        print("---")
        show_prices_compared()
    else:
        print("No products")


def show_help():
    table = PrettyTable()
    table.field_names = ["Option", "Action"]
    table.add_rows(
        [
            ["none", "Xbar Mode - displays data in xbar format"],
            ["-u", "Full Mode - shows all possible actions"],
            ["-h", "Help Mode - current help section"],
            ["-p", "Pretty Mode - shows more and better formatted information"]
        ]
    )
    print(table)


def show_pretty_info():
    table = PrettyTable()
    table.field_names = ["Label", "Name", "Price"]
    for entry in products_list:
        table.add_row([entry, products_list[entry][0], products_list[entry][1]])
    print(table)


if __name__ == '__main__':
    in_option = check_argument()
    if in_option == '-u':
        json_check()
        while True:
            read_json()
            build_menu()
            action = return_action(menu_options, read_menu(menu_options))
            main_actions()
    elif in_option == '-h':
        show_help()
    elif in_option == '-p':
        json_check()
        read_json()
        show_pretty_info()
    elif in_option == 'none':
        emag_check()
        json_check()
        read_json()
        xbar_show()
    else:
        print("Wrong option selected, select -h for help")
