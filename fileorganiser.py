import os
import shutil

# 📂 Change this path
source_folder = "C:/Users/Asus/Downloads"

# 📁 File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Data Files": [".csv"],
    "Code": [".py", ".c", ".cpp", ".java", ".js", ".html", ".css", ".ipynb"],
    "Markdown": [".md"],
    "Archives": [".zip", ".rar", ".7z"],
    "Applications": [".exe", ".msi", ".msix"],
    "Audio": [".mp3", ".wav"],
    "Torrents": [".torrent"],
    "Config": [".ini"],
    "Shortcuts": [".lnk"]
}

# 📊 Summary
summary = {folder: 0 for folder in file_types}
summary["Others"] = 0

def organize_files():
    total_files = 0

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # ❌ Skip hidden/system files
        if filename.startswith("."):
            print(f"Skipped: {filename} (hidden/system file)")
            continue

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # ❌ Skip .part files
        if extension == ".part":
            print(f"Skipped: {filename} (still downloading)")
            continue

        total_files += 1
        moved = False

        for folder, extensions in file_types.items():
            if extension in extensions:
                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder}")

                summary[folder] += 1
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} → Others")

            summary["Others"] += 1

    # 📊 Summary
    print("\n📊 Summary:")
    print(f"Total files processed: {total_files}")

    for folder, count in summary.items():
        print(f"{folder}: {count} files")


if __name__ == "__main__":
    organize_files()