"""
Kyle Honaker

Description: An N5 Japanese vocabulary tester in Tkinter (Python GUI)

"""

# ------------------------------------------------------------------------------------------------
# Tkinter section and global variables
# ------------------------------------------------------------------------------------------------

# Imports
import random
from tkinter import *
from tkinter import ttk
root = Tk()

# Window Setup and grid
frm = ttk.Frame(root, padding=10)
frm.grid()

# Label for vocab display.
vocab_label = ttk.Label(frm, text="", font=("Arial", 30))
vocab_label.grid(column=2, row=1)

# Label for english display (hidden)
english = ttk.Label(frm, text="", font=("Arial", 20))
english.grid(column=2, row=2)

# Read the vocab file
with open("n5_vocab.csv", "r", encoding="utf-8") as file:
    file_lines = file.readlines()

# Global right and wrong counters for score
right_answers = 0
wrong_answers = 0
counter = 0

# Empty list to hold the 20 random vocab
vocab_list = []

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

def initialization():
    """
    INITIALIZATION: Resets the scores and populates 20 new vocab. Tied to the 'Start Quiz' button

    """

    # Global variables
    global right_answers
    right_answers = 0
    global wrong_answers
    wrong_answers = 0
    global counter
    counter = 0

    # Clear the vocab_list []
    vocab_list.clear()

    # Grab 20 vocab randomly from the file. Uses random module to pick from 0 to the length
    # of the lines in the CSV file
    for vocab in range(20): # 20 total vocab
        vocab_list.append(file_lines[random.randint(0, len(file_lines) - 1)]) # Append all 20 random vocab to the list
    
    # Calls the next_vocab( ) function to display the first or next vocab
    next_vocab(vocab_list[0])

# --------------------------------------------------------------------------

def next_vocab(vocab):
    """
    NEXT VOCAB: Displays the next vocab in the list. Splits each vocab into parts.
    Parameters: vocab - This is the string from the vocab list in the file_lines
    """

    # Global variables
    global vocab_label
    global english

    # Split vocab into parts
    vocab_parts = vocab.strip().split(",") # Strip the word, then split it from the ","
    japanese_word = vocab_parts[0]         # Japense words
    romaji = vocab_parts[1]                # Romaji words

    # Creates a label for Tkinter to show the Japanese and Romaji
    vocab_label.config(text=f"Japanese: {japanese_word}\nRomaji: {romaji}")

# --------------------------------------------------------------------------

def display_english():

    """
    DISPLAY ENGLISH: Originally hidden, but when the button is pushed it will display
    the english version of the word.
    """
    # Global variables
    global english
    global vocab_list, counter

    # This is the vocab_list[] at the current file line within the CSV
    vocab = vocab_list[counter]

    vocab_parts = vocab.strip().split(",") # Strip the word, then split it from the ","
    english_meaning = vocab_parts[2]  # Assignes [2] item which is the English
    english.config(text=f"Meaning: {english_meaning}") # Shows the English meaning from the CSV file

# --------------------------------------------------------------------------

def hide_english():

    """
    HIDE_ENGLISH: This hides the english text when 'right answer' and 'wrong answer' buttons 
    are pressed.
    """
    global english
    # Set the English text to nothing
    english.config(text="")

# --------------------------------------------------------------------------
def right_answer():

    """
    RIGHT_ANSWER: This increases the counter of right answers. This also contains the logic 
    to check if the vocabulary is still within the 20 word limit. If it's at 20 words it will
    end the quiz and show right/wrong answers.
    """
    global vocab_label
    global counter
    counter += 1
    global right_answers
    right_answers += 1
    
    if counter < 20:
        next_vocab(vocab_list[counter])
    elif counter >= 20:
         vocab_label.config(text=f"Right answers: {right_answers}\nWrong answers: {wrong_answers}")
    hide_english()

# --------------------------------------------------------------------------
def wrong_answer():

    """
    WRONG_ANSWER: This increases the counter of wrong answers. This also contains the logic 
    to check if the vocabulary is still within the 20 word limit. If it's at 20 words it will
    end the quiz and show right/wrong answers.
    """
    global vocab_label
    global counter
    counter += 1
    global wrong_answers
    wrong_answers += 1
    if counter < 20:
        next_vocab(vocab_list[counter])
    elif counter >= 20:  
        vocab_label.config(text=f"Right answers: {right_answers}\nWrong answers: {wrong_answers}")
    hide_english()

# ------------------------------------------------------------------------------------------------
# Tkinter labels and buttons
# ------------------------------------------------------------------------------------------------

# Title label - "Japanese N5 Vocab Quiz"
ttk.Label(frm, text="Japanese N5 Vocab Quiz").grid(column=2, row=0)

# Buttons
# Start quiz button - Triggers initialization( ) function
ttk.Button(frm, text="Start Quiz", command=initialization).grid(column=0, row=5)
# Right answer button - Triggers right_answer( ) function
ttk.Button(frm, text = "Right", command=right_answer).grid(column=0, row=2)
# Wrong answer button - Triggers wrong_answer( ) function
ttk.Button(frm, text="Wrong", command=wrong_answer).grid(column=0, row=3)
# English button - Triggers display_english( ) fuction
ttk.Button(frm, text="English", command=display_english).grid(column=0, row=4)

# Event loop - Ensures the window remains active and repsonsive to user interactions.
root.mainloop()