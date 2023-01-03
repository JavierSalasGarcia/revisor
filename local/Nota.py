# Basado en el script de "ProjectGurukul's Voice recorder"
# Librerías necesarias para ejecutar este código
import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
from tkinter import messagebox
import os

def next_path(path_pattern):
    """
    Encuentra el siguiente archivo que se debe escribir siguiendo un patrón
    ejemplo del patrón:  path_pattern = 'file-%s.txt':

    file-1.txt
    file-2.txt
    file-3.txt
    """
    i = 1

    # Hace una búsqueda exponencial
    while os.path.exists(path_pattern % i):
        i = i * 2

    # El resultado está entre (i/2..i]
    # llamada a este intervalo (a..b] y lo va estrechando hasta que a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2 # mitad del intervalo
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)

    return path_pattern % b

#Define la interfaz del usuario
voice_rec = Tk()
voice_rec.geometry("360x200")
voice_rec.title("Grabadora Javier Salas")
voice_rec.config(bg="#107dc2")

#contenedor del audio data
q = queue.Queue()
#Declara las variables y las inicializa
recording = False
file_exists = False    

#Fit data into queue
def callback(indata, frames, time, status):
    q.put(indata.copy())

#Functions to play, stop and record audio
#The recording is done as a thread to prevent it being the main process
def threading_rec(x):
    if x == 1:
        #If recording is selected, then the thread is activated
        t1=threading.Thread(target= record_audio)
        t1.start()
    elif x == 2:
        #To stop, set the flag to false
        global recording
        recording = False
        # messagebox.showinfo(message="Recording finished")

#Recording function
def record_audio():
    #Declare global variables    
    global recording 
    #Set to True to record
    recording= True   
    global file_exists 
    #Create a file to save the audio
    # messagebox.showinfo(message="Recording Audio. Speak into the mic")
    d = next_path('notaJSG-%s.wav')
    print(d)
    notavozfile = d
    with sf.SoundFile(notavozfile, mode='w', samplerate=44100,
                        channels=2) as file:
    #Create an input stream to record audio without a preset time
            with sd.InputStream(samplerate=44100, channels=2, callback=callback):
                while recording == True:
                    #Set the variable to True to allow playing the audio later
                    file_exists =True
                    #write into file
                    file.write(q.get())

#Label to display app title
title_lbl  = Label(voice_rec, text="Notas voz", bg="#107dc2").grid(row=0, column=0, columnspan=3)


#Button to record audio
record_btn = Button(voice_rec, text="Grabar Nota", command=lambda m=1:threading_rec(m))
#Stop button
stop_btn = Button(voice_rec, text="Detener", command=lambda m=2:threading_rec(m))
#Play button
# play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3:threading_rec(m))

#Position buttons
record_btn.grid(row=1,column=1)
stop_btn.grid(row=1,column=0)
# play_btn.grid(row=1,column=2)
voice_rec.mainloop()

