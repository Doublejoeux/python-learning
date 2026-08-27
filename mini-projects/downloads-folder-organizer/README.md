# Downloads Folder Organizer

A Python script for a Downloads folder organizer that sorts files in the downloads folder into appropriate sub-folders.

## Features
- Locates the `Downloads` folder properly. 
- Moves only files in the downloads folder into appropriate sub-folders.
- Creates the sub-folders if not already present.
- Makes sure not to sort the sub-folders.
- Doesn't crash when there's nothing to sort.

## How It Works
- Uses `expanduser("~")` and `os.path.join()` so it effectively locates the `Downloads` folder on devices other than the local device.
- Uses `os.path.exists()` to check if sub-folders exists before creating.
- Uses `os.path.splitext()` to sort by extension.
- Uses a dictionary (`categories`) that helps multiple extensions share same sub-folder.

## What I Learned
- Encountered an error while trying to sort the files and discovered I couldn't access the files in the `Downloads` folder without using `os.listdir()`.
- Encountered another error/problem while script was moving the files and discovered it was moving the sub-folders too. Had to use `os.path.isfile()` to make sure it sorts just files.

## How to Run It
```bash
python downloads_folder_organizer.py
```
## Possible Improvements
- Making the script run on a schedule.