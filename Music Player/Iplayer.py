import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Iplayer')
root.geometry('920x600+290+85')
root.configure(background='#212121')
root.resizable(False,False)
mixer.init()


#----------------------------
#function to open music file
#----------------------------

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        
        
        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)
                
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
