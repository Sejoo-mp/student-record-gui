# Student Record GUI

A simple desktop app built with Python and Tkinter to record student info and calculate GPA.

## Features
- Add a student (id, name, phone, student number, 5 course grades)
- Input validation (empty fields, non-numeric grades, grades outside 0-20)
- Automatic average calculation
- Search a student by id
- Records saved in a local text file (`student.txt`)

## Requirements
- Python 3.8+
- Tkinter (included with Python; on Linux: `sudo apt install python3-tk`)

## Installation & Run
```bash
git clone https://github.com/Sejoo-mp/student-record-gui.git
cd student-record-gui
python3 project_gui.py
```

## Usage
1. **Extend Student**: fill the form and press Submit.
2. **Search**: enter an id to see that student's full record.

## Project structure
- `project_gui.py` - GUI version (main)
- `project.py` - console version
- `student.txt` - saved records (created automatically)

## Future ideas
- Edit/delete records
- Unique id check
- Switch from text file to SQLite/JSON