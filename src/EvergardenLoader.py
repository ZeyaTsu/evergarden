import importlib
import datetime
import os
import sys  # Import the sys module

def logs(log_to_write: str):
    date = datetime.date.today()
    d, m, y = date.day, date.month, date.year
    filename = f'evergardenLoaderlog.txt'
    log = open(filename, 'a')
    log_to_write = f"\n[EvergardenLoader{d}{m}{y}] {log_to_write}"
    log.write(log_to_write)
    log.close()

appdata = os.path.join(os.environ['APPDATA'])
addons_directory = f"{appdata}\\Evergarden\\addons"
elements = 0
addons_to_load = []
loaded_addons = []

# Append addons_directory to sys.path
sys.path.append(addons_directory)

for file_name in os.listdir(addons_directory):
    if file_name.endswith(".py") and file_name != "__init__.py":
        addon_name = os.path.splitext(file_name)[0]
        addons_to_load.append(addon_name)

try:
    for addon_name in addons_to_load:
        try:
            addon_module = importlib.import_module(addon_name)
            loaded_addons.append(addon_module)
        except ImportError as e:
            print(f"Failed to load addon {addon_name}: {e}")

    for addon in loaded_addons:
        logs(f'Addon [{addon}]')
except Exception as e:
    logs(f"Error - {e}")

def isModded():
    global addons_to_load
    global elements
    try:
        for addons in addons_to_load:
            elements += 1
            logs(f"Got '{addons}'")
        logs(f"Loaded {elements} addons")
        return addons_to_load
    except Exception as e:
        logs(f"Error - {e}")
        return False

def run(addon_name):
    try:
        addon_module = importlib.import_module(addon_name)
        addon_module.run()
    except Exception as e:
        print(f"Failed to load addon {addon_name}: {e}")
