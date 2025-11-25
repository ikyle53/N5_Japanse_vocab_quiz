# Japanese N5 level quiz
### Kyle Honaker | Final Project

This is my final project for Computer Science 115. My friends and I get together every Friday morning for Japanese language studies and I decided to make a tool to improve our recollection of vocabulary terms specifically tailored to the N5 level (survival Japanese). This program provides 20 words at a time to which the user can select the English button to see its English meaning. The user is presented with a right and wrong button to track how many they've gotten right or wrong. At the end of the quiz it shows 2 seperate summary lists of right words and wrong words with the ability to start over on 20 new words.

## Modules 👨‍💻
- Package manager is [pip](https://pip.pypa.io/en/stable/).
- [Pandas](https://pandas.pydata.org/) for pulling vocab from a large list stored in a CSV file and randomizing the selection.
- [TKinter](https://docs.python.org/3/library/tkinter.html) as my graphical user interface.

## Things I've learned 👨‍🏫
### Pandas 🐼
Pandas is a very large module that has a lot of powerful tools for manipulating data. The ```iloc()``` method stands for integer location. This essentially works like python's indexing methods where you call a certain item in a list like ```list[0]```. However, Pandas can go into columns and rows instead of using multiple for loops to access certain data (depending on how it's structured.)

I also replaced the random module for Pandas ```sample(n=20)``` method to pull 20 total vocab words. Made it easier to work with and replaced a few lines of code.

### TKinter 👨‍🎨
This module had me thinking outside the box on how to structure my code. Each button has a function tied to it that updates other pieces of the program as the vocab are called. Once I realized how to tie functions to buttons it became a lot easier to realize what to do with each function. It's a total of 7 functions that update the interface as the user goes through each word.

One of the harder aspects of TKinter was making the user experience better becuase I wasn't sure how to hide and show buttons. There's various methods that 'pull' a button from the interface stack and make it disappear. The biggest challenge was trying to make it reappear in the place I wanted it because it stripped the grid attributes from the button(s). I found out I could just create the buttons (again) in a function and they would still work as usual. I literally copy/pasted them into my intialization() function and all was well. Easy fix, but took a lot of brain power on my end...

Lastly, styling in TKinter is kinda clunky without having to go deep into rabbit holes to customize the window, get the grid system mastered, and sift through attributes to make everything tie together well. A lot of people suggest using imported themese like:

```
import  customtkinter as ctk
ctk.set_appearance_mode("dark")
app = ctk.CTK()
```
This would set all the labels, buttons, and text to a dark theme without having to do much customization. I played around with the grid system, made my own theme, and even added a background image to give it some appeal.


### As a whole 🌱
A few of the problems I faced stemmed from subtle undocumented behaviors in the underlying libraries. The correct solution(s) was sometimes intuitive but often required digging to uncover non-obvious fixes.

This was particularly true for getting some of the buttons to work. I originally had them set up outside functions, moved them to functions, figured out I had to set them as empty variables, and then update them globally to make them work in the way I wanted for a better user experience.

The rest of the code came together nicely. It had some hiccups but there were easy to resolve with some interface testing and moving parts around.