import tkinter as tk
from tkhtmlview import HTMLLabel

def create_instructions_tab(tab):
    # Load HTML content from instructions.html
    with open("instructions.html", "r") as file:
        html_content = file.read()

    # Create an HTMLLabel widget to display the HTML content
    html_label = HTMLLabel(tab, html=html_content)
    html_label.pack(padx=10, pady=10, expand=True, fill="both")
