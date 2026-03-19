# 📁 File Organizer (Python Automation)

A Python automation tool that organizes files in a folder (like Downloads) into categorized subfolders based on file type.

---

## 🚀 Features

- 📂 Automatically sorts files into folders:
  - Images
  - Videos
  - Documents
  - Code
  - Archives
  - Applications
  - Audio
  - Torrents
  - Config files
  - Shortcuts

- ⚡ Skips:
  - `.part` files (active downloads)
  - Hidden/system files (starting with `.`)

- 📊 Displays summary:
  - Total files processed
  - Files moved per category

- 🧠 Smart categorization based on file extensions

---

## 🛠️ Tech Used

- Python
- os module
- shutil module

---

## 📂 Example

### Before:
```
Downloads/
  file.jpg
  movie.mp4
  notes.pdf
  code.py
```

### After:
```
Downloads/
├── Images/
├── Videos/
├── Documents/
├── Code/
```

---

## ▶️ How to Run

### 1. Run Python Script
```
python fileorganiser.py
```

### 2. OR Run EXE
```
fileorganiser.exe
```

---

## ⚙️ Configuration

Edit this line in the script:

```python
source_folder = "C:/Users/YourName/Downloads"
```

Replace `YourName` with your system username.

---

## 💡 Future Improvements

- GUI version (Tkinter)
- Auto-run on system startup
- File sorting by date
- Duplicate file handling
- Notification system

---

## 🔥 Use Case

- Clean messy Downloads folder
- Automate file management
- Improve productivity

---

## 📌 Author

**Soham Rokade**

---

## 💡 Quote

> "Automate the boring stuff."
