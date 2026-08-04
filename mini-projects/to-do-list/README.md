# To-Do List (with persistence)

A command-line to-do list app that saves your tasks to a JSON file, 
so your list survives between runs.

## Features
- Add, view, remove, and mark tasks as done.
- Tasks persist across sessions, saved to `tasks.json` after every change.
- Handles first-time run gracefully (no crash if `tasks.json` doesn't exist yet).

## How it works
- `load_tasks()` runs once at startup. It tries to read `tasks.json`; 
  if the file doesn't exist yet (first run), it catches `FileNotFoundError` 
  and returns an empty list instead of crashing.
- `save_tasks()` runs after every change made (add/remove/mark). It overwrites 
  `tasks.json` completely with the current state of the `tasks` list. 
  A full rewrite each time rather than an append, since JSON doesn't support 
  partial edits to a file on disk.

## What I learned
- The `try/except FileNotFoundError` pattern for handling a file that may 
  not exist yet on a program's first run.
- Why JSON persistence uses a full read-modify-write cycle instead of 
  appending? You load the whole structure into memory, change it, then 
  write the whole thing back.
- Caught my own bug during development: `load_tasks()` was reading the file 
  but not returning the data, so it silently returned `None` on every run 
  where a save file existed. Fixed by returning `json.load(file)` explicitly.

## Run it
```bash
python to_do_list.py
```

## Possible improvements
- Add due dates or priority levels to tasks.
- Add a "clear all" option.
- Handle corrupted/empty `tasks.json` (currently assumes valid JSON if the file exists).