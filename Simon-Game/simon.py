# Import required libraries
from tkinter import *
import random
import threading
import time
from tapsdk import TapSDK
from tapsdk import TapSDK, TapInputMode
from tapsdk.models import AirGestures
import csv

# Initialize global variables
tap_instance = []
tap_identifiers = []
codelist = []

prophet_dict = {
    'pinky': 5,
    'ring Finger': 4,
    'Middle Finger': 3,
    'Index Finger': 2
}

# Create the main window
win = Tk()
win.title("Simon Game")
win.geometry('232x410')
win.resizable(width=0, height=0)

# Define global variables
global Green
global Red
global Yellow
global Blue
global watch
global count
global tmp
global gameover
global timer_count
global score
global input_text
score = 0
timer_count = 0
watch = True
gameover = False
stt = []
tmp = len(stt)
tmp_stt = []

# Check if the game is not over
if gameover == False:
    # Function to change color of buttons based on the sequence
    def ChangeColor(i=5):
        global stt
        global watch
        global count
        global timer_count
        count = len(stt)

        for i in stt:
            time.sleep(0.2)

            if i == 5:
                win.after((timer_count + 300), lambda: Green.config(bg='green'))
                win.after((timer_count + 500), lambda: Green.config(bg='#003300'))

            elif i == 2:
                win.after((timer_count + 300), lambda: Red.config(bg='red'))
                win.after((timer_count + 500), lambda: Red.config(bg='#550000'))

            elif i == 3:
                win.after((timer_count + 300), lambda: Yellow.config(bg='yellow'))
                win.after((timer_count + 500), lambda: Yellow.config(bg='#555500'))

            elif i == 4:
                win.after((timer_count + 300), lambda: Blue.config(bg='blue'))
                win.after((timer_count + 500), lambda: Blue.config(bg='#000055'))

            timer_count += 220

    # Function to process the user input as a string
    def Stringcutting(num_str='1'):
        if len(stt) == len(num_str):
            for digit in num_str:
                press(int(digit))
        else:
            gameover = True

            with open('input.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                stt.append(num)
                writer.writerow(stt)

            l1.configure(text="GAMEOVER")

    # Function to simulate button press
    def press(num=5):
        global watch
        global gameover
        global count
        global score
        if count > 0 and watch == False:
            if watch == False:
                if num == 5:
                    tmp_stt.append(5)
                    check(count, (len(tmp_stt) - 1), num)
                    count -= 1

                elif num == 2:
                    tmp_stt.append(2)
                    check(count, (len(tmp_stt) - 1), num)
                    count -= 1

                elif num == 3:
                    tmp_stt.append(3)
                    check(count, (len(tmp_stt) - 1), num)
                    count -= 1

                elif num == 4:
                    tmp_stt.append(4)
                    check(count, (len(tmp_stt) - 1), num)
                    count -= 1

        if count <= 0 and gameover == False:
            score += 1
            l0.config(text=score)
            watch = True
            tmp_stt.clear()
            start(watch, gameover)

    # Function to check user input against the sequence
    def check(count=100, x=0, num=5):
        global stt
        global gameover
        if stt[x] != num:
            gameover = True

            with open('input.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                stt.append(num)
                writer.writerow(stt)

            l1.configure(text="GAMEOVER")

    # Function to handle tap events
    def on_tap_event(identifier, tapcode):
        print(identifier, str(tapcode))

        if tapcode == 16:
            codelist.append(5)
        elif tapcode == 8:
            codelist.append(4)
        elif tapcode == 4:
            codelist.append(3)
        elif tapcode == 2:
            codelist.append(2)
        else:
            gameover = True
            exit()

            with open('input.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                stt.append(num)
                writer.writerow(stt)

            l1.configure(text="GAMEOVER")

        if len(stt) == len(codelist):
            for digit in codelist:
                press(digit)
        else:
            gameover = True
            exit()

            with open('input.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                stt.append(num)
                writer.writerow(stt)

            l1.configure(text="GAMEOVER")

    # GUI elements
    l0 = Label(win, text="0", font=("Courier", 25))
    l0.grid(padx=10, pady=2, row=0, columnspan=2)

    l1 = Label(win, text="Simon game with tap")
    l1.grid(padx=10, pady=2, row=1, columnspan=2)

    win.title("Simon game")

    text_entry = Entry(win, width=20)
    text_entry.grid(padx=10, pady=2, row=5, columnspan=2)

    # Function to handle submit button click
    def submit_action(entry_widget):
        text = entry_widget.get()
        Stringcutting(text)
        entry_widget.delete(0, END)

    submit_button = Button(win, text="Submit", command=lambda: submit_action(text_entry))
    submit_button.grid(padx=10, pady=2, row=4, columnspan=2)
    text_entry.delete(0, 'end')

    # Buttons for different colors
    Green = Button(win, text="5-pinky", font=1, bg="#003300", activebackground='green', width=8, height=4,
                   command=lambda: press(5))
    Green.grid(padx=5, pady=10, row=2, column=0)

    Red = Button(win, text="2-Index", font=1, bg="#550000", activebackground='red', width=8, height=4,
                 command=lambda: press(2))
    Red.grid(padx=5, pady=10, row=2, column=1)

    Yellow = Button(win, text="3-Middle", font=1, bg="#555500", activebackground='yellow', width=8, height=4,
                    command=lambda: press(3))
    Yellow.grid(padx=5, pady=10, row=3, column=0)
    Blue = Button(win, text="4- Ring", font=1, bg="#000055", activebackground='blue', width=8, height=4,
                  command=lambda: press(4))
    Blue.grid(padx=5, pady=10, row=3, column=1)

    # Function to start the game with a random color sequence
    def first():
        global watch
        global gameover
        if watch == True and gameover == False:
            tmp = random.randint(2, 5)
            stt.append(tmp)
            win.after(1000, ChangeColor)
            watch = False

    # Function to start the game
    def start(a=True, b=False):
        global watch
        global stt
        if a == True and b == False:
            tmp = random.randint(2, 5)
            stt.append(tmp)
            ChangeColor()
            watch = False

    # Main function
    if __name__ == "__main__":
        tap_instance = TapSDK()
        tap_instance.run()
        tap_instance.set_input_mode(TapInputMode("raw"))
        tap_instance.register_tap_events(on_tap_event)

        first()
        mainloop()
