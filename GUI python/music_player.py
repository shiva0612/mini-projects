import tkinter
from tkinter import *
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk

import os
from mutagen.mp3 import MP3
import threading
import time

global paused

mixer.init()
root = tk.ThemedTk()
root.get_themes()  # Returns a list of all themes that can be set
root.set_theme("radiance")

play_this = []

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30)

rightframe = Frame(root)
rightframe.pack()

topframe = Frame(rightframe)
topframe.pack()

middleframe = Frame(rightframe)
middleframe.pack(padx=30, pady=30)

bottomframe = Frame(rightframe)
bottomframe.pack(padx=10, pady=10)

root.title("njy your music")

paused = False


def on_closing():
    mixer.music.stop()
    root.destroy()


def start_count(len):
    x = 0;
    while x <= len and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = x / 60, x % 60
            mins = round(mins)
            secs = round(secs)
            status["text"] = str(mins) + " : " + str(secs)
            time.sleep(1)
            x += 1


def play_music():
    global paused
    if paused == True:
        mixer.music.unpause()
        statusbar['text'] = "resumed:"

        paused = False

    else:
        try:
            stop_music()
            time.sleep(1)
            selectedsong = list.curselection()
            selectedsong = int(selectedsong[0])  # bcz, it gives tuple (0,)
            play_it = play_this[selectedsong]
            mixer.music.load(play_it)
            mixer.music.play()
            print("playing")
            statusbar["text"] = "playing:" + os.path.basename(play_it)
            a = MP3(play_it)
            len = a.info.length
            leng["text"] = "length : " + str(round(len / 60)) + " : " + str(round(len % 60))

            t1 = threading.Thread(target=start_count, args=(len,))
            t1.start()
        except NameError:
            tkinter.messagebox.showerror("shiva", "error")


def stop_music():
    mixer.music.stop()
    statusbar["text"] = "stopped:"


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar["text"] = "paused:"
def scale_volume(val):
    vol = float(val) / 100
    mixer.music.set_volume(vol)


muted = False


def mute():
    global muted
    if muted:
        scale.set(70)
        mixer.music.set_volume(0.7)
        volbtn.configure(image=vol_photo)
        statusbar["text"] = "playing"
        muted = False
    else:
        scale.set(0)
        mixer.music.set_volume(0)
        volbtn.configure(image=mute_photo)
        statusbar["text"] = "muted"
        muted = True


def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)


def add_to_playlist(filename_path):
    global filename
    filename = os.path.basename(filename_path)
    index = 0;
    list.insert(index, filename)
    play_this.insert(index, filename_path)
    index += 1


def del_playlist():
    a = list.curselection()
    a = int(a[0])
    del play_this[a]
    list.delete(a)

print("def")

menubar = Menu()
root.config(menu=menubar)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="file", menu=submenu)
submenu.add_command(label="open", command=browse_file)

list = Listbox(leftframe)
list.pack(padx=30)

addbtn = ttk.Button(leftframe, text="add", command=browse_file)
addbtn.pack(side=LEFT)

delbtn = ttk.Button(leftframe, text="del", command=del_playlist)
delbtn.pack(side=LEFT)

leng = ttk.Label(topframe, text="length of the audio:")
leng.pack()

status = ttk.Label(topframe, text="please play some music: ")
status.pack(pady=20)

play_photo = PhotoImage(file='play.png')
playbtn = ttk.Button(middleframe, image=play_photo, command=play_music)
playbtn.grid(row=0, column=0, padx=10)

stop_photo = PhotoImage(file='stop.png')
stopbtn = ttk.Button(middleframe, image=stop_photo, command=stop_music)
stopbtn.grid(row=0, column=1, padx=10)

pause_photo = PhotoImage(file='pause.png')
pausebtn = ttk.Button(middleframe, image=pause_photo, command=pause_music)
pausebtn.grid(row=0, column=2, padx=10)

rewind_photo = PhotoImage(file='rewind.png')
rewindbtn = ttk.Button(bottomframe, image=rewind_photo, command=play_music)
rewindbtn.grid(row=0, column=0, padx=10)

vol_photo = PhotoImage(file='vol.png')
mute_photo = PhotoImage(file='mute.png')
volbtn = ttk.Button(bottomframe, image=vol_photo, command=mute)
volbtn.grid(row=0, column=1, padx=10)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=scale_volume)
scale.grid(row=0, column=2)
scale.set(70)
mixer.music.set_volume(0.7)

statusbar = Label(root, text="status:", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
