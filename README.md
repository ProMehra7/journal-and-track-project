# Personal Journal & Mood Tracker 📔

## Project Overview
A simple command-line Python application for tracking daily journal entries and monitoring mood patterns. Perfect for students learning Python basics!

## Features
✅ **Add Journal Entries** - Write and save daily thoughts  
✅ **Track Moods** - Log your emotional state (Happy, Sad, Neutral, Angry)  
✅ **View All Entries** - Read all past journal entries  
✅ **Search by Date** - Find entries from specific dates  
✅ **Mood Statistics** - Visualize mood patterns over time  
✅ **Random Jokes** - Get a laugh with pyjokes module  

## Technologies Used
- **Python 3** - Core programming language
- **JSON** - Data storage format
- **pyjokes** - External module for random jokes
- **datetime** - Built-in module for date/time tracking

## Project Structure
```
journal-and-track-project/
├── journal_app.py          # Main application
├── journal_entries.json    # Data storage (auto-created)
├── README.md               # This file
└── requirements.txt        # Dependencies
```

## Installation & Setup

### Step 1: Clone or Download
```bash
git clone https://github.com/ProMehra7/journal-and-track-project.git
cd journal-and-track-project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

OR manually install pyjokes:
```bash
pip install pyjokes
```

### Step 3: Run the Application
```bash
python journal_app.py
```

## How to Use

When you run the app, you'll see this menu:
```
╔════════════════════════════════════════╗
║   📔 Personal Journal & Mood Tracker   ║
╚════════════════════════════════════════╝

Main Menu:
1. ✍️  Add New Entry
2. 📖 View All Entries
3. 🔍 Search by Date
4. 📊 View Mood Statistics
5. 😂 Tell Me a Joke
6. ❌ Exit
```

### Example Usage:

**Option 1: Add Entry**
- Type your thoughts
- Select your current mood (1-4)
- Entry is automatically saved with date & time

**Option 2: View All Entries**
- See all your past journal entries
- Shows date, mood, and content

**Option 3: Search by Date**
- Enter a date in YYYY-MM-DD format
- Find entries from that specific day

**Option 4: Mood Statistics**
- Visual bar chart of your mood patterns
- Shows percentages and counts

**Option 5: Tell Me a Joke**
- Uses pyjokes to display random jokes

## What You're Learning

This project teaches you:

1. **Variables & Data Types** - Storing text, dates, and moods
2. **Functions** - Modular code with single responsibilities
3. **File I/O** - Reading and writing JSON files
4. **Libraries & Modules** - Using built-in (datetime, json, os) and external (pyjokes)
5. **Lists & Dictionaries** - Organizing and storing data
6. **Control Flow** - If/else statements and loops
7. **User Input/Output** - Interactive terminal application
8. **Error Handling** - Try/except blocks

## Data Storage

All entries are automatically saved in `journal_entries.json`:
```json
[
  {
    "date": "2026-05-22 15:30:45",
    "mood": "Happy",
    "content": "Had a great day today!"
  },
  {
    "date": "2026-05-22 18:20:10",
    "mood": "Sad",
    "content": "Missing my friends..."
  }
]
```

## Explaining to Your Professor

**Key Points to Mention:**

1. **Purpose**: "This is a journaling app that helps track mood patterns and emotions over time"

2. **Features Used**: 
   - File handling with JSON (persistent storage)
   - Modular functions (each feature is separate)
   - Built-in modules (datetime, json, os)
   - External module (pyjokes for engagement)

3. **Core Concepts Demonstrated**:
   - Data structures (dictionaries & lists)
   - File I/O operations
   - String formatting and user interaction
   - Date/time handling
   - Statistical analysis (mood counting)

4. **Why This Project**: "Perfect for learning Python fundamentals while building something practical and useful"

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'pyjokes'`
```bash
pip install pyjokes
```

**Issue**: `FileNotFoundError`
- The app creates `journal_entries.json` automatically on first entry

**Issue**: Entries not saving
- Make sure the script has write permissions in its directory

## Future Enhancements (Optional)
- Export entries to PDF
- Email digest of weekly mood
- Graphical interface with tkinter
- Cloud backup with API

---

**Status**: ✅ Complete and Ready for Submission  
**Last Updated**: May 22, 2026
