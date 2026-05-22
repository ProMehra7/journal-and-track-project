"""
Personal Journal & Mood Tracker Application
BCA Major Project - Last Semester
Author: Your Name
Description: A simple command-line application to track daily journal entries and moods
"""

import json
import os
from datetime import datetime
import pyjokes

# File to store journal entries
JOURNAL_FILE = "journal_entries.json"

# Color codes for nice terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def load_entries():
    """
    Load all journal entries from the JSON file
    Returns: List of entries or empty list if file doesn't exist
    """
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, 'r') as file:
            return json.load(file)
    return []


def save_entries(entries):
    """
    Save journal entries to JSON file
    Params: entries - List of journal entries
    """
    with open(JOURNAL_FILE, 'w') as file:
        json.dump(entries, file, indent=2)
    print(f"{Colors.GREEN}✓ Entry saved successfully!{Colors.END}")


def add_entry():
    """
    Add a new journal entry with mood tracking
    """
    print(f"\n{Colors.CYAN}--- Add New Journal Entry ---{Colors.END}")
    
    # Get entry text from user
    entry_text = input(f"{Colors.BLUE}What's on your mind? (Type your entry):{Colors.END}\n> ")
    
    if not entry_text.strip():
        print(f"{Colors.RED}✗ Entry cannot be empty!{Colors.END}")
        return
    
    # Get mood from user
    print(f"\n{Colors.BLUE}How are you feeling?{Colors.END}")
    moods = ["😊 Happy", "😢 Sad", "😐 Neutral", "😠 Angry"]
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood}")
    
    try:
        mood_choice = int(input(f"{Colors.BLUE}Select mood (1-4):{Colors.END} "))
        mood_map = {1: "Happy", 2: "Sad", 3: "Neutral", 4: "Angry"}
        
        if mood_choice not in mood_map:
            print(f"{Colors.RED}✗ Invalid choice!{Colors.END}")
            return
        
        mood = mood_map[mood_choice]
    except ValueError:
        print(f"{Colors.RED}✗ Please enter a number!{Colors.END}")
        return
    
    # Create entry dictionary
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "content": entry_text
    }
    
    # Load, add, and save
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)


def view_all_entries():
    """
    Display all journal entries
    """
    print(f"\n{Colors.CYAN}--- All Journal Entries ---{Colors.END}")
    
    entries = load_entries()
    
    if not entries:
        print(f"{Colors.YELLOW}No entries yet. Start writing!{Colors.END}")
        return
    
    for i, entry in enumerate(entries, 1):
        print(f"\n{Colors.BOLD}{Colors.HEADER}Entry #{i}{Colors.END}")
        print(f"{Colors.BLUE}Date:{Colors.END} {entry['date']}")
        print(f"{Colors.BLUE}Mood:{Colors.END} {entry['mood']}")
        print(f"{Colors.BLUE}Content:{Colors.END}\n{entry['content']}")
        print("-" * 50)


def search_by_date():
    """
    Search entries by specific date
    """
    print(f"\n{Colors.CYAN}--- Search by Date ---{Colors.END}")
    
    search_date = input(f"{Colors.BLUE}Enter date (YYYY-MM-DD):{Colors.END} ")
    
    entries = load_entries()
    found_entries = [e for e in entries if e['date'].startswith(search_date)]
    
    if not found_entries:
        print(f"{Colors.YELLOW}No entries found for {search_date}{Colors.END}")
        return
    
    print(f"\n{Colors.GREEN}Found {len(found_entries)} entry/entries:{Colors.END}")
    for entry in found_entries:
        print(f"\n{Colors.BLUE}Date:{Colors.END} {entry['date']}")
        print(f"{Colors.BLUE}Mood:{Colors.END} {entry['mood']}")
        print(f"{Colors.BLUE}Content:{Colors.END}\n{entry['content']}")
        print("-" * 50)


def view_mood_stats():
    """
    Display mood statistics
    """
    print(f"\n{Colors.CYAN}--- Mood Statistics ---{Colors.END}")
    
    entries = load_entries()
    
    if not entries:
        print(f"{Colors.YELLOW}No entries yet!{Colors.END}")
        return
    
    # Count moods
    mood_count = {"Happy": 0, "Sad": 0, "Neutral": 0, "Angry": 0}
    for entry in entries:
        mood_count[entry['mood']] += 1
    
    total = len(entries)
    print(f"\n{Colors.BLUE}Total entries: {total}{Colors.END}\n")
    
    mood_emojis = {"Happy": "😊", "Sad": "😢", "Neutral": "😐", "Angry": "😠"}
    
    for mood, count in mood_count.items():
        percentage = (count / total) * 100
        bar = "█" * int(percentage / 5)
        print(f"{mood_emojis[mood]} {mood:10} | {bar:20} | {count:3} ({percentage:5.1f}%)")


def tell_joke():
    """
    Tell a random joke to brighten the mood
    """
    print(f"\n{Colors.CYAN}--- Random Joke ---{Colors.END}")
    joke = pyjokes.get_joke()
    print(f"{Colors.YELLOW}{joke}{Colors.END}")


def display_menu():
    """
    Display main menu
    """
    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("╔════════════════════════════════════════╗")
    print("║   📔 Personal Journal & Mood Tracker   ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.END}")
    
    print(f"{Colors.CYAN}Main Menu:{Colors.END}")
    print("1. ✍️  Add New Entry")
    print("2. 📖 View All Entries")
    print("3. 🔍 Search by Date")
    print("4. 📊 View Mood Statistics")
    print("5. 😂 Tell Me a Joke")
    print("6. ❌ Exit")
    print()


def main():
    """
    Main function - Program entry point
    """
    while True:
        display_menu()
        
        choice = input(f"{Colors.BLUE}Enter your choice (1-6):{Colors.END} ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            view_mood_stats()
        elif choice == "5":
            tell_joke()
        elif choice == "6":
            print(f"\n{Colors.GREEN}Thank you for using Journal Tracker! Goodbye! 👋{Colors.END}\n")
            break
        else:
            print(f"{Colors.RED}✗ Invalid choice! Please select 1-6.{Colors.END}")


if __name__ == "__main__":
    main()
