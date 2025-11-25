"""
Kyle Honaker

Description: An N5 Japanese vocabulary tester in Tkinter (Python GUI)

"""

# ------------------------------------------------------------------------------------------------
# Tkinter section and global variables
# ------------------------------------------------------------------------------------------------

# Imports ------------------------------------------------
import pandas as pd
from tkinter import *
from tkinter import ttk

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

# Styling -----------------------------------------------
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

# Load the CSV file with Pandass
df = pd.read_csv("n5_vocab.csv")

# Global Tracking -----------------------------------------
# Right and wrong counters for score
right_answers = 0
wrong_answers = 0
counter = 0

# Empty list to hold the 20 random vocab
vocab_list = pd.DataFrame()

# Empty list to hold right/wrong words to show at the end
right_list = []
wrong_list = []

# Right and Wrong buttons - Need to be declared as variables so they can be hidden/displayed
right_button = None
wrong_button = None
displayEng = None

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

def initialization():
    """
    INITIALIZATION: Resets the scores, interface, and populates 20 new vocab. Tied to the 'Start Quiz' button

    """

    # Global variables
    global right_answers, wrong_answers, counter, vocab_list, right_button, wrong_button, displayEng
    right_answers = 0
    wrong_answers = 0
    counter = 0

    # Clear the vocab_list, righ_list, and wrong_list
    right_list.clear()
    wrong_list.clear()

    # Reset the list of right/wrong text to empty text.
    right_answers_list.config(text="")
    wrong_answers_list.config(text="")

    # Pandas picks 20 random rows using the 'sample' method. 'replace' would change
    # the word values and create issues. It's set to False.
    vocab_list = df.sample(n=20, replace=False).reset_index(drop = True)
    # reset_index(drop = True) will drop the list item if its an empty line
    

    # Right answer button - Triggers right_answer( ) function
    right_button = ttk.Button(frm, text = "Right", command=right_answer)
    right_button.grid(
    column=1, 
    row=6,
    padx=10)
    
    # Wrong answer button - Triggers wrong_answer( ) function
    wrong_button = ttk.Button(frm, text="Wrong", command=wrong_answer)
    wrong_button.grid(
    column=2, 
    row=6,
    padx=10)

    # English button - Triggers display_english( ) fuction
    displayEng = ttk.Button(frm, text="English", command=display_english)
    displayEng.grid(
    column=0, 
    row=2)

    start_quiz.grid_forget()

    # Calls the next_vocab( ) function to display the first or next vocab
    next_vocab(0)

# --------------------------------------------------------------------------

def next_vocab(vocab):
    """
    NEXT VOCAB: Displays the next vocab in the list. Splits each vocab into parts.
    Parameters: vocab: strings from the csv file
    """

    # Global variables
    global vocab_label

    # Split vocab into parts
    # "iloc" = integer location. Pandas uses a number to find the position of
    # the index
    japanese_word = vocab_list.iloc[vocab]["Japanese"] # Japense words
    romaji = vocab_list.iloc[vocab]["Romaji"]          # Romaji words

    # Creates a label for Tkinter to show the Japanese and Romaji
    vocab_label.config(text=f"Japanese:   {japanese_word}\nRomaji:   {romaji}")

# --------------------------------------------------------------------------

def display_english():

    """
    DISPLAY ENGLISH: Originally hidden, but when the button is pushed it will display
    the english version of the word.
    """
    # Global variables
    global english, vocab_list, counter

    # "iloc" = integer location. Pandas uses a number to find the position of
    # the index
    english_meaning = vocab_list.iloc[counter]["English"]
    english.config(text=f"Meaning:   {english_meaning}") # Shows the English meaning from the CSV file

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
    RIGHT_ANSWER: This increases the counter of right answers and continues the quiz. 
    Contains the if statement to continue or end the quiz. If it's at 20 words it will
    end the quiz and show 
    right/wrong answers.
    """
    global counter, right_list, right_answers
    right_answers += 1
    
    right_list.append(vocab_list.iloc[counter])

    if counter < 19:
        counter += 1
        next_vocab(counter)
    else:
         end_of_quiz()
    hide_english()

# --------------------------------------------------------------------------
def wrong_answer():

    """
    WRONG_ANSWER: This increases the counter of wrong answers and continues the quiz. 
    Contains the if statement to continue or end the quiz. If it's at 20 words it will 
    end the quiz and show right/wrong answers.
    """
    global counter, wrong_list, wrong_answers
    wrong_answers += 1

    wrong_list.append(vocab_list.iloc[counter])

    if counter < 19:
        counter += 1
        next_vocab(counter)
    else:  
        end_of_quiz()
    hide_english()

# --------------------------------------------------------------------------
def end_of_quiz():

    """
    END_OF_QUIZ: Once the 20 word limit is reached from the if statements in right_answer() 
    or wrong_answer() this function will be called. It will reveal a list of right and wrong
    answers.
    """
    global right_answers, wrong_answers

    # configure text that appears
    vocab_label.config(text=f"Right answers: {right_answers}\n Wrong answers: {wrong_answers}")

    # Join the Japanese, Romaji, and English from the right/wrong lists.
    # Learned how to use a for loop when assigning values to a variable. This is a common
    # practice in data science for cleaner code.
    right_text = "\n".join([f"{r["Japanese"]}, {r["Romaji"]}, {r["English"]}" for r in right_list])
    wrong_text = "\n".join([f"{r["Japanese"]}, {r["Romaji"]}, {r["English"]}" for r in wrong_list])

    # Assign the text of the labels to the list of right and wrong answers
    right_answers_list.config(text=f"Vocab Right: \n\n{right_text}")
    wrong_answers_list.config(text=f"Vocab Wrong: \n\n{wrong_text}")

    start_quiz.grid(
        column=2, 
        row=5)
    
    right_button.grid_forget()
    wrong_button.grid_forget()
    displayEng.grid_forget()

# ------------------------------------------------------------------------------------------------
# Tkinter labels and buttons
# ------------------------------------------------------------------------------------------------

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

# Label for english display (hidden)
english = ttk.Label(frm, text="", font=("Arial", 15))
english.grid(
    column=1, 
    row=2,
    columnspan=2)

# Label for right answers
right_answers_list = ttk.Label(frm, text="", font=("Ariel", 10))
right_answers_list.grid(
    column=1, 
    row=4, 
    padx=50, 
    pady=0)

# Label for wrong answers
wrong_answers_list = ttk.Label(frm, text="", font=("Ariel", 10))
wrong_answers_list.grid(
    column=3, 
    row=4, 
    padx=50, 
    pady=0)

# Buttons ----------------------------------------------------------------------------------------

# Start quiz button - Triggers initialization( ) function
start_quiz = ttk.Button(frm, text="Start Quiz", command=initialization)
start_quiz.grid(
    column=2, 
    row=5)

# Event loop - Ensures the window remains active and repsonsive to user interactions.
root.mainloop()