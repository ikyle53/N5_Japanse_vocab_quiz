"""
Kyle Honaker

Description: An N5 Japanese vocabulary tester in Tkinter (Python GUI)

"""

# ------------------------------------------------------------------------------------------------
# Tkinter section and global variables
# ------------------------------------------------------------------------------------------------

# Imports ------------------------------------------------
from tkinter import *
from tkinter import ttk
import functions as f

# Window Setup and grid ----------------------------------
root = Tk()
root.title("Japanese N5 Vocab Quiz")

# Sets the size of the window on initial startup
root.geometry("1024x768")

# This makes the widgets 'responsive' and resizes with the window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Sets the background image
bg = PhotoImage(file="okinawa.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------------------------------------------------------------------------------------
# TKinter Styling
# ------------------------------------------------------------------------------------------------
style = ttk.Style() # Making a custom style

# Background color for the quiz window
style.configure("Transparent.TFrame", background="#515177")

# Label background/text color
style.configure("TLabel", background="#515177", foreground="white")

# Button background/text color
style.configure("TButton", background="#515177", foreground="white")

# Give a hover effect when mousing over the buttons
style.map("TButton", 
          background=[("active", "#0011ff")],
          foreground=[("active", "#000000"), ("!active", "#000000")])

# Set the frame as a variable so I can place labels/buttons in it with the configured style
frm = ttk.Frame(root, style="Transparent.TFrame", padding=30)
frm.place(relx=0.5, rely=0.5, anchor="center")

# After frame and window is set this lowers the bg image below all content
label1.lower(frm)

# Access to functions.py variables
f.frm = frm
f.root = root
f.start_quiz  = None
f.right_answers_list = None
f.wrong_answers_list = None
f.vocab_label = None
f.english = None
f.right_button = None
f.wrong_button = None
f.displayEng = None

# ------------------------------------------------------------------------------------------------
# Tkinter labels / buttons (Widgets)
# ------------------------------------------------------------------------------------------------

# Labels --------------------------------------------------

# Title label - "Japanese N5 Vocab Quiz"
ttk.Label(frm, text="Japanese N5 Vocab Quiz", font=("Arial", 20)).grid(
    column=0, 
    row=0, 
    columnspan=5, 
    rowspan=1, 
    sticky=N,
    pady=50)

# Label for vocab display.
vocab_label = ttk.Label(frm, text="", font=("Arial", 15))
vocab_label.grid(
    column=0, 
    row=1, 
    columnspan=5, 
    rowspan=1,
    pady=20)
f.vocab_label = vocab_label

# Label for english display (hidden)
english = ttk.Label(frm, text="", font=("Arial", 15))
english.grid(
    column=1, 
    row=2,
    columnspan=2)
f.english = english

# Label for right answers
right_answers_list = ttk.Label(frm, text="", font=("Ariel", 10))
right_answers_list.grid(
    column=1, 
    row=4, 
    padx=50, 
    pady=0)
f.right_answers_list = right_answers_list

# Label for wrong answers
wrong_answers_list = ttk.Label(frm, text="", font=("Ariel", 10))
wrong_answers_list.grid(
    column=3, 
    row=4, 
    padx=50, 
    pady=0)
f.wrong_answers_list = wrong_answers_list

# Buttons --------------------------------------------------

# Start quiz button - Triggers initialization( ) function
start_quiz = ttk.Button(frm, text="Start Quiz", command=f.initialization)
start_quiz.grid(
    column=2, 
    row=5)
f.start_quiz = start_quiz

# Event loop - Ensures the window remains active and repsonsive to user interactions.
root.mainloop()