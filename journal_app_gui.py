"""
Personal Journal & Mood Tracker Application - GUI Version
BCA Major Project - Last Semester
Author: Your Name
Description: A GUI-based journaling application with mood tracking
"""

import json
import os
from datetime import datetime
import pyjokes
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from tkinter import ttk
import tkinter.font as tkFont

# File to store journal entries
JOURNAL_FILE = "journal_entries.json"

class JournalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📔 Personal Journal & Mood Tracker")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Set icon (optional)
        try:
            self.root.iconbitmap(default='')
        except:
            pass
        
        # Define colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.button_hover = "#45a049"
        self.text_color = "#333333"
        
        # Create main frame
        self.create_main_menu()
    
    def create_main_menu(self):
        """Create the main menu screen"""
        self.clear_window()
        
        # Title
        title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(
            self.root,
            text="📔 Journal & Mood Tracker",
            font=title_font,
            bg=self.bg_color,
            fg="#2196F3"
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_font = tkFont.Font(family="Helvetica", size=12)
        subtitle = tk.Label(
            self.root,
            text="Track your thoughts and emotions",
            font=subtitle_font,
            bg=self.bg_color,
            fg="#666666"
        )
        subtitle.pack(pady=5)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=30, expand=True)
        
        # Buttons
        buttons = [
            ("✍️  Add New Entry", self.create_add_entry_screen),
            ("📖 View All Entries", self.view_all_entries),
            ("🔍 Search by Date", self.create_search_screen),
            ("📊 View Mood Statistics", self.view_mood_stats),
            ("😂 Tell Me a Joke", self.tell_joke),
            ("❌ Exit", self.root.quit)
        ]
        
        for text, command in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Helvetica", 12),
                width=25,
                bg=self.button_color,
                fg="white",
                activebackground=self.button_hover,
                command=command,
                relief=tk.RAISED,
                bd=2
            )
            btn.pack(pady=10)
    
    def create_add_entry_screen(self):
        """Create screen to add new entry"""
        self.clear_window()
        
        # Back button at top
        self.create_back_button()
        
        # Title
        title = tk.Label(
            self.root,
            text="✍️  Add New Journal Entry",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg="#2196F3"
        )
        title.pack(pady=10)
        
        # Entry text label
        tk.Label(
            self.root,
            text="What's on your mind?",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).pack(anchor="w", padx=20, pady=(10, 5))
        
        # Text area
        self.text_entry = scrolledtext.ScrolledText(
            self.root,
            height=10,
            width=70,
            font=("Helvetica", 11),
            wrap=tk.WORD
        )
        self.text_entry.pack(padx=20, pady=10)
        
        # Mood selection
        tk.Label(
            self.root,
            text="How are you feeling?",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).pack(anchor="w", padx=20, pady=(10, 5))
        
        mood_frame = tk.Frame(self.root, bg=self.bg_color)
        mood_frame.pack(padx=20, pady=10)
        
        self.mood_var = tk.StringVar(value="Happy")
        moods = [("😊 Happy", "Happy"), ("😢 Sad", "Sad"), ("😐 Neutral", "Neutral"), ("😠 Angry", "Angry")]
        
        for text, value in moods:
            rb = tk.Radiobutton(
                mood_frame,
                text=text,
                variable=self.mood_var,
                value=value,
                font=("Helvetica", 11),
                bg=self.bg_color
            )
            rb.pack(side=tk.LEFT, padx=10)
        
        # Save button
        save_btn = tk.Button(
            self.root,
            text="💾 Save Entry",
            font=("Helvetica", 12),
            bg="#4CAF50",
            fg="white",
            command=self.save_entry,
            width=20
        )
        save_btn.pack(pady=20)
    
    def save_entry(self):
        """Save the journal entry"""
        content = self.text_entry.get("1.0", tk.END).strip()
        
        if not content:
            messagebox.showerror("Error", "Entry cannot be empty!")
            return
        
        mood = self.mood_var.get()
        
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mood": mood,
            "content": content
        }
        
        entries = self.load_entries()
        entries.append(entry)
        self.save_entries(entries)
        
        messagebox.showinfo("Success", "✓ Entry saved successfully!")
        self.create_main_menu()
    
    def view_all_entries(self):
        """Display all entries"""
        self.clear_window()
        self.create_back_button()
        
        entries = self.load_entries()
        
        if not entries:
            tk.Label(
                self.root,
                text="No entries yet. Start writing!",
                font=("Helvetica", 14),
                bg=self.bg_color
            ).pack(pady=50)
            return
        
        # Create frame with scrollbar
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        canvas = tk.Canvas(frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.bg_color)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display entries
        for i, entry in enumerate(entries, 1):
            entry_frame = tk.Frame(scrollable_frame, bg="white", relief=tk.RAISED, bd=1)
            entry_frame.pack(fill=tk.X, pady=10, padx=10)
            
            tk.Label(
                entry_frame,
                text=f"Entry #{i} - {entry['date']} - Mood: {entry['mood']}",
                font=("Helvetica", 10, "bold"),
                bg="white",
                fg="#2196F3"
            ).pack(anchor="w", padx=10, pady=5)
            
            tk.Label(
                entry_frame,
                text=entry['content'][:200] + "..." if len(entry['content']) > 200 else entry['content'],
                font=("Helvetica", 10),
                bg="white",
                fg="#333333",
                wraplength=700,
                justify=tk.LEFT
            ).pack(anchor="w", padx=10, pady=(0, 5))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_search_screen(self):
        """Create search screen"""
        self.clear_window()
        self.create_back_button()
        
        tk.Label(
            self.root,
            text="🔍 Search Entries by Date",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg="#2196F3"
        ).pack(pady=20)
        
        tk.Label(
            self.root,
            text="Enter date (YYYY-MM-DD):",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).pack()
        
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 12), width=30)
        self.search_entry.pack(pady=10)
        
        search_btn = tk.Button(
            self.root,
            text="🔍 Search",
            font=("Helvetica", 12),
            bg="#2196F3",
            fg="white",
            command=self.perform_search,
            width=20
        )
        search_btn.pack(pady=20)
        
        self.search_result_frame = tk.Frame(self.root, bg=self.bg_color)
        self.search_result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    def perform_search(self):
        """Perform the search"""
        search_date = self.search_entry.get().strip()
        
        if not search_date:
            messagebox.showerror("Error", "Please enter a date!")
            return
        
        entries = self.load_entries()
        found_entries = [e for e in entries if e['date'].startswith(search_date)]
        
        # Clear previous results
        for widget in self.search_result_frame.winfo_children():
            widget.destroy()
        
        if not found_entries:
            tk.Label(
                self.search_result_frame,
                text=f"No entries found for {search_date}",
                font=("Helvetica", 12),
                bg=self.bg_color,
                fg="#FF9800"
            ).pack()
            return
        
        tk.Label(
            self.search_result_frame,
            text=f"Found {len(found_entries)} entry/entries:",
            font=("Helvetica", 12, "bold"),
            bg=self.bg_color
        ).pack()
        
        for entry in found_entries:
            entry_frame = tk.Frame(self.search_result_frame, bg="white", relief=tk.RAISED, bd=1)
            entry_frame.pack(fill=tk.X, pady=10)
            
            tk.Label(
                entry_frame,
                text=f"{entry['date']} - {entry['mood']}",
                font=("Helvetica", 10, "bold"),
                bg="white",
                fg="#2196F3"
            ).pack(anchor="w", padx=10, pady=5)
            
            tk.Label(
                entry_frame,
                text=entry['content'],
                font=("Helvetica", 10),
                bg="white",
                wraplength=700,
                justify=tk.LEFT
            ).pack(anchor="w", padx=10, pady=(0, 5))
    
    def view_mood_stats(self):
        """Display mood statistics"""
        self.clear_window()
        self.create_back_button()
        
        entries = self.load_entries()
        
        if not entries:
            tk.Label(
                self.root,
                text="No entries yet!",
                font=("Helvetica", 14),
                bg=self.bg_color
            ).pack(pady=50)
            return
        
        # Count moods
        mood_count = {"Happy": 0, "Sad": 0, "Neutral": 0, "Angry": 0}
        for entry in entries:
            mood_count[entry['mood']] += 1
        
        total = len(entries)
        
        tk.Label(
            self.root,
            text="📊 Mood Statistics",
            font=("Helvetica", 18, "bold"),
            bg=self.bg_color,
            fg="#2196F3"
        ).pack(pady=20)
        
        tk.Label(
            self.root,
            text=f"Total entries: {total}",
            font=("Helvetica", 12),
            bg=self.bg_color
        ).pack()
        
        # Display mood stats
        stats_frame = tk.Frame(self.root, bg=self.bg_color)
        stats_frame.pack(pady=30, expand=True)
        
        mood_emojis = {"Happy": "😊", "Sad": "😢", "Neutral": "😐", "Angry": "😠"}
        colors = {"Happy": "#4CAF50", "Sad": "#2196F3", "Neutral": "#FF9800", "Angry": "#F44336"}
        
        for mood in ["Happy", "Sad", "Neutral", "Angry"]:
            count = mood_count[mood]
            percentage = (count / total) * 100
            
            row_frame = tk.Frame(stats_frame, bg=self.bg_color)
            row_frame.pack(fill=tk.X, pady=10, padx=50)
            
            tk.Label(
                row_frame,
                text=f"{mood_emojis[mood]} {mood}",
                font=("Helvetica", 12, "bold"),
                bg=self.bg_color,
                width=15,
                anchor="w"
            ).pack(side=tk.LEFT, padx=10)
            
            # Progress bar
            bar_length = int(percentage / 5)
            bar = "█" * bar_length
            tk.Label(
                row_frame,
                text=bar,
                font=("Courier", 12),
                bg=self.bg_color,
                fg=colors[mood],
                width=20,
                anchor="w"
            ).pack(side=tk.LEFT, padx=10)
            
            tk.Label(
                row_frame,
                text=f"{count} ({percentage:.1f}%)",
                font=("Helvetica", 12),
                bg=self.bg_color,
                width=15,
                anchor="w"
            ).pack(side=tk.LEFT, padx=10)
    
    def tell_joke(self):
        """Tell a random joke"""
        joke = pyjokes.get_joke()
        messagebox.showinfo("😂 Random Joke", joke)
    
    def create_back_button(self):
        """Create back button"""
        back_btn = tk.Button(
            self.root,
            text="← Back to Menu",
            font=("Helvetica", 10),
            bg="#757575",
            fg="white",
            command=self.create_main_menu,
            width=15
        )
        back_btn.pack(anchor="ne", padx=10, pady=10)
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def load_entries(self):
        """Load entries from JSON file"""
        if os.path.exists(JOURNAL_FILE):
            with open(JOURNAL_FILE, 'r') as file:
                return json.load(file)
        return []
    
    def save_entries(self, entries):
        """Save entries to JSON file"""
        with open(JOURNAL_FILE, 'w') as file:
            json.dump(entries, file, indent=2)


def main():
    """Main function"""
    root = tk.Tk()
    app = JournalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
