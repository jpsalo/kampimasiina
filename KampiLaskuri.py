# coding: utf-8

# In[ ]:

#!/usr/bin/env python3

#

# Creates three "windows" that the user can navigate through using Back and Next - buttons.

import tkinter as tk
from tkinter import LEFT, TOP, BOTTOM, PhotoImage
import time
import serial

# Globaalit muuttujat
tokasivu_kaynnistetty = time.time()
ansaittu = 0
euroaPerTunti = 10
taustavari = 'purple3'
tekstivari = 'white'
isofontti=("Helvetica", 40)
pikkufontti=("Helvetica",20)
serialLaskuri = 0
montakoSekuntiaSallitaan = 8
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/tty.usbmodem1411'  # NOTE: Change this to COM1
nollausaika = time.time()
aikaaEdellisestaNollauksesta = time.time()-nollausaika


def readSerial(ser):
    ser.open()
    value = float(ser.readline().strip())
    ser.close()
    return value

def nollaaLaskuri():
    global aikaaEdellisestaNollauksesta
    global nollausaika
    aikaaEdellisestaNollauksesta = 0
    nollausaika = time.time()


def paivita_ekaasivu():
    tulos = readSerial(ser)
    if tulos == edellinenTulos:
        root.ekansivunPaivitysTehtava = root.after(500,paivita_ekaasivu)
    else:
        tokasivu_paalle()

def paivita_tokasivu():
    global aikaaEdellisestaNollauksesta
    global nollausaika
    global ansaittu
    
    
    nyt = time.time()
    ansaittu = (nyt - tokasivu_kaynnistetty) * euroaPerTunti/3600
    ansaittu_teksti = '{0:.2f}'.format(ansaittu) + ' €'
    tokasivu_teksti.configure(text=ansaittu_teksti)
    tokasivu_teksti.pack()
   
    if (aikaaEdellisestaNollauksesta < montakoSekuntiaSallitaan):
        tulos = readSerial(ser)
        if tulos == edellinenTulos:
            aikaaEdellisestaNollauksesta = time.time()-nollausaika
            #print(aikaaEdellisestaNollauksesta)
            tokasivu_teksti_progress.configure(text='●'*int(montakoSekuntiaSallitaan-aikaaEdellisestaNollauksesta)+'○'*int(aikaaEdellisestaNollauksesta))            
        else:
            nollausaika = time.time()
        root.tokansivunPaivitysTehtava = root.after(100, paivita_tokasivu)
    else:
        root.after_cancel(root.tokansivunPaivitysTehtava)
        kolmossivu_paalle()
 
def ekasivu_paalle():
    # Piilotetaan muut ikkunat ja näytetään eka
    tokasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()    
    ekasivu.pack(padx=20,pady=40)
    paivita_ekaasivu()

def tokasivu_paalle():
    # Piilotetaan muut ikkunat ja näytetään toka
    global tokasivu_kaynnistetty
    
    nollaaLaskuri()
    ekasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()    
    tokasivu.pack(padx=20,pady=40)
    tokasivu_kaynnistetty = time.time()
    paivita_tokasivu()

def luo_kolmossivu():
    # Piilotetaan muut ikkunat ja näytetään kolmos
    
    root.kolmossivu_teksti = tk.Label(kolmossivu, text='Kiitos!',font=isofontti,bg=taustavari,fg=tekstivari)
    root.kolmossivu_leipa = tk.Label(kolmossivu, text='',font=pikkufontti,wraplength=300,justify='center',bg=taustavari,fg=tekstivari)
    #root.kolmossivu_aloitaAlustaNappi = tk.Button(kolmossivu, text = "Uusi", command = uusi_ohjelma)
    #root.kolmossivu_suljenappi = tk.Button(kolmossivu, text = "Quit", command = sulje_ohjelma)
    
   
def kolmossivu_paalle():
    # Piilotetaan muut ikkunat ja näytetään kolmos
    tokasivu.pack_forget()
    kolmossivu.configure(background=taustavari)
    kolmossivu.pack(padx=20,pady=40)
    root.kolmossivu_teksti.pack(side=TOP)
    lopputeksti = ("Ansaitsit " + '{0:.2f}'.format(ansaittu) + " €." +
                   "Kerrotko vielä mikä on tunteesi tällä hetkellä?")
    root.kolmossivu_leipa.configure(text=lopputeksti)   
    root.kolmossivu_leipa.pack(side=TOP)
    
    root.kolmossivu_teksti.pack()
    root.kolmossivu_aloitaAlustaNappi.pack()
    
    #photo = PhotoImage(file='./pics/quit.png')
    #kolmossivu_suljenappi.config(image=photo)
    root.kolmossivu_suljenappi.pack()
    kysely.pack()    
    


