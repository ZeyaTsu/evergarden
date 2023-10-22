import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
from threading import Thread
from bing_image_downloader import downloader
from PIL import Image, ImageTk
import sys, requests, datetime, os, platform, getpass, importlib.util
from configparser import ConfigParser

try:
    system_os_platform = platform.system()
    if system_os_platform == "Windows":
        appdata = os.path.join(os.environ['APPDATA'])
        dr = f"{appdata}\\Evergarden"
        if os.path.exists(dr) == False:
            folder = "Evergarden"
            path = os.path.join(appdata, folder)
            os.mkdir(path)
    elif system_os_platform == "Linux":
        username = getpass.getuser()
        appdata = os.path.join("/home", username)
        dr = f"{appdata}/Evergarden"
        if os.path.exists(dr) == False:
            folder = "Evergarden"
            path = os.path.join(appdata, folder)
            os.mkdir(path)
    else:
        appdata = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(appdata, "Evergarden")
        os.mkdir(path)
        
except:
    pass

"""
███████ ██    ██ ███████ ██████   ██████   █████  ██████  ██████  ███████ ███    ██ 
██      ██    ██ ██      ██   ██ ██       ██   ██ ██   ██ ██   ██ ██      ████   ██ 
█████   ██    ██ █████   ██████  ██   ███ ███████ ██████  ██   ██ █████   ██ ██  ██ 
██       ██  ██  ██      ██   ██ ██    ██ ██   ██ ██   ██ ██   ██ ██      ██  ██ ██ 
███████   ████   ███████ ██   ██  ██████  ██   ██ ██   ██ ██████  ███████ ██   ████ 
                                                                                    
                                                                                    
███████ ███████ ██    ██  █████  ████████ ███████ ██    ██                          
   ███  ██       ██  ██  ██   ██    ██    ██      ██    ██                          
  ███   █████     ████   ███████    ██    ███████ ██    ██                          
 ███    ██         ██    ██   ██    ██         ██ ██    ██                          
███████ ███████    ██    ██   ██    ██    ███████  ██████    
"""

"""

MAIN CODE

"""

CACHE_PATH = ""

def logs(log_to_write:str):
    global CACHE_PATH
    date = datetime.date.today()
    d,m,y = date.day, date.month, date.year
    osn = platform.system()
    filename = f'evergardenlog.txt'
    if osn == "Windows":
        appdata = os.path.join(os.environ['APPDATA'])
        path = f"{appdata}\\Evergarden\\"
        r_path = path+filename
    elif osn == "Linux":
        username = getpass.getuser()
        appdata = os.path.join("/home", username)
        path = f"{appdata}/Evergarden/"
        r_path = path+filename
    else:
        path = f"Evergarden/"
        r_path = path+filename
    log = open(r_path, 'a')
    log_to_write = f"\n[Evergarden{d}{m}{y}] {log_to_write}"
    log.write(log_to_write)
    log.close()
    if CACHE_PATH == "":
        CACHE_PATH = path

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("violet.ico")
search_term = ""
set_loaded = False
profile_selected = None
theme_selected = None
custom_theme_selected = None
main_color = None
second_color = None
button_color = None
text_color = None

def download_images(anime_name, character_name, image_type, num_images_to_download, save_folder, anime_explicit, gif_only, options_black_white, options_pinterest, options_tenor):
    global search_term
    search_term = f"{anime_name} {character_name} {image_type}"
    if anime_explicit:
        search_term += " anime"
        logs("Applying Anime Explicit")
    if gif_only:
        search_term += " gif"
        logs('Applying Gif Only Filter')
    if options_black_white:
        search_term += " black white manga"
        logs('Applying Black & White Filter')
    if options_pinterest:
        search_term += " pinterest"
        logs('Applying Pinterest source')
    if options_tenor:
        search_term += " tenor"
        logs('Applying Tenor source')
    if image_type.lower() == "all":
        image_type = ""
    logs('Starting download')
    downloader.download(search_term, limit=num_images_to_download, output_dir=save_folder,
                        adult_filter_off=True, force_replace=False, timeout=60)

