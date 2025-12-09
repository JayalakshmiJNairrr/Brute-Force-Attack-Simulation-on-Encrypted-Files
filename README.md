🔐 Brute-Force Attack Simulation on Encrypted Files

This Python application simulates a brute-force password attack on encrypted ZIP and PDF files using a wordlist. It automates password attempts via a user-friendly GUI and displays the cracked password if found in the list.

Features

Supports password cracking for ZIP and PDF files

Uses the RockYou wordlist for brute-force simulation

Animated cracking progress with a responsive multithreaded GUI

Built using Tkinter for lightweight interface performance

Prerequisites

Ensure you have Python installed on your system along with the required dependencies.

Required Libraries:

Install them using:

pip install pikepdf

Wordlist Requirement

Download rockyou.txt and place it at:

/home/lenovo/Downloads/rockyou.txt


(You may change this path by editing the WORDLIST_PATH variable in the script.)

How to Use
1. Selecting a File

Run the script: python brute_force_gui.py

Click Select ZIP File or Select PDF File to choose the encrypted file

2. Running the Brute-Force Attack

Click Start Attack to begin the password cracking process

If the password is found in the wordlist, it will be displayed on the screen

3. Exiting the Tool

Click Exit anytime to close the application

File Structure
/Brute-Force-Attack-Simulation-on-Encrypted-Files
│── brute_force_gui.py      # Main application script
│── README.md               # Project documentation
│── rockyou.txt (external)  # Required wordlist – must be downloaded separately

Notes

This tool is intended only for ethical and authorized cybersecurity learning.

Do not use it on systems or files you do not own or lack permission to test.

Cracking time depends on the size of the wordlist and system performance.

License

This project is open-source and available under the MIT License.