def sulje_ohjelma():
    root.destroy()
    
def uusi_ohjelma():
    nollaaLaskuri()
    ekasivu_paalle()

def kiitos_palautteesta(event):
    print(event.x)
    nollaaLaskuri()
    ekasivu_paalle()

###############################
# Main program starts here :) #
###############################

# Luodaan pääohjelma(ikkuna)
root = tk.Tk()




# Määritetään pääikkunan koko fullscreeniksi
window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (window_w, window_h))
root.configure(background=taustavari)


# Luodaan sivut

# EKASIVU
ekasivu=tk.Frame(root, width=window_w, height=window_h)
ekasivu.configure(background=taustavari)
ekasivu.pack(padx=20,pady=40)
ekasivu_teksti = tk.Label(ekasivu, text='Pyöritä ja Ansaitse',bg=taustavari,fg=tekstivari,font=isofontti)
ekasivu_teksti.pack(side=TOP)
ekasivu_leipateksti = ("Ansaitse rahaa pyörittämällä kampea."+
                         "Näet hankkimasi rahat ruudulla. Yliopiston tutkija maksaa ansaitsemasi summan "+
                         "välittömästi kun olet lopettanut pyörittämisen.")
ekasivu_leipa = tk.Label(ekasivu, text=ekasivu_leipateksti,
                         bg=taustavari,fg=tekstivari,font=pikkufontti,wraplength=400,justify='center')
ekasivu_leipa.pack(side=TOP)


#ekasivu_suljenappi = tk.Button(ekasivu, command = sulje_ohjelma)
#ekasivu_suljenappi.pack()
#ekasivu_seuraavanappi = tk.Button(ekasivu, text = "Next", command = tokasivu_paalle)
#ekasivu_seuraavanappi.pack()


tokasivu=tk.Frame(root, width=window_w, height=window_h)
tokasivu.configure(background=taustavari)
tokasivu.pack(padx=20,pady=400)
tokasivu_teksti = tk.Label(tokasivu, text="",bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti.pack(side=TOP)
tokasivu_teksti_progress = tk.Label(tokasivu,text='●●●●●●●',bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti_progress.pack(side=TOP)

#tokasivu_takaisinnappi= tk.Button(tokasivu, text = "Back", command = ekasivu_paalle)
#tokasivu_takaisinnappi.pack(side=BOTTOM)
#tokasivu_seuraavanappi = tk.Button(tokasivu, text = "Next", command = kolmossivu_paalle)
#tokasivu_seuraavanappi.pack(side=BOTTOM)

kolmossivu=tk.Frame(root, width=window_w, height=window_h)
luo_kolmossivu()

kysely=tk.Frame(root,width=window_w,height=window_h)
nappi1=tk.Label(kysely,text='①',bg=taustavari,fg=tekstivari,font=isofontti)
nappi1.bind("<Button-1>",kiitos_palautteesta)
nappi1.pack(side=LEFT)
nappi2=tk.Label(kysely,text='②',bg=taustavari,fg=tekstivari,font=isofontti)
nappi2.bind("<Button-1>",kiitos_palautteesta)
nappi2.pack(side=LEFT)
nappi3=tk.Label(kysely,text='③',bg=taustavari,fg=tekstivari,font=isofontti)
nappi3.bind("<Button-1>",kiitos_palautteesta)
nappi3.pack(side=LEFT)
nappi4=tk.Label(kysely,text='④',bg=taustavari,fg=tekstivari,font=isofontti)
nappi4.bind("<Button-1>",kiitos_palautteesta)
nappi4.pack(side=LEFT)
nappi5=tk.Label(kysely,text='⑤',bg=taustavari,fg=tekstivari,font=isofontti)
nappi5.bind("<Button-1>",kiitos_palautteesta)
nappi5.pack(side=LEFT)
kysely.pack(side=TOP)


#kolmossivu_takaisinnappi = tk.Button(kolmossivu, text = "Back", command = tokasivu_paalle)
#kolmossivu_takaisinnappi.pack()


# Jätetään eka sivu näkyviin (unhidden).
edellinenTulos = readSerial(ser)
ekasivu_paalle()

# Start tkinter event - loop
root.mainloop()