def on_download_clicked():
    global set_loaded, profile, CACHE_PATH, profile_selected
    save_folder = entry_save_folder.get().strip()  # Get the selected save folder

    if profile_selected != None:
        c = ConfigParser()
        c.read(f'{CACHE_PATH}evergarden_presets.ini')
        profiles = c.sections()
        for profile in profiles:
            logs(f'Getting [{profile}] preset')
        preset = c[profile_selected]
        anime_name = preset["anime_name"]
        character_name = preset["character_name"]
        image_type = preset["type"]
        if image_type == "pfp" or image_type == "profile picture":
            image_type == "profile picture"
        elif image_type.lower() == "wallpaper":
            image_type = "wallpaper"
        elif image_type.lower() == "screencaps":
            image_type = "screencaps"
        else:
            image_type = "all"
        num_images_to_download = int(preset["n_images"])
        gif_only = preset["gif"]
        if gif_only == "True":
            gif_only = True
        else:
            gif_only = False
        options_black_white = preset['filter']
        if options_black_white != "None":
            options_black_white = True
        else:
            options_black_white = False
        options_pinterest = preset["pinterest"]
        if options_pinterest == "True":
            options_pinterest = True
        else:
            options_pinterest = False 
        options_tenor = preset["tenor"]
        if options_tenor == "True":
            options_tenor = True
        else:
            options_tenor = False        
        if not save_folder:
            messagebox.showinfo("Save Folder", f"No Save Folder was specified, you will find your images in the Evergarden folder ({CACHE_PATH})")
            logs(f'INFO : Save Folder : {CACHE_PATH}')
            save_folder = CACHE_PATH
        
    else:
        anime_name = entry_anime_name.get().strip()
        character_name = entry_character_name.get().strip()
        image_type = image_type_var.get().lower()  # Get the selected image type from the dropdown menu
        num_images_to_download = int(entry_num_images.get().strip())
        anime_explicit = anime_explicit_var.get() == 1  # Check if the "Gif only" checkbox is checked
        gif_only = gif_only_var.get() == 1  # Check if the "Gif only" checkbox is checked
        options_black_white = filter_black_white.get() == 1
        options_pinterest = pinterest.get() == 1
        options_tenor = tenor.get() == 1

        if not anime_name or not image_type:
            messagebox.showerror("Invalid Input", "Please fill in all the required fields")
            logs('Error : Invalid Input')
            return
        if not character_name:
            character_name = ""

        if not save_folder:
            messagebox.showinfo("Save Folder", f"No Save Folder was specified, you will find your images in the Evergarden folder ({CACHE_PATH})")
            logs(f'INFO : Save Folder : {CACHE_PATH}')
            save_folder = CACHE_PATH

    # Disable the DL button while downloading
    button_download.config(state=tk.DISABLED)

    download_thread = Thread(target=download_images, args=(anime_name, character_name, image_type, num_images_to_download, save_folder, anime_explicit, gif_only, options_black_white, options_pinterest, options_tenor))
    download_thread.start()

    progress_thread = Thread(target=update_progress, args=(download_thread, num_images_to_download, save_folder, options_black_white, image_type, anime_name, character_name, anime_explicit, options_pinterest, options_tenor))
    progress_thread.start()

def apply_black_and_white_filter(dir_folder):
    global search_term
    logs('Converting images to black & white mode')
    dir = f"{dir_folder}/{search_term}"
    if not os.path.exists(dir):
        os.makedirs(dir)
        logs('Making dir')
    file_list = os.listdir(dir)

    for file_name in file_list:
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(dir, file_name)
            output_path = os.path.join(dir, file_name)

            img = Image.open(input_path)
            img_bw = img.convert('L')
            img_bw.save(output_path)

def rename_folder(dir_folder, new_name):
    global search_term
    logs('Renaming the folder with BetterName variable [Type] Anime - Character (Source) [filter]')
    try:
        dir = f"{dir_folder}/{search_term}"
        parent_dir = os.path.dirname(dir)
        new_path = os.path.join(parent_dir, new_name)
        os.rename(dir, new_path)
        print(f"Folder '{dir}' renamed to '{new_path}'.")
        logs(f'Folder "{dir}" renamed to "{new_path}"')

    except Exception as e:
        print(f"Error: {e}")
        logs(f'Error : {e}')
        try:
            logs('Fixing error')
            dir = f"{dir_folder}/{search_term}"
            parent_dir = os.path.dirname(dir)
            new_name += ' (2)'
            new_path = os.path.join(parent_dir, new_name)
            os.rename(dir, new_path)
            print(f"Folder '{dir}' renamed to '{new_path}'.")
        except Exception as e:
            print(e)
            logs("Can't rename folder, already existing")

