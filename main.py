'''
Integrity Checker Application
This is the main file of the Integrity Checker application. It provides the user interface and handles user interactions.
'''
import tkinter as tk
from integrity_checker import IntegrityChecker
class IntegrityCheckerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Integrity Checker")
        self.integrity_checker = IntegrityChecker()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create the user interface elements.
        '''
        self.label = tk.Label(self.root, text="Welcome to Integrity Checker!")
        self.label.pack()
        self.scan_button = tk.Button(self.root, text="Scan", command=self.scan_files)
        self.scan_button.pack()
        self.alert_text = tk.Text(self.root, height=10, width=50)
        self.alert_text.pack()
    def scan_files(self):
        '''
        Scan the system files and display any discrepancies found.
        '''
        alerts = self.integrity_checker.scan_files()
        self.alert_text.delete(1.0, tk.END)
        self.alert_text.insert(tk.END, alerts)
    def run(self):
        '''
        Run the application.
        '''
        self.root.mainloop()
if __name__ == "__main__":
    app = IntegrityCheckerApp()
    app.run()