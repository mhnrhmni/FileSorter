import subprocess
import sys

# Function to install packages using pip
def install(package):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install required packages
required_packages = ['requests']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)

import os
import shutil
import logging
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import webbrowser
from concurrent.futures import ThreadPoolExecutor

# Logging configuration
logging.basicConfig(filename='OrganizeMyFiles.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dictionary for file types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg', '.tiff', '.ico', '.psd', '.raw', '.heic'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.tex'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.3gp'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso', '.cab'],
    'Coding': ['.json', '.scss', '.css', '.html', '.js', '.py', '.java', '.c', '.cpp', '.php', '.xml', '.sql', '.rb', '.go', '.sh', '.ts', '.md'],
    'Installation Files': ['.msi', '.exe', '.dmg', '.pkg', '.deb', '.rpm', '.app', '.bat', '.sh', '.bin'],
    'E-Books': ['.epub', '.mobi', '.azw', '.azw3', '.djvu', '.ibooks'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot', '.fon'],
    'Databases': ['.db', '.sqlite', '.sql', '.mdb', '.accdb'],
    'CAD Files': ['.dwg', '.dxf', '.step', '.stl', '.igs', '.iges'],
    '3D Models': ['.obj', '.fbx', '.dae', '.3ds', '.blend'],
    'Vector Graphics': ['.ai', '.eps', '.svg', '.cdr'],
    'Design Projects': ['.psd', '.ai', '.xd', '.fig', '.sketch'],
    'Saved Web Pages': ['.html', '.htm', '.mhtml', '.webarchive'],
    'Configurations': ['.ini', '.cfg', '.conf', '.yaml', '.yml'],
    'Log Files': ['.log', '.out'],
    'PDF Files': ['.pdf'],
    'Miscellaneous': []
}

# Function to sort files
def sort_files(download_folder, file_type_selection):
    try:
        # Using ThreadPoolExecutor for concurrent file processing
        with ThreadPoolExecutor(max_workers=4) as executor:
            for filename in os.listdir(download_folder):
                file_path = os.path.join(download_folder, filename)
                if os.path.isfile(file_path):
                    executor.submit(process_file, file_path, download_folder, file_type_selection)
        
        remove_empty_folders(download_folder)
        messagebox.showinfo("Success", "Files sorted successfully!")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to process individual file
def process_file(file_path, download_folder, file_type_selection):
    file_ext = os.path.splitext(file_path)[1].lower()
    destination_folder = None

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            if file_type_selection == "All Files" or file_type_selection == folder:
                destination_folder = os.path.join(download_folder, folder)
                break

    if destination_folder:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        dest_file_path = os.path.join(destination_folder, os.path.basename(file_path))
        if os.path.exists(dest_file_path):
            base_name, ext = os.path.splitext(os.path.basename(file_path))
            counter = 1
            new_filename = f"{base_name}_{counter}{ext}"
            while os.path.exists(os.path.join(destination_folder, new_filename)):
                counter += 1
                new_filename = f"{base_name}_{counter}{ext}"
            dest_file_path = os.path.join(destination_folder, new_filename)

        shutil.move(file_path, dest_file_path)
        logging.info(f'Successfully moved: {os.path.basename(file_path)} -> {destination_folder}')

# Function to remove empty folders
def remove_empty_folders(path):
    if not os.path.isdir(path):
        return

    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path):
            remove_empty_folders(folder_path)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                logging.info(f'Removed empty folder: {folder_path}')

# Function to choose download folder
def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# Function to start sorting files
def start_sorting():
    folder = folder_path.get()
    file_type_selection = file_type_var.get()
    if folder:
        sort_files(folder, file_type_selection)
    else:
        messagebox.showwarning("Warning", "Please select a folder first.")

# Function to open link in web browser
def open_link(url):
    webbrowser.open_new(url)

# Create GUI
root = tk.Tk()
root.title("File Sorter")

style = ttk.Style()
style.configure("TButton", font=('Helvetica', 12))
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))
style.configure("TCombobox", font=('Helvetica', 12))

folder_path = tk.StringVar()
file_type_var = tk.StringVar()

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

center_frame = ttk.Frame(main_frame)
center_frame.pack(padx=20, pady=20)

label = ttk.Label(center_frame, text="Select Download Folder:")
label.pack(side=tk.LEFT)

entry = ttk.Entry(center_frame, textvariable=folder_path, width=50)
entry.pack(side=tk.LEFT, padx=10)

browse_button = ttk.Button(center_frame, text="Browse", command=choose_folder)
browse_button.pack(side=tk.LEFT)

# Add dropdown menu for selecting file type
file_type_options = ["All Files", "Images", "Documents", "Videos", "Audio", "Archives", "Coding", "Installation Files", "E-Books", "Fonts", "Databases", "CAD Files", "3D Models", "Vector Graphics", "Design Projects", "Saved Web Pages", "Configurations", "Log Files", "PDF Files", "Miscellaneous"]
file_type_var.set("All Files")
file_type_menu = ttk.Combobox(center_frame, textvariable=file_type_var, values=file_type_options, state="readonly")
file_type_menu.pack(side=tk.LEFT, padx=10)

sort_button = ttk.Button(root, text="Start Sorting", command=start_sorting)
sort_button.pack(pady=10)

# Add developer names with hyperlinks
footer_frame = ttk.Frame(root, padding="10")
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# GitHub links for developers
creator_1_url = "https://github.com/GylanSalih"
creator_2_url = "https://github.com/mhnrhmni"

developers_label = ttk.Label(footer_frame, text="Developers:", font=('Helvetica', 12))
developers_label.pack(side=tk.LEFT, padx=5)

creator_1_link = ttk.Label(footer_frame, text="Gylan Salih (Germany)", foreground="blue", cursor="hand2", font=('Helvetica', 12))
creator_1_link.pack(side=tk.LEFT, padx=5)
creator_1_link.bind("<Button-1>", lambda e: open_link(creator_1_url))

creator_2_link = ttk.Label(footer_frame, text="Mahan Rahmani (Iran)", foreground="blue", cursor="hand2", font=('Helvetica', 12))
creator_2_link.pack(side=tk.LEFT, padx=5)
creator_2_link.bind("<Button-1>", lambda e: open_link(creator_2_url))

# Add thank you message and request for GitHub stars
thanks_message = ttk.Label(footer_frame, text="Thank you for using our tool! Please follow us and give us a star on GitHub ⭐", font=('Helvetica', 12))
thanks_message.pack(side=tk.LEFT, padx=20)

root.mainloop()