def update_progress(download_thread, num_images_to_download, save_folder, options_black_white, image_type, anime_name, character_name, anime_explicit, options_pinterest, options_tenor):
    while download_thread.is_alive():
        percentage_label.config(text=f"Downloading...")
    percentage_label.config(text="Download Completed")
    button_download.config(state=tk.NORMAL)
    if options_black_white:
        print("Black & White filter on", save_folder)
        apply_black_and_white_filter(save_folder)
    messagebox.showinfo("Download Complete", "Image download completed.")
    logs('Download completed')
    if image_type == 'profile picture':
        image_type = 'PFP'
    elif image_type == 'wallpaper':
        image_type = 'Wallpaper'
    elif image_type == 'screencaps':
        image_type = 'Screencaps'
    else:
        image_type = 'All'
    if 'gif' in search_term:
            image_type += 'g'
    betterName = f"[{image_type}] {anime_name} - {character_name}"
    if options_pinterest:
        if options_tenor:
            betterName += " (Pin&Ten)"
        else:
            betterName += " (Pinterest)"

    if options_tenor == True and options_pinterest == False:
        betterName += " (Tenor)"

    if options_black_white:
        betterName += f' [bw]'
    rename_folder(save_folder, betterName)

        

def on_select_folder_clicked():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        entry_save_folder.delete(0, tk.END)
        entry_save_folder.insert(tk.END, selected_folder)

root = tk.Tk()

__nameApp__ = "Evergarden (Anime Image Downloader)"
__version__ = "1.7.9 Stable"
__author__ = "ZeyaTsu"


def isUpdated():
    global __version__
    logs('Checking isUpdated')
    response = requests.get("https://raw.githubusercontent.com/ZeyaTsu/evergarden/main/config/isUpdated.json")
    
    if response.status_code == 200:
        data = response.json()
        version = data.get("new_version")
        
        if version:
            version = f"{version} Stable"
            if version == __version__:
                return True
            else:
                logs('Not updated version')
                return False
        else:
            return False
    else:
        return False

def isAuthor():
    global __version__
    logs('Checking isAuthor')
    response = requests.get("https://raw.githubusercontent.com/ZeyaTsu/evergarden/main/config/isUpdated.json")
    
    if response.status_code == 200:
        data = response.json()
        author = data.get("author")
        
        if author:
            if author == __author__:
                return True
            else:
                logs('Invalid author')
                return False
        else:
            return False
    else:
        return False

logs('\n\n ============== EVERGARDEN ============== \n')
logs(f'Starting Evergarden (Anime Image Downloader) version: {__version__}')

version_value = isUpdated()
author_value = isAuthor()

if version_value == False:
    __nameApp__ = "Evergarden (Not updated)"

if author_value == False:
    __nameApp__ = "Evergarden - NOT ORIGINAL PRODUCT"

# Select Preset

menu = Menu(root)
root.config(menu=menu)
select_set = Menu(menu, tearoff=0)
select_theme = Menu(menu, tearoff=0)
menu.add_cascade(label="Presets", menu=select_set)
menu.add_cascade(label="Themes", menu=select_theme)

""" 

COLORS

"""

def makeThemeFile():
    global CACHE_PATH
    ct = ConfigParser()
    ct.add_section('Themes')
    ct.set('Themes', 'theme', 'Evergarden')
    with open(f'{CACHE_PATH}evergarden_themes.ini', 'w') as f:
        ct.write(f)  

if os.path.exists(f'{CACHE_PATH}evergarden_themes.ini'):
    ct = ConfigParser()
    ct.read(f'{CACHE_PATH}evergarden_themes.ini')
    themes = ["Evergarden", "Ilulu", "Tohru", "Chito", "Tsukasa"]
    for theme in themes:
        if len(str(theme)) <= 10:
            logs(f'Got [{theme}]')
            select_theme.add_command(label=theme, command=lambda p=theme: LoadDefaultTheme(p))
        else:
            logs(f"Couldn't get {theme} as length > 10 characters")
