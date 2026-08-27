# Downloads Folder Organizer
import os
import shutil

downloads_path = os.path.expanduser(os.path.join("~", "Downloads"))

if not os.path.exists(os.path.join(downloads_path, "Images")):
    os.mkdir(os.path.join(downloads_path, "Images"))
if not os.path.exists(os.path.join(downloads_path, "Documents")):
    os.mkdir(os.path.join(downloads_path, "Documents"))
if not os.path.exists(os.path.join(downloads_path, "Videos")):
    os.mkdir(os.path.join(downloads_path, "Videos"))
if not os.path.exists(os.path.join(downloads_path, "Audio")):
    os.mkdir(os.path.join(downloads_path, "Audio"))
if not os.path.exists(os.path.join(downloads_path, "Archives")):
    os.mkdir(os.path.join(downloads_path, "Archives"))
if not os.path.exists(os.path.join(downloads_path, "Misc")):
    os.mkdir(os.path.join(downloads_path, "Misc"))

categories = {
    "Images": [".jpeg", ".png",".jpg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3"],
    "Documents": [".pdf", ".docx", ".txt", ".ppt", ".pptx", ".doc", ".xls", ".xlsx", ".csv", ".html"],
    "Archives": [".zip", ".rar"],
    "Misc":[]
}

for item in os.listdir(downloads_path):
    name, extension = os.path.splitext(item)
    source_path = os.path.join(downloads_path,item)
    if os.path.isfile(source_path):
        if extension in categories["Images"]:
            shutil.move(source_path, os.path.join(downloads_path, "Images", item))
        elif extension in categories["Videos"]:
            shutil.move(source_path, os.path.join(downloads_path, "Videos", item))
        elif extension in categories["Audio"]:
            shutil.move(source_path, os.path.join(downloads_path, "Audio", item))
        elif extension in categories["Documents"]:
            shutil.move(source_path, os.path.join(downloads_path, "Documents", item))
        elif extension in categories["Archives"]:
            shutil.move(source_path, os.path.join(downloads_path, "Archives", item))
        else:
            shutil.move(source_path, os.path.join(downloads_path, "Misc", item))