from tkinter import *
from tkinter import messagebox
from logic import shareEmail
from pygame import mixer

def setWinSound():
    mixer.init()
    mixer.music.load("../asset/song/winCondition.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

def main(winOrder, playerEmail):
    Tk().wm_withdraw() #to hide the main window

    position = ""
    if winOrder == 1: position ="first"
    elif winOrder == 2: position ="second"
    elif winOrder == 3: position = "third"
    elif winOrder == 4: position = "fourth"

    setWinSound()

    message = 'Congratulations, you have finished ' + position + ' place. Do you want to share it to your email ?'
    result = messagebox.askquestion('Congratulations',message)

    if result == "yes":
        shareEmail.main(playerEmail, position)