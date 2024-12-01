import os
import importlib.util
import sys
import string
import secrets
from simple_term_menu import TerminalMenu


def load_module(source):
    """
    reads file source and loads it as a module
    credit to: https://medium.com/@david.bonn.2010/dynamic-loading-of-python-code-2617c04e5f3f

    :param source: file to load
    :return: loaded module
    """

    module_name = 'gensym_' + "".join([secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32)])

    spec = importlib.util.spec_from_file_location(module_name, source)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def getDirectories() -> list:
    """
    list the available days in the `days` folder

    :return: list of days
    """

    availableDays = []

    for singleDir in os.listdir('days'):
        if os.path.isdir(f"days/{singleDir}"):
            availableDays.append(singleDir)

    return availableDays


if __name__ == '__main__':
    days = getDirectories()
    action = 'main'
    args = sys.argv

    if len(days) == 0:
        print("[Info] Unable to find any days to load")
        exit(0)

    match len(args):
        case 1:
            menuObject = TerminalMenu(days, title='Select day:')
            dayChoice = days[menuObject.show()]
        case 2:
            if args[1] in days:
                dayChoice = args[1]
            else:
                print(f"[Err] Invalid day chosen: {args[1]}")
                exit(1)
        case 3:
            if args[1] in days:
                dayChoice = args[1]
                action = args[2]
            else:
                print(f"[Err] Invalid day chosen: {args[1]}")
                exit(1)
        case _:
            print("[Err] Invalid number of arguments provided!")
            exit(1)

    customModule = load_module(f'days/{dayChoice}/main.py')

    match action:
        case 'main':
            customModule.main()
        case 'test':
            customModule.test()
        case 'partOne':
            customModule.partOne()
        case 'partTwo':
            customModule.partTwo()
