import PySimpleGUI as sg
import keyboard
from random import *
import _thread
import time

layout = [
    [sg.Text('Satır 1', key="txtstr1"),  sg.Input(key="inputstr1",  size=(34, 18))],
    [sg.Text('Satır 2', key="txtstr2"), sg.Input(key="inputstr2", size=(34, 18))],
    [sg.Text('Satır 3', key="txtstr3"), sg.Input(key="inputstr3", size=(34, 18))],
    [sg.Text('Satır 4', key="txtstr4"), sg.Input(key="inputstr4", size=(34, 10))],
    [sg.Text('',)],
    [sg.Text('En kısa zaman ', key="txtmin"), sg.Spin(["Saniye", "Dakika", "Saat   "], key="smin", readonly=True), sg.Input(key="inputmin", size=(18, 18))],
    [sg.Text('En uzun zaman', key="txtmax"), sg.Spin(["Saniye", "Dakika", "Saat   "], key="smax", readonly=True), sg.Input(key="inputmax", size=(18, 18))],
    [sg.Button("Ayarla", key = "setup", size = (8,1)), sg.Text("        ",key = "txtstatus"), sg.Button("Başlat", key = "start", size = (8,1)),sg.Button("Durdur", key = "stop", size = (8,1))]
]

window = sg.Window('Oto Yazıcı by thozoz', layout)

button = False
ayar = False
run = False


def deneme():
    global run
    if button and run == False:


        run = True
        #print(1)
        #print(run)
        time.sleep(randint(int(sayik), int(sayib)))
        if button:
            #print("Yazılıyor")
            window["txtstatus"].update("Yazılıyor")
            keyboard.write(str1)
            keyboard.press_and_release('shift + enter')
            keyboard.write(str2)
            keyboard.press_and_release('shift + enter')
            keyboard.write(str3)
            keyboard.press_and_release('shift + enter')
            keyboard.write(str4)
            keyboard.send("enter")
            window["txtstatus"].update("        ")

        _thread.start_new_thread(deneme2, ())



def deneme2():
    if button:
        global run
        run = False
        #print(2) debugging
        _thread.start_new_thread(deneme, ())



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "setup":

        button = True
        sayikk = values["inputmin"]
        sayibb = values["inputmax"]
        if sayikk.isnumeric() == False or sayibb.isnumeric() == False:
            window["txtstatus"].update("Sayı giriniz")
        else:
            global sayik
            global sayib
            global yazi

            ayar = True
            window["txtstatus"].update("        ")

            spinmin = values["smin"]
            spinmax = values["smax"]
            sayik = 0
            sayib = 0
            if spinmin == "Saniye":

                #print("Saniye")
                sayik = int(sayikk) * 1
                #print(sayik)
            elif spinmin == "Dakika":

                #print("Dakika")
                sayik = int(sayikk) * 60
                #print(sayik)
            elif spinmin == "Saat   ":

                #print("Saat   ")
                sayik = int(sayikk) * 3600
                #print(sayik)

            if spinmax == "Saniye":

                #print("Saniye")
                sayib = int(sayibb) * 1
                #print(sayib)

            elif spinmax == "Dakika":

                #print("Dakika")
                sayib = int(sayibb) * 60
                #print(sayib)

            elif spinmax == "Saat   ":
                #print("Saat")
                sayib = int(sayibb) * 3600
                #print(sayib)


            str1 = values["inputstr1"]
            str2 = values["inputstr2"]
            str3 = values["inputstr3"]
            str4 = values["inputstr4"]


    if event == "stop":

        button = False
        window["txtstatus"].update("        ")
        run = False
        #print("Durduruldu")



    if event == "start":

        if run:
            window["txtstatus"].update("Zaten çalışıyor")
        else:
            if ayar:

                #print("Başlıyor")
                button = True
                _thread.start_new_thread(deneme, ())

            else:

                window["txtstatus"].update("Ayarla")



window.close()
