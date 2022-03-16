Web scraper designed to work with emag.bg. Current features: <br>
* monitor the price of different products and show if it drops or is increased
* show if a product is out of stock and shows if it becomes available
* support running the script with [xbar](https://xbarapp.com/) for showing the data in your taskbar
---
### Requirements
You need to have the following python packages installed:
```commandline
simple_term_menu
pathlib
bs4
requests
prettytable
```
```
pip3 install -r requirements.txt
```

In the begging of the file update `json_path` to the full desired path where you want to have the main json file stored.

### Usage
-Run the file without any arguments for xbar mode (this means that it will display only the end data): <br>
```
Koce@ ~/Python/Web-Scraper:py scrape-main.py
View Scrape
---
LG-Cheap: 695.04 =
32UltraWide: 799.99 =
274K-The one: 727.92 =
TheOne: 1102.74 =
StockTest: Not in stock
```

-Run the file with the argument `-u` for full mode where you can add new connections, remove existing ones and etc. : <br>
```
Koce@ ~/Python/Web-Scraper:py scrape-main.py -u
Please select:
> Add new product
  Remove existing product
  Show all products
  Exit
```
