import zipfile
import pikepdf # type: ignore
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import time

# Default path to RockYou wordlist
WORDLIST_PATH = "/home/lenovo/Downloads/rockyou.txt"

def animate_cracking():
    """Simulates a cracking animation."""
    animation = ["Cracking.", "Cracking..", "Cracking...", "Cracking...."]
    i = 0
    while cracking_animation["running"]:
        progress_label.config(text=animation[i % len(animation)])
        i += 1
        time.sleep(0.5)

def crack_zip(zip_file_path):
    print("Starting brute force attack on the ZIP file...")
    cracking_animation["running"] = True
    threading.Thread(target=animate_cracking).start()

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            with open(WORDLIST_PATH, 'r', encoding='utf-8', errors='ignore') as wordlist:
                for i, line in enumerate(wordlist):
                    password = line.strip().encode('utf-8')
                    print(f"Trying ZIP password: {password.decode('utf-8')}")
                    
                    try:
                        zf.extractall(pwd=password)
                        cracking_animation["running"] = False
                        progress_label.config(text="Cracked!")
                        password_label.config(text=f"Cracked Password: {password.decode('utf-8')}", fg="lime")
                        messagebox.showinfo("Success", f"ZIP Password found: {password.decode('utf-8')}")
                        print(f"Password found: {password.decode('utf-8')}")
                        return
                    except (RuntimeError, zipfile.BadZipFile):
                        pass
        cracking_animation["running"] = False
        progress_label.config(text="Failed to crack")
        messagebox.showerror("Failed", "Password not found in the wordlist.")
    except FileNotFoundError:
        cracking_animation["running"] = False
        messagebox.showerror("Error", "ZIP file or wordlist not found.")
    except zipfile.BadZipFile:
        cracking_animation["running"] = False
        messagebox.showerror("Error", "The ZIP file is invalid or corrupted.")
    except Exception as e:
        cracking_animation["running"] = False
        messagebox.showerror("Error", f"Unexpected error: {e}")

def crack_pdf(pdf_file_path):
    print("Starting brute force attack on the PDF file...")
    cracking_animation["running"] = True
    threading.Thread(target=animate_cracking).start()

    try:
        with open(WORDLIST_PATH, 'r', encoding='utf-8', errors='ignore') as wordlist:
            for i, line in enumerate(wordlist):
                password = line.strip()
                print(f"Trying PDF password: {password}")
                
                try:
                    with pikepdf.open(pdf_file_path, password=password):
                        cracking_animation["running"] = False
                        progress_label.config(text="Cracked!")
                        password_label.config(text=f"Cracked Password: {password}", fg="lime")
                        messagebox.showinfo("Success", f"PDF Password found: {password}")
                        print(f"Password found: {password}")
                        return
                except pikepdf.PasswordError:
                    pass
        cracking_animation["running"] = False
        progress_label.config(text="Failed to crack")
        messagebox.showerror("Failed", "Password not found in the wordlist.")
    except FileNotFoundError:
        cracking_animation["running"] = False
        messagebox.showerror("Error", "PDF file or wordlist not found.")
    except Exception as e:
        cracking_animation["running"] = False
        messagebox.showerror("Error", f"Unexpected error: {e}")

def select_zip():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if selected_file:
        file_label.config(text=f"Selected: {selected_file}", font=("Courier", 12, "bold"))

def select_pdf():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if selected_file:
        file_label.config(text=f"Selected: {selected_file}", font=("Courier", 12, "bold"))

def start_attack():
    if selected_file.endswith(".zip"):
        threading.Thread(target=crack_zip, args=(selected_file,)).start()
    elif selected_file.endswith(".pdf"):
        threading.Thread(target=crack_pdf, args=(selected_file,)).start()
    else:
        messagebox.showerror("Error", "No valid file selected.")

# GUI Setup
root = tk.Tk()
root.title("Brute Force Password Cracker")
root.geometry("600x400")
root.configure(bg="black")

# Shared animation control
cracking_animation = {"running": False}

# Title Label
title_label = tk.Label(root, text="Password Cracker Tool", font=("Courier", 18, "bold"), fg="lime", bg="black")
title_label.pack(pady=15)

# File Selection Buttons
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=10)

zip_button = tk.Button(btn_frame, text="Select ZIP File", command=select_zip, bg="black", fg="lime", font=("Courier", 14, "bold"), relief=tk.GROOVE)
zip_button.grid(row=0, column=0, padx=10)

pdf_button = tk.Button(btn_frame, text="Select PDF File", command=select_pdf, bg="black", fg="lime", font=("Courier", 14, "bold"), relief=tk.GROOVE)
pdf_button.grid(row=0, column=1, padx=10)

# Selected File Label
file_label = tk.Label(root, text="No file selected", font=("Courier", 12, "bold"), fg="lime", bg="black")
file_label.pack(pady=5)

# Progress Label
progress_label = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="yellow", bg="black")
progress_label.pack(pady=5)

# Start Attack Button
start_button = tk.Button(root, text="Start Attack", command=start_attack, bg="black", fg="lime", font=("Courier", 14, "bold"), relief=tk.RIDGE)
start_button.pack(pady=10)

# Cracked Password Label
password_label = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="lime", bg="black")
password_label.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, bg="black", fg="red", font=("Courier", 14, "bold"), relief=tk.GROOVE)
exit_button.pack(pady=10)

root.mainloop()