else:
    makeThemeFile()
    if os.path.exists(f'{CACHE_PATH}evergarden_themes.ini'):
        ct = ConfigParser()
        ct.read(f'{CACHE_PATH}evergarden_themes.ini')
        themes = ["Evergarden", "Ilulu", "Tohru", "Chito", "Tsukasa"]
        for theme in themes:
            if len(str(theme)) <= 10:
                logs(f'Got [{theme}]')
                select_theme.add_command(label=theme, command=lambda p=theme: LoadDefaultTheme(p))
            else:
                logs(f"Couldn't get {theme} as length > 10 characters")

ct = ConfigParser()
ct.read(f'{CACHE_PATH}evergarden_themes.ini')
themes = ct.sections()
for theme in themes:
    logs(f'Getting [{theme}] theme')
theme = ct["Themes"]
theme_name = theme["theme"]
logs(f'Using {theme_name}')

if theme_name == "Evergarden":
    main_color = "#0d1b2a"
    second_color = "#1b263b"
    button_color = "#778da9"
    text_color = "white"
if theme_name == "Ilulu":
    main_color = "#49475C"
    second_color = "#625E6F"
    button_color = "#F67E97"
    text_color = "white"
if theme_name == "Tohru":
    main_color = "#395274"
    second_color = "#99aac4"
    button_color = "#F1AC72"
    text_color = "white"
if theme_name == "Chito":
    main_color = "#23342E"
    second_color = "#404F4A"
    button_color = "#0E1819"
    text_color = "white"
if theme_name == "Tsukasa":
    main_color = "#862C45"
    second_color = "#EE344C"
    button_color = "#DB9CAF"
    text_color = "white"
elif theme_name not in ["Evergarden", "Ilulu", "Tohru", "Chito", "Tsukasa"]:
    try:
        ctc = ConfigParser()
        ctc.read(f'{CACHE_PATH}custom_evergarden_themes.ini')
        theme_custom_use = ctc[theme_name]
        main_color = str(theme_custom_use["main_color"])
        second_color = str(theme_custom_use["second_color"])
        button_color = str(theme_custom_use["button_color"])
        text_color = str(theme_custom_use["text_color"])
    except:
        main_color = "#0d1b2a"
        second_color = "#1b263b"
        button_color = "#778da9"
        text_color = "white"


"""

MAIN GUI

"""

root.title(__nameApp__)
root.configure(background=main_color)
# window non-resizable
root.resizable(False, False)

# notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Main Tab (General)
main_tab = ttk.Frame(notebook, style='Main.TFrame')
notebook.add(main_tab, text='General')

# GUI
label_anime_name = tk.Label(main_tab, text="Anime Name:", fg=text_color, bg=main_color)
label_anime_name.grid(row=0, column=0, padx=5, pady=5)
entry_anime_name = tk.Entry(main_tab, bg=second_color, fg=text_color)
entry_anime_name.grid(row=0, column=1, padx=5, pady=5)

label_character_name = tk.Label(main_tab, text="Character Name:", fg=text_color, bg=main_color)
label_character_name.grid(row=1, column=0, padx=5, pady=5)
entry_character_name = tk.Entry(main_tab, bg=second_color, fg=text_color)
entry_character_name.grid(row=1, column=1, padx=5, pady=5)

label_image_type = tk.Label(main_tab, text="Image Type (Click to select):", fg=text_color, bg=main_color)
label_image_type.grid(row=2, column=0, padx=5, pady=5)

# Dropdown menu for Image Type
image_types = ["Profile Picture", "Wallpaper", "Screencaps","All"]
image_type_var = tk.StringVar(main_tab, value="Profile Picture")  # Default value
dropdown_image_type = tk.OptionMenu(main_tab, image_type_var, *image_types)
dropdown_image_type.config(bg=second_color, fg=text_color, activebackground=main_color, activeforeground=text_color, relief=tk.FLAT)
dropdown_image_type.grid(row=2, column=1, padx=5, pady=5)

label_num_images = tk.Label(main_tab, text="Number of Images to Download:", fg=text_color, bg=main_color)
label_num_images.grid(row=3, column=0, padx=5, pady=5)
entry_num_images = tk.Entry(main_tab, bg=second_color, fg=text_color)
entry_num_images.grid(row=3, column=1, padx=5, pady=5)

