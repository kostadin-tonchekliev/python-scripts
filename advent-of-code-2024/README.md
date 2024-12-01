## Executor for the Advent of Code 2024 challenges

---

This script is designed to dynamically combine all Advent of Code 2024 challenges into a single executable and run specific days.

### Setup:
1. Clone the folder
2. Initialize a python virtual environment using the following command:
```shell
python3 -m venv shadowRealm
```
3. Enter the virtual environment
```shell
source shadowRealm/bin/activate
```
4. Install the requirements
```shell
python3 -m pip install -r requirements.txt
```

### Usage:
Run the `main.py` executable:
```shell
python3 main.py
```

By default it will run the `main` function of the selected day, however you can also provide a specific day to be executed and which function to run. This is an example which runs day 2 and the test function:
```shell
python3 main.py 2 test
```

### Configuration:
- Days should be added into the `days` folder, each day needs to be separated in a different folder
- Days should all include a `main.py` file
- The `main.py` file needs to include a `main()` function which will be run by default, additional functions currently supported: `test`, `partOne`, `partTwo`. Any additional functions need to be defined in the `main.py` file as well (in the switch case on line **76**)