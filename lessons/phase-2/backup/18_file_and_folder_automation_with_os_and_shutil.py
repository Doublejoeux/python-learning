# File and Folder Automation with os and shutil
import os
import shutil

print(os.getcwd())
files = os.listdir("lessons/phase-2")
print(files)
totals = {}
for item in files:
    if os.path.isfile(os.path.join("lessons/phase-2", item)):
        totals["files"] = totals.get("files", 0) + 1    # Counting files
        print(f"{item} is a file")
    elif os.path.isdir(os.path.join("lessons/phase-2", item)):
        totals["folders"] = totals.get("folders", 0) + 1    # Counting folders
        print(f"{item} is a folder")
print (totals)

# Filter by extension
files_2 = os.listdir("lessons/phase-2")   # Using files_2 just to display on a new loop, nothing else.
for item in files_2:
    name, extension = os.path.splitext(item)
    if extension == ".py":
        print(item)

# Copy Practice
if not os.path.exists("lessons/phase-2/backup"):
    os.mkdir("lessons/phase-2/backup")
shutil.copy("lessons/phase-2/18_file_and_folder_automation_with_os_and_shutil.py", "lessons/phase-2/backup/18_file_and_folder_automation_with_os_and_shutil.py")
files_3 = os.listdir("lessons/phase-2/backup")
print(files_3)

# Rename Practice
if os.path.isfile("lessons/phase-2/test-folder/test_file.py"):
    os.rename("lessons/phase-2/test-folder/test_file.py", "lessons/phase-2/test-folder/renamed_test_file.py")
else:
    print("File doesn't exist")
files_4 = os.listdir("lessons/phase-2/test-folder")
print(files_4)

# __file__
print(os.getcwd())    # Current working directory
print(__file__)    # Script path
print(os.path.dirname(os.path.abspath(__file__)))    # Script's folder path

# expanduser("~")
print(os.path.expanduser("~"))
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
print(downloads_path)