label_save_folder = tk.Label(main_tab, text="Save Folder:", fg=text_color, bg=main_color)
label_save_folder.grid(row=4, column=0, padx=5, pady=5)
entry_save_folder = tk.Entry(main_tab, bg=second_color, fg=text_color)
entry_save_folder.grid(row=4, column=1, padx=5, pady=5)
button_select_folder = tk.Button(main_tab, text="Select Folder", command=on_select_folder_clicked, bg=button_color, fg=text_color, bd=0, relief=tk.FLAT)
button_select_folder.grid(row=4, column=2, padx=5, pady=5)

# Checkbox Gif Only (variable)
gif_only_var = tk.IntVar()
anime_explicit_var = tk.IntVar()

# Checkbox Gif Only (creating)
checkbox_gif_only = tk.Checkbutton(main_tab, text="Gif only", variable=gif_only_var, selectcolor=second_color, bg=main_color, fg=text_color, activebackground=main_color, activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_gif_only.grid(row=3, column=2, padx=5, pady=5)

button_download = tk.Button(main_tab, text="Download Images", command=on_download_clicked, bg=button_color, fg=text_color, bd=0, relief=tk.FLAT)
button_download.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

percentage_label = tk.Label(main_tab, text="", fg=text_color, bg=main_color)
percentage_label.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

try:
    c = ConfigParser()
    c.read(f'{CACHE_PATH}evergarden_presets.ini')
    c = c["evergarden"]
    set_loaded = True
    logs(f'Set loaded : {set_loaded}')
except:
    pass

# Options Tab (WIP, coming soon)
options_tab = ttk.Frame(notebook, style='Second.TFrame')
notebook.add(options_tab, text="Options")

anime_explicit_var = tk.IntVar()
checkbox_blackwhite = tk.Checkbutton(options_tab, text="Anime explicit", variable=anime_explicit_var, selectcolor=second_color, bg=main_color, fg=text_color, activebackground=main_color, activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_blackwhite.grid(row=1, column=1, padx=5, pady=5)

filter_black_white = tk.IntVar()
checkbox_blackwhite = tk.Checkbutton(options_tab, text="Black & White", variable=filter_black_white, selectcolor=second_color, bg=main_color, fg=text_color, activebackground=main_color, activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_blackwhite.grid(row=1, column=2, padx=5, pady=5)

pinterest = tk.IntVar()
checkbox_pinterest = tk.Checkbutton(options_tab, text="From Pinterest", variable=pinterest, selectcolor=second_color, bg=main_color, fg=text_color, activebackground=main_color, activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_pinterest.grid(row=1, column=3, padx=5, pady=5)

tenor = tk.IntVar()
checkbox_tenor = tk.Checkbutton(options_tab, text="From Tenor", variable=tenor, selectcolor=second_color, bg=main_color, fg=text_color, activebackground=main_color, activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_tenor.grid(row=2, column=1, padx=5, pady=5)


# About Tab
second_tab = ttk.Frame(notebook, style='Third.TFrame')
notebook.add(second_tab, text='About')

# Text about tab
text_in_second_tab = tk.Label(second_tab, text=f"Author: {__author__}\n\nVersion: {__version__}", fg=text_color, bg=main_color)
text_in_second_tab.grid(row=1, column=2, padx=150, pady=100)


def restart():
    import subprocess
    python_executable = sys.executable
    script_file = sys.argv[0]
    root.destroy()
    subprocess.Popen([python_executable, script_file])

def LoadPreset(profile):
    global profile_selected
    if profile == 'None':
        profile_selected = None
        label_preset.config(text="")
    else:
        profile_selected = profile
        label_preset.config(text=f"{profile}")

def LoadCustomTheme(theme_chosen):
    global custom_theme_selected, theme_selected
    logs(f'Chose {theme_chosen} theme')
    custom_theme_selected = theme_chosen
    if theme == 'None':
        theme_selected = "Evergarden"
    else:
        theme_selected = theme_chosen
    ct.read(f"{CACHE_PATH}evergarden_themes.ini")
    ct.set("Themes", "theme", str(theme_selected))
    with open(f"{CACHE_PATH}evergarden_themes.ini", 'w') as f:
        ct.write(f)
    logs(f'Setting {theme_selected}')
    messagebox.showinfo('Evergarden (Anime Image Downloader)', f"Evergarden will now restart to use `{theme_selected}` theme.")
    restart()
    

def LoadDefaultTheme(theme):
    global theme_selected
    if theme == 'None':
        theme_selected = "Evergarden"
    else:
        theme_selected = theme
    ct.read(f"{CACHE_PATH}evergarden_themes.ini")
    ct.set("Themes", "theme", str(theme_selected))
    with open(f"{CACHE_PATH}evergarden_themes.ini", 'w') as f:
        ct.write(f)
    logs(f'Setting {theme_selected}')
    messagebox.showinfo('Evergarden (Anime Image Downloader)', f"Evergarden will now restart to use `{theme_selected}` theme.")
    restart()

def makePresetFile():
    global CACHE_PATH
    c.add_section('Preset name')
    c.set('Preset name', 'anime_name','Anime name')
    c.set('Preset name', 'character_name','Character name')
    c.set('Preset name', 'type','profile picture/wallpaper/screencaps/all')
    c.set('Preset name', 'n_images','number of images')
    c.set('Preset name', 'gif','True/False')
    c.set('Preset name', 'filter','None/bw')
    c.set('Preset name', 'pinterest','True/False')
    c.set('Preset name', 'tenor', 'True/False')
    c.set('Preset name', 'INFO', 'PRESET NAME MUST BE UNDER 10 CHARACTERS. (you can delete this line)')
    with open(f'{CACHE_PATH}evergarden_presets.ini', 'w') as f:
        c.write(f)
    logs('Made evergarden_presets.ini')
    messagebox.showinfo("Evergarden Help", f"Note that if you want to add another preset, just copy & paste the existing preset and edit it. By clicking 'OK' Evergarden will close to load presets. ({CACHE_PATH})")
    restart()

def makeCustomThemeFile():
    global CACHE_PATH
    c.add_section('Theme name')
    c.set('Theme name', 'main_color','#FFFFFF')
    c.set('Theme name', 'second_color','#FFFFFF')
    c.set('Theme name', 'button_color','#FFFFFF')
    c.set('Theme name', 'text_color','#FFFFFF')
    c.set('Theme name', 'INFO', 'PRESET NAME MUST BE UNDER 10 CHARACTERS. (you can delete this line)')
    with open(f'{CACHE_PATH}custom_evergarden_themes.ini', 'w') as f:
        c.write(f)
    logs('Made custom_evergarden_themes.ini')
    messagebox.showinfo("Evergarden Help", f"Note that if you want to add another preset, just copy & paste the existing preset and edit it. By clicking 'OK' Evergarden will close to load themes. ({CACHE_PATH})")
    restart()

if os.path.exists(f'{CACHE_PATH}evergarden_presets.ini'):
    select_set.add_command(label="None", command=lambda p='None': LoadPreset(p))
    c = ConfigParser()
    c.read(f'{CACHE_PATH}evergarden_presets.ini')
    profiles = c.sections()
    for profile in profiles:
        if len(str(profile)) <= 10:
            logs(f'Got [{profile}]')
            select_set.add_command(label=profile, command=lambda p=profile: LoadPreset(p))
        else:
            logs(f"Couldn't get {profile} as length > 10 characters")
else:
    select_set.add_command(label="Make preset file", command=makePresetFile)


if os.path.exists(f'{CACHE_PATH}custom_evergarden_themes.ini'):
    ctc = ConfigParser()
    ctc.read(f'{CACHE_PATH}custom_evergarden_themes.ini')
    themes_c = ctc.sections()
    for theme_c in themes_c:
        if len(str(theme_c)) <= 10:
            logs(f'Got [{theme_c}] Theme')
            select_theme.add_command(label=theme_c, command=lambda p=theme_c: LoadCustomTheme(p))
        else:
            logs(f"Couldn't get {theme_c} Theme as lenght > 10 characters") 
else:
    select_theme.add_command(label="Make custom theme file", command=makeCustomThemeFile)

label_preset = tk.Label(main_tab, text="", fg=text_color, bg=main_color)
label_preset.grid(row=6, column=1, columnspan=3,padx=5, pady=10)

style = ttk.Style()
style.configure('Main.TFrame', background=main_color)
style.configure('Second.TFrame', background=main_color)
style.configure('Third.TFrame', background=main_color)
style.configure('TNotebook.Tab', background=main_color) 
style.configure('Custom.TNotebook', background=main_color)  

root.iconbitmap(icon)
root.mainloop()