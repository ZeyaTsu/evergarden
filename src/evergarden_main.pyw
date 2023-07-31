import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from threading import Thread
from bing_image_downloader import downloader
from PIL import Image
import sys

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

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("violet.ico")
search_term = ""

def download_images(anime_name, character_name, image_type, num_images_to_download, save_folder, gif_only, options_black_white):
    global search_term
    search_term = f"{anime_name} {character_name} {image_type} anime"
    if gif_only:
        search_term += " gif"
    if options_black_white:
        search_term += " black white manga"
    downloader.download(search_term, limit=num_images_to_download, output_dir=save_folder,
                        adult_filter_off=True, force_replace=False, timeout=60)

def on_download_clicked():
    anime_name = entry_anime_name.get().strip()
    character_name = entry_character_name.get().strip()
    image_type = image_type_var.get().lower()  # Get the selected image type from the dropdown menu
    num_images_to_download = int(entry_num_images.get().strip())
    save_folder = entry_save_folder.get().strip()  # Get the selected save folder
    gif_only = gif_only_var.get() == 1  # Check if the "Gif only" checkbox is checked
    options_black_white = filter_black_white.get() == 1

    if not anime_name or not character_name or not image_type:
        messagebox.showerror("Invalid Input", "Please fill in all the required fields")
        return

    if not save_folder:
        messagebox.showerror("Invalid Save Folder", "Please select a folder to save the images")
        return

    # Disable the DL button while downloading
    button_download.config(state=tk.DISABLED)

    download_thread = Thread(target=download_images, args=(anime_name, character_name, image_type, num_images_to_download, save_folder, gif_only, options_black_white))
    download_thread.start()

    progress_thread = Thread(target=update_progress, args=(download_thread, num_images_to_download, save_folder, options_black_white))
    progress_thread.start()

def apply_black_and_white_filter(dir_folder):
    global search_term
    dir = f"{dir_folder}/{search_term}"
    if not os.path.exists(dir):
        os.makedirs(dir)

    file_list = os.listdir(dir)

    for file_name in file_list:
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(dir, file_name)
            output_path = os.path.join(dir, file_name)

            img = Image.open(input_path)
            img_bw = img.convert('L')
            img_bw.save(output_path)

def update_progress(download_thread, num_images_to_download, save_folder, options_black_white):
    while download_thread.is_alive():
        percentage_label.config(text=f"Downloading...")
    percentage_label.config(text="Download Completed")
    button_download.config(state=tk.NORMAL)
    if options_black_white:
        print("Black & White filter on", save_folder)
        apply_black_and_white_filter(save_folder)
    messagebox.showinfo("Download Complete", "Image download completed.")

        

def on_select_folder_clicked():
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        entry_save_folder.delete(0, tk.END)
        entry_save_folder.insert(tk.END, selected_folder)

root = tk.Tk()
root.title("Evergarden (Anime Image Downloader)")
root.configure(background="#0d1b2a")

# window non-resizable
root.resizable(False, False)

# notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Main Tab (General)
main_tab = ttk.Frame(notebook, style='Main.TFrame')
notebook.add(main_tab, text='General')

# GUI
label_anime_name = tk.Label(main_tab, text="Anime Name:", fg="white", bg="#0d1b2a")
label_anime_name.grid(row=0, column=0, padx=5, pady=5)
entry_anime_name = tk.Entry(main_tab, bg="#1b263b", fg="white")
entry_anime_name.grid(row=0, column=1, padx=5, pady=5)

label_character_name = tk.Label(main_tab, text="Character Name:", fg="white", bg="#0d1b2a")
label_character_name.grid(row=1, column=0, padx=5, pady=5)
entry_character_name = tk.Entry(main_tab, bg="#1b263b", fg="white")
entry_character_name.grid(row=1, column=1, padx=5, pady=5)

label_image_type = tk.Label(main_tab, text="Image Type (Click to select):", fg="white", bg="#0d1b2a")
label_image_type.grid(row=2, column=0, padx=5, pady=5)

# Dropdown menu for Image Type
image_types = ["Profile Picture", "Wallpaper", "All"]
image_type_var = tk.StringVar(main_tab, value="Profile Picture")  # Default value
dropdown_image_type = tk.OptionMenu(main_tab, image_type_var, *image_types)
dropdown_image_type.config(bg="#1b263b", fg="white", activebackground="#0d1b2a", activeforeground="#FFFFFF", relief=tk.FLAT)
dropdown_image_type.grid(row=2, column=1, padx=5, pady=5)

label_num_images = tk.Label(main_tab, text="Number of Images to Download:", fg="white", bg="#0d1b2a")
label_num_images.grid(row=3, column=0, padx=5, pady=5)
entry_num_images = tk.Entry(main_tab, bg="#1b263b", fg="white")
entry_num_images.grid(row=3, column=1, padx=5, pady=5)

label_save_folder = tk.Label(main_tab, text="Save Folder:", fg="white", bg="#0d1b2a")
label_save_folder.grid(row=4, column=0, padx=5, pady=5)
entry_save_folder = tk.Entry(main_tab, bg="#1b263b", fg="white")
entry_save_folder.grid(row=4, column=1, padx=5, pady=5)
button_select_folder = tk.Button(main_tab, text="Select Folder", command=on_select_folder_clicked, bg="#778da9", fg="white", bd=0, relief=tk.FLAT)
button_select_folder.grid(row=4, column=2, padx=5, pady=5)

# Checkbox Gif Only (variable)
gif_only_var = tk.IntVar()

# Checkbox Gif Only (creating)
checkbox_gif_only = tk.Checkbutton(main_tab, text="Gif only", variable=gif_only_var, selectcolor="#1b263b", bg="#0d1b2a", fg="white", activebackground="#0d1b2a", activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_gif_only.grid(row=3, column=2, padx=5, pady=5)

button_download = tk.Button(main_tab, text="Download Images", command=on_download_clicked, bg="#778da9", fg="white", bd=0, relief=tk.FLAT)
button_download.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

percentage_label = tk.Label(main_tab, text="", fg="white", bg="#0d1b2a")
percentage_label.grid(row=5, column=0, columnspan=3, padx=5, pady=10)

# Options Tab (WIP, coming soon)
options_tab = ttk.Frame(notebook, style='Second.TFrame')
notebook.add(options_tab, text="Options")

options_label = tk.Label(options_tab, text="More options coming soon.", fg="white", bg="#0d1b2a")
options_label.grid(row=1, column=1, padx=5, pady=5)

filter_black_white = tk.IntVar()
checkbox_blackwhite = tk.Checkbutton(options_tab, text="Black & White", variable=filter_black_white, selectcolor="#1b263b", bg="#0d1b2a", fg="white", activebackground="#0d1b2a", activeforeground="#FFFFFF", disabledforeground="#FFFFFF")
checkbox_blackwhite.grid(row=1, column=2, padx=5, pady=5)

# About Tab
second_tab = ttk.Frame(notebook, style='Third.TFrame')
notebook.add(second_tab, text='About')

__version__ = "1.4.3 Stable"
__author__ = "ZeyaTsu"

# Text about tab
text_in_second_tab = tk.Label(second_tab, text=f"Author: {__author__}\n\nVersion: {__version__}", fg="white", bg="#0d1b2a")
text_in_second_tab.pack(padx=100, pady=100)

style = ttk.Style()
style.configure('Main.TFrame', background="#0d1b2a")
style.configure('Second.TFrame', background="#0d1b2a")
style.configure('Third.TFrame', background="#0d1b2a")
style.configure('TNotebook.Tab', background="#0d1b2a") 
style.configure('Custom.TNotebook', background="#0d1b2a")  

root.iconbitmap(icon)
root.mainloop()