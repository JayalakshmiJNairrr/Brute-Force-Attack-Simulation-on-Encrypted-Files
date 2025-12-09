# Brute-Force Attack Simulation on Encrypted Files

This Python application simulates a brute-force password attack on encrypted ZIP and PDF files using a wordlist. It automates password attempts through a user-friendly GUI and displays the cracked password if found.

## Features
- Cracks ZIP and PDF files using a brute-force dictionary attack
- Uses the RockYou wordlist for password attempts
- Animated cracking progress with a responsive multithreaded GUI
- Lightweight interface built with Tkinter

## Prerequisites
Ensure Python is installed along with the required library.

### Required Library:
```sh
pip install pikepdf
```

##  Wordlist Requirement
Download **rockyou.txt** and place it at:
```
/home/Downloads/rockyou.txt
```
(You can update this path in the script by modifying the `WORDLIST_PATH` variable.)

## How to Use

### 1. Selecting a File
- Run the script: `python brute_force_gui.py`
- Click **Select ZIP File** or **Select PDF File** to choose an encrypted file

### 2. Starting the Attack
- Click **Start Attack** to begin the brute-force simulation
- If the password exists in the wordlist, it will be displayed on the screen

### 3. Exiting the Tool
- Click **Exit** to close the application at any time

## File Structure
```
/Brute-Force-Attack-Simulation-on-Encrypted-Files
│── brute_force_gui.py      # Main application script
│── README.md               # Project documentation
│── rockyou.txt (external)  # Required wordlist – must be downloaded separately
```

## Notes
- This tool is intended **only for ethical cybersecurity learning and research**
- Never use it on files or systems without proper authorization
- Cracking time depends on the hardware and the size of the wordlist

## License
This project is open‑source and available under the **MIT License**.
