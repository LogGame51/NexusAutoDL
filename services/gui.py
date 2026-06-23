import os
import tkinter as tk
from typing import TYPE_CHECKING
from utils.logger import RECENT_LOGS
from utils.i18n import _

if TYPE_CHECKING:
    from services.scanner import Scanner

class OverlayGUI:
    """Tkinter Overlay GUI for NexusAutoDL."""

    def __init__(self, scanner: 'Scanner'):
        self.scanner = scanner
        
        self.root = tk.Tk()
        self.root.title("NexusAutoDL")
        self.root.overrideredirect(True)  # No window borders/title bar
        self.root.attributes("-topmost", True)  # Always on top
        self.root.attributes("-alpha", 0.85)  # Liquid glass look
        
        # Dark theme
        bg_color = "#1E1E1E"
        fg_color = "#00FF00"
        text_color = "#FFFFFF"
        
        self.root.configure(bg=bg_color, padx=10, pady=10)
        
        # Position in top right corner of the primary monitor
        # We'll just put it at x = screen_width - 350, y = 20
        screen_width = self.root.winfo_screenwidth()
        window_width = 320
        window_height = 180
        x = screen_width - window_width - 20
        y = 20
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Header: Bot Status
        self.header_label = tk.Label(
            self.root, 
            text=_("bot_working"), 
            font=("Consolas", 12, "bold"), 
            bg=bg_color, 
            fg=fg_color
        )
        self.header_label.pack(anchor="w")
        
        # Current Action / Timer
        self.action_label = tk.Label(
            self.root, 
            text=_("init"), 
            font=("Consolas", 10), 
            bg=bg_color, 
            fg="#FFA500"  # Orange
        )
        self.action_label.pack(anchor="w", pady=(5, 5))
        
        # Logs (last 3 lines)
        self.logs_var = tk.StringVar(value="")
        self.logs_label = tk.Label(
            self.root, 
            textvariable=self.logs_var, 
            font=("Consolas", 8), 
            bg=bg_color, 
            fg=text_color,
            justify="left",
            wraplength=300
        )
        self.logs_label.pack(anchor="w", fill="x")
        
        # Stop Button
        self.stop_btn = tk.Button(
            self.root, 
            text=_("stop"), 
            command=self.kill_bot,
            bg="#FF0000",
            fg="#FFFFFF",
            font=("Consolas", 10, "bold"),
            relief="flat",
            activebackground="#CC0000",
            activeforeground="#FFFFFF"
        )
        self.stop_btn.pack(fill="x", pady=(10, 0))
        
        # Start the update loop
        self.update_ui()

    def kill_bot(self):
        """Instantly kills the python process."""
        print(_("stopped_by_user"))
        os._exit(0)
        
    def update_ui(self):
        """Poll the scanner status and update UI."""
        status = self.scanner.status
        
        # Update action and timer
        self.action_label.config(text=_("target", status.current_action))
        
        # Update logs
        logs_text = "\n".join(RECENT_LOGS)
        self.logs_var.set(logs_text)
        
        # Schedule next update
        self.root.after(200, self.update_ui)
        
    def run(self):
        """Start the Tkinter main loop."""
        self.root.mainloop()
