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
    
#ICON ON THE APP

image_icon = PhotoImage(file='PATH_TO_LOGO')
root.iconphoto(False,image_icon)

Top = PhotoImage(file='PATH_TO_LOGO')
Label(root, image=Top, bg='#0f1a2b').pack()


#logo
Logo = PhotoImage(file='PATH_TO_LOGO')
Label(root,image=Logo, bg='#0f1a2b',bd=0).place(x=70, y=115)


#BUTTONS

ButtonPlay = PhotoImage(file='PATH_TO_IMAGE')
Button(root,image=ButtonPlay,bg='#0f1a2b', 
       bd=0,command=PlayMusic).place(x=100,y=400)

ButtonStop = PhotoImage(file='PATH_TO_IMAGE')
Button(root,image=ButtonStop,bg='#0f1a2b', 
       bd=0,command=mixer.music.stop).place(x=30,y=500)

ButtonResume = PhotoImage(file='PATH_TO_IMAGE')
Button(root,image=ButtonResume,bg='#0f1a2b', 
       bd=0,command=mixer.music.unpause).place(x=115,y=500)

ButtonPause = PhotoImage(file='PATH_TO_IMAGE')
Button(root,image=ButtonPause,bg='#0f1a2b', 
       bd=0,command=mixer.music.pause).place(x=200,y=500)

#LABEL



