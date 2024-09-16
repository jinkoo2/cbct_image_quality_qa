import tkinter as tk
from tkinter import ttk
from instructions import create_instructions_tab
from analysis import create_analysis_tab
from results import create_results_tab

# Create the main window
root = tk.Tk()
root.title("Tabbed App with Separated Files")
root.geometry("640x480")

# Create a notebook widget (this will hold the tabs)
notebook = ttk.Notebook(root)

# Add the tabs by importing from other files
tab1 = ttk.Frame(notebook)
create_instructions_tab(tab1)
notebook.add(tab1, text="Instruction")

tab2 = ttk.Frame(notebook)
create_analysis_tab(tab2)
notebook.add(tab2, text="Analysis")

tab3 = ttk.Frame(notebook)
create_results_tab(tab3)
notebook.add(tab3, text="Results")

notebook.pack(expand=True, fill="both")

# Run the application
root.mainloop()

