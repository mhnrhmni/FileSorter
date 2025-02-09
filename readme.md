# 🎉 File Sorter 🗂️
<a id="readme-top"></a>

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

</div>

<!-- Badges Shields -->
[contributors-shield]: https://custom-icon-badges.demolab.com/github/contributors/GylanSalih/OrganizeMyFiles?color=FF0000&logo=group&label=Contributors&logoColor=white&style=for-the-badge&labelColor=000000
[forks-shield]: https://custom-icon-badges.demolab.com/github/forks/GylanSalih/OrganizeMyFiles?color=FF0000&logo=repo-forked&label=Forks&logoColor=white&style=for-the-badge&labelColor=000000
[stars-shield]: https://custom-icon-badges.demolab.com/github/stars/GylanSalih/OrganizeMyFiles?color=FF0000&label=Stars&style=for-the-badge&logo=star&logoColor=white&labelColor=000000
[issues-shield]: https://custom-icon-badges.demolab.com/github/issues/GylanSalih/OrganizeMyFiles?color=FF0000&logo=issue-opened&label=Issues&logoColor=white&labelColor=000000&style=for-the-badge&
[license-shield]: https://custom-icon-badges.demolab.com/github/license/GylanSalih/OrganizeMyFiles?color=FF0000&logo=law&label=License&logoColor=white&style=for-the-badge&labelColor=000000

<!-- Badges Links -->
[contributors-url]: https://github.com/GylanSalih/OrganizeMyFiles/graphs/contributors
[forks-url]: https://github.com/GylanSalih/OrganizeMyFiles/network/members
[stars-url]: https://github.com/GylanSalih/OrganizeMyFiles/stargazers
[issues-url]: https://github.com/GylanSalih/OrganizeMyFiles/issues
[license-url]: https://github.com/GylanSalih/OrganizeMyFiles/blob/main/LICENSE

<p align="center">
  <img src="https://github.com/user-attachments/assets/faa560a4-6185-4fc6-a4bc-1ec41cca53d4" alt="File Sorter Logo" width="300">
</p>

A user-friendly tool to automatically organize your files! This program categorizes files based on their types and places them into designated folders. Say goodbye to the hassle of manual file sorting! 😊

---

## 📋 Table of Contents
- [📖 Introduction](#-introduction)
- [✨ Features](#-features)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📂 File Types](#-file-types)
- [📦 Dependencies](#-dependencies)
- [🔧 Configuration](#-configuration)
- [📜 Logging](#-logging)
- [🖼️ Screenshots](#-screenshots)
- [🤝 Developers](#-developers)
- [📄 License](#-license)

---

## 📖 Introduction
🎯 **File Sorter** is your go-to tool for organizing files in a folder automatically into predefined categories like Images, Documents, Videos, and more. With just a few clicks, you can transform a cluttered folder into an organized one. 🚀

---

## ✨ Features
✅ **User-Friendly GUI**: Built with `tkinter`, making it easy to use for everyone.  
✅ **File Categorization**: Organizes files into categories such as Images, Documents, and Videos.  
✅ **Custom Sorting**: Allows sorting by specific file types or all file types at once.  
✅ **Multithreading**: Uses concurrent file processing for faster sorting.  
✅ **Duplicate Handling**: Prevents overwriting by appending unique identifiers to duplicate filenames.  
✅ **Empty Folder Cleanup**: Automatically removes empty folders after sorting.  
✅ **Detailed Logging**: Keeps track of all operations in a log file for reference.

---

## ⚙️ Installation
To set up and use the File Sorter:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-sorter.git
   cd file-sorter
   ```

2. Install the required dependencies:
    

3. Run the program:
   ```bash
   python file_sorter.py
   ```

---

## 🚀 Usage
1. **Launch the Program**: Run the script, and the GUI will open.  
2. **Select a Folder**: Click the "Browse" button to select the folder you want to organize.  
3. **Choose a File Type**: Use the dropdown menu to select a category (e.g., Images, Documents, etc.) or choose "All Files" to sort everything.  
4. **Start Sorting**: Click the "Start Sorting" button. A success message will pop up once the files are sorted.  

---

## 📂 File Types
The following file types are supported:

| **Category**          | **Extensions**                                                                 |
|------------------------|-------------------------------------------------------------------------------|
| **Images**            | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.bmp`, `.webp`, `.ico`, `.tiff`     |
| **Documents**         | `.pdf`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.rtf`, `.odt`, `.ods`      |
| **Videos**            | `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`, `.webm`, `.wmv`                      |
| **Audio**             | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`                              |
| **Archives**          | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.iso`                                 |
| **Coding**            | `.py`, `.js`, `.html`, `.css`, `.json`, `.java`, `.cpp`, `.rb`, `.php`       |
| **Installation Files**| `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm`                               |
| **E-Books**           | `.epub`, `.mobi`, `.azw`, `.pdf`                                             |
| **Fonts**             | `.ttf`, `.otf`, `.woff`, `.eot`                                              |
| **Databases**         | `.db`, `.sqlite`, `.sql`, `.mdb`                                             |
| **3D Models**         | `.obj`, `.fbx`, `.stl`, `.dae`                                               |
| **Vector Graphics**   | `.ai`, `.eps`, `.svg`, `.cdr`                                                |
| **Configurations**    | `.cfg`, `.ini`, `.yaml`                                                      |
| **Log Files**         | `.log`, `.out`                                                               |

---

## 📦 Dependencies
The program relies on the following Python modules:
- `tkinter` (built-in with Python)
- `requests`
- `shutil`
- `concurrent.futures`

The script automatically installs missing dependencies.

---

## 🔧 Configuration
- **Download Folder**: Select your desired folder through the GUI.  
- **File Type Selection**: Choose specific file categories or sort all files.  
- **Multithreading**: The script uses `ThreadPoolExecutor` with 4 workers by default. Adjust the `max_workers` parameter in the code for higher performance if needed.  

---

## 📜 Logging
All operations are logged in a file named `OrganizeMyFiles.log`. Logs include:
- Successfully moved files  
- Duplicate files and their renamed versions  
- Errors encountered  
- Empty folders that were removed  

---

## 🖼️ Screenshots
Below are some screenshots of the application in action:

<p align="center">
  <img src="https://github.com/user-attachments/assets/b1759910-559a-4f11-924f-46ae4e393595" alt="Main Interface" width="600">
  <br>
  <i>Figure 1: The main interface of the File Sorter</i>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4d43aa4d-5d2e-48ad-9b88-cb6da445539e" alt="File Sorting Process" width="600">
  <br>
  <i>Figure 2: File sorting process is ended</i>
</p>

---

## 🤝 Developers
Developed by:  
- [Gylan Salih (Germany)](https://github.com/GylanSalih)  
- [Mahan Rahmani (Iran)](https://github.com/mhnrhmni)  

🌟 **Thank you for using our tool! Follow us on GitHub and give us a star if you find it useful!** 🌟  

---

## 📄 License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software.  

---

🚀 **Enjoy organizing your files with ease!**
```
