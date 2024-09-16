import tkinter as tk
from tkinter import filedialog, messagebox
import os
import zipfile
from pylinac import CatPhan604

def create_analysis_tab(tab):
    # Variable to store the selected folder path
    folder_path = tk.StringVar()

    # Function to select a folder
    def select_folder():
        selected_folder = filedialog.askdirectory()
        folder_path.set(selected_folder)
        log_message(f"Selected folder: {selected_folder}")

    # Function to start analysis
    def start_analysis():
        folder = folder_path.get()
        if not folder:
            log_message("Please select a folder first!")
            return

        # Perform CBCT analysis
        log_message('Starting analysis...')

        try:
            log_message(f'loading images from {folder} ...')
            cbct = CatPhan604(folder)
            log_message('done')

            log_message(f'starting analysis...')
            cbct.analyze()
            log_message('done')

            #cbct.plot_analyzed_image()
            pdf_file = os.path.join(folder, 'report.pdf')
            log_message(f'saving pdf file, {pdf_file}...')
            #cbct.publish_pdf(pdf_file)
            log_message('done')

            #result = cbct.results_data()

            json_file = os.path.join(folder, 'result.json')
            log_message(f'saving result, {json_file}...')
            cbct.to_quaac(json_file, format='json', overwrite=True)
            
            log_message("CBCT analysis completed successfully.")
            # You can display or save the results as needed
        except Exception as e:
            log_message(f"Error during CBCT analysis: {str(e)}")

    # Function to display logs
    def log_message(message):
        log_text.insert(tk.END, message + "\n")
        log_text.see(tk.END)  # Auto-scroll to the end of the text widget

    # Button to select folder
    select_folder_button = tk.Button(tab, text="Select Folder", command=select_folder)
    select_folder_button.pack(pady=10)

    # Label to display the selected folder path
    folder_label = tk.Label(tab, textvariable=folder_path)
    folder_label.pack(pady=5)

    # Button to start analysis
    start_button = tk.Button(tab, text="Start Analysis", command=start_analysis)
    start_button.pack(pady=10)

    # Log display area (Text widget)
    log_label = tk.Label(tab, text="Logs:")
    log_label.pack(pady=5)

    log_text = tk.Text(tab, height=10, state="normal", wrap="word")
    log_text.pack(padx=10, pady=10, expand=True, fill="both")
