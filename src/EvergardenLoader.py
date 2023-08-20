import importlib
import datetime
import os, platform, getpass
import sys

def logs(log_to_write: str):
    system_os_platform = platform.system()
    filename = "evergardenLoaderlog.txt"
    if system_os_platform == "Windows":
        appdata = os.path.join(os.environ['APPDATA'])
        path = f"{appdata}\\Evergarden\\{filename}"
    elif system_os_platform == "Linux":
        username = getpass.getuser()
        appdata = os.path.join("/home", username)
        path = f"{appdata}/Evergarden/{filename}"
    else:
        path = f"Evergarden/{filename}"
    date = datetime.date.today()
    d, m, y = date.day, date.month, date.year
    log = open(path, 'a')
    log_to_write = f"\n[EvergardenLoader{d}{m}{y}] {log_to_write}"
    log.write(log_to_write)
    log.close()


system_os_platform = platform.system()

if system_os_platform == "Windows":
    appdata = os.path.join(os.environ['APPDATA'])
    addons_directory = f"{appdata}\\Evergarden\\addons"
elif system_os_platform == "Linux":
    username = getpass.getuser()
    appdata = os.path.join("/home", username)
    addons_directory = f"{appdata}/Evergarden/addons"
else:
    appdata = os.path.dirname(os.path.realpath(__file__))
    addons_directory = f"{appdata}/Evergarden/addons"

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
