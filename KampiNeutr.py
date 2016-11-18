
# coding: utf-8

# In[ ]:

#!/usr/bin/env python3

#

# Creates three "windows" that the user can navigate through using Back and Next - buttons.

import Tkinter as tk
from Tkinter import LEFT, TOP, BOTTOM, PhotoImage
import time
import serial

testiNimi = "Neutr"

nollasivu_otsikko = ("OSALLISTU NEUTRAALIIN \n TUTKIMUKSEEN")
nollasivu_leipateksti = ("Tämä tutkimus koskee."+
                         "blaa blaa "+
                         "et kuitenkaan lue tänne asti.")
ekasivu_otsikkoteksti = ("OHJEET")
ekasivu_leipateksti = ("Ansaitse rahaa pyörittämällä kampea."+
                         "Näet tilanteen lennosta"+
                         "Rahta saat jos luoja suo.")
kiitossivu_otsikko = ("KIITOS OSALLISTUMISESTASI")
kiitossivu_leipateksti = ("Tutkija maksaa sinulle keräämästi rahasumman:"+
                         "Älä tuhlaa heti kaikkea!")
tokasivu_teksti1_otsikko = ("Olet ansainnut itsellesi:")

# Globaalit muuttujat
tokasivu_kaynnistetty = time.time()
ansaittu = 0
euroaPerTunti = 10
taustavari = 'black'
tekstivari = 'white'
isofontti=("Helvetica", 80)
pikkufontti=("Helvetica",40)
serialLaskuri = 0
montakoSekuntiaSallitaan = 8
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
nollausaika = time.time()
aikaaEdellisestaNollauksesta = time.time()-nollausaika
arvosana1 = 0
arvosana2 = 0



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


def paivita_tokasivu():
    global aikaaEdellisestaNollauksesta
    global nollausaika
    global ansaittu
    
    
    nyt = time.time()
    ansaittu = (nyt - tokasivu_kaynnistetty) * euroaPerTunti/3600
    ansaittu_teksti = '{0:.2f}'.format(ansaittu) + ' €'
    tokasivu_teksti2.configure(text=ansaittu_teksti)
    tokasivu_teksti2.pack()
   
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

def nollasivu_paalle():
    ekasivu.pack_forget()    
    tokasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()
    kysely2.pack_forget()
    kiitossivu.pack_forget()    
    nollasivu.pack(padx=20,pady=40)

    
 
def ekasivu_paalle():
    # Piilotetaan muut ikkunat ja näytetään eka
    nollasivu.pack_forget()
    tokasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()    
    kiitossivu.pack_forget()
    ekasivu.pack(padx=20,pady=40)

def tokasivu_paalle():
    # Piilotetaan muut ikkunat ja näytetään toka
    global tokasivu_kaynnistetty
    
    nollaaLaskuri()
    ekasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()    
    kiitossivu.pack_forget()
    tokasivu.pack(padx=20,pady=40)
    tokasivu_kaynnistetty = time.time()
    paivita_tokasivu()

def kolmossivu_paalle():
    tokasivu.pack_forget()
    kiitossivu.pack_forget()
    lopputeksti = ("Ansaitsit " + '{0:.2f}'.format(ansaittu) + " €.\n" +
                   "Miltä tuntuu (1-5)?")
    kolmossivu_leipa.configure(text=lopputeksti)   
    kolmossivu.pack(padx=20,pady=40)    
    kysely.pack(side=TOP)  
    kysely2.pack(side=TOP)      
    kolmossivu_alaosa.pack(side=TOP)
    
def kiitossivu_paalle():
    nollasivu.pack_forget()    
    ekasivu.pack_forget()    
    tokasivu.pack_forget()
    kolmossivu.pack_forget()
    kysely.pack_forget()    
    kysely2.pack_forget()        
    kolmossivu_alaosa.pack_forget()
    kiitossivu.pack(padx=20,pady=40)
    aikaleima = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tokasivu_kaynnistetty))
    output_teksti = (testiNimi + " "+ aikaleima + " " + '{0:.2f}'.format(ansaittu) + " " + str(arvosana1) + str(arvosana2) + '\n')
    with open("Output.txt", "a") as text_file:
        text_file.write(output_teksti)

def sulje_ohjelma():
    root.destroy()

def muutanumeroksi(nappinumero):
    nappinumerot = ['①','②','③','④','⑤']    
    return nappinumerot.index(nappinumero)+1
    
def uusi_ohjelma():
    nollaaLaskuri()
    ekasivu_paalle()

def kiitos_palautteesta1(event):
    global arvosana1    
    for wid in kysely1Napit:
        wid.configure(fg = tekstivari)
    event.widget.configure(fg='red')
    arvosana1 = muutanumeroksi(event.widget.cget("text"))
    

def kiitos_palautteesta2(event):
    global arvosana2    
    for wid in kysely2Napit:
        wid.configure(fg = tekstivari)
    event.widget.configure(fg='red')
    arvosana2 = muutanumeroksi(event.widget.cget("text"))
    
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

# NOLLASIVU
nollasivu=tk.Frame(root, width=window_w, height=window_h)
nollasivu.configure(background=taustavari)
nollasivu.pack(padx=20,pady=40)
nollasivu_teksti = tk.Label(nollasivu, text=nollasivu_otsikko,bg=taustavari,fg=tekstivari,font=isofontti)
nollasivu_teksti.pack(side=TOP)
nollasivu_leipa = tk.Label(nollasivu, text=nollasivu_leipateksti,
                         bg=taustavari,fg=tekstivari,font=pikkufontti,wraplength=800,justify='center')
nollasivu_leipa.pack(side=TOP)
nollasivu_jatka = tk.Button(nollasivu,text="Haluan osallistua",command=ekasivu_paalle)
nollasivu_jatka.pack(side=TOP)

# EKASIVU
ekasivu=tk.Frame(root, width=window_w, height=window_h)
ekasivu.configure(background=taustavari)
ekasivu.pack(padx=20,pady=40)
ekasivu_teksti = tk.Label(ekasivu, text=ekasivu_otsikkoteksti,bg=taustavari,fg=tekstivari,font=isofontti)
ekasivu_teksti.pack(side=TOP)
ekasivu_leipa = tk.Label(ekasivu, text=ekasivu_leipateksti,
                         bg=taustavari,fg=tekstivari,font=pikkufontti,wraplength=800,justify='center')
ekasivu_leipa.pack(side=TOP)
ekasivu_jatka = tk.Button(ekasivu,text="Aloita koe",command=tokasivu_paalle)
ekasivu_jatka.pack(side=TOP)


# TOKASIVU
tokasivu=tk.Frame(root, width=window_w, height=window_h)
tokasivu.configure(background=taustavari)
tokasivu.pack(padx=20,pady=400)
tokasivu_teksti_progress = tk.Label(tokasivu,text='●●●●●●●',bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti_progress.pack(side=TOP)
tokasivu_teksti1 = tk.Label(tokasivu, text=tokasivu_teksti1_otsikko,bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti1.pack(side=TOP)
tokasivu_teksti2 = tk.Label(tokasivu, text="",bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti2.pack(side=TOP)
tokasivu_teksti4 = tk.Label(tokasivu, text="",bg=taustavari,fg=tekstivari,font=isofontti)
tokasivu_teksti4.pack(side=TOP)


# KOLMOSSIVU
kolmossivu=tk.Frame(root, width=window_w, height=window_h)
kolmossivu.configure(background=taustavari)
kolmossivu.pack()
kolmossivu_teksti = tk.Label(kolmossivu, text='ONNEKSI OLKOON!',font=isofontti,bg=taustavari,fg=tekstivari)
kolmossivu_teksti.pack()
kolmossivu_leipa = tk.Label(kolmossivu, text='',font=pikkufontti,wraplength=800,justify='center',bg=taustavari,fg=tekstivari)
kolmossivu_leipa.pack()
kysely=tk.Frame(root,width=window_w,height=window_h)
nappi1=tk.Label(kysely,text='①',bg=taustavari,fg=tekstivari,font=isofontti)
nappi1.bind("<Button-1>",kiitos_palautteesta1)
nappi1.pack(side=LEFT)
nappi2=tk.Label(kysely,text='②',bg=taustavari,fg=tekstivari,font=isofontti)
nappi2.bind("<Button-1>",kiitos_palautteesta1)
nappi2.pack(side=LEFT)
nappi3=tk.Label(kysely,text='③',bg=taustavari,fg=tekstivari,font=isofontti)
nappi3.bind("<Button-1>",kiitos_palautteesta1)
nappi3.pack(side=LEFT)
nappi4=tk.Label(kysely,text='④',bg=taustavari,fg=tekstivari,font=isofontti)
nappi4.bind("<Button-1>",kiitos_palautteesta1)
nappi4.pack(side=LEFT)
nappi5=tk.Label(kysely,text='⑤',bg=taustavari,fg=tekstivari,font=isofontti)
nappi5.bind("<Button-1>",kiitos_palautteesta1)
nappi5.pack(side=LEFT)
kysely1Napit = [nappi1,nappi2,nappi3,nappi4,nappi5]
kysely.pack(side=TOP)
kysely2=tk.Frame(root,width=window_w,height=window_h)
nappi6=tk.Label(kysely2,text='①',bg=taustavari,fg=tekstivari,font=isofontti)
nappi6.bind("<Button-1>",kiitos_palautteesta2)
nappi6.pack(side=LEFT)
nappi7=tk.Label(kysely2,text='②',bg=taustavari,fg=tekstivari,font=isofontti)
nappi7.bind("<Button-1>",kiitos_palautteesta2)
nappi7.pack(side=LEFT)
nappi8=tk.Label(kysely2,text='③',bg=taustavari,fg=tekstivari,font=isofontti)
nappi8.bind("<Button-1>",kiitos_palautteesta2)
nappi8.pack(side=LEFT)
nappi9=tk.Label(kysely2,text='④',bg=taustavari,fg=tekstivari,font=isofontti)
nappi9.bind("<Button-1>",kiitos_palautteesta2)
nappi9.pack(side=LEFT)
nappi10=tk.Label(kysely2,text='⑤',bg=taustavari,fg=tekstivari,font=isofontti)
nappi10.bind("<Button-1>",kiitos_palautteesta2)
nappi10.pack(side=LEFT)
kysely2Napit = [nappi6,nappi7,nappi8,nappi9,nappi10]
kysely2.pack(side=TOP)


kolmossivu_alaosa=tk.Frame(root,width=window_w,height=window_h)
kolmossivu_jatka = tk.Button(kolmossivu_alaosa,text="Valmis",command=kiitossivu_paalle)
kolmossivu_jatka.pack(side=TOP)

# KIITOSSIVU
kiitossivu=tk.Frame(root, width=window_w, height=window_h)
kiitossivu.configure(background=taustavari)
kiitossivu.pack(padx=20,pady=40)
kiitossivu_teksti = tk.Label(kiitossivu, text=kiitossivu_otsikko,bg=taustavari,fg=tekstivari,font=isofontti)
kiitossivu_teksti.pack(side=TOP)
kiitossivu_leipa = tk.Label(kiitossivu, text=kiitossivu_leipateksti,
                         bg=taustavari,fg=tekstivari,font=pikkufontti,wraplength=800,justify='center')
kiitossivu_leipa.pack(side=TOP)
kiitossivu_jatka = tk.Button(kiitossivu,text="Aloita alusta",command=sulje_ohjelma)
kiitossivu_jatka.pack(side=TOP)


# Jätetään eka sivu näkyviin (unhidden).
edellinenTulos = readSerial(ser)
nollasivu_paalle()

# Start tkinter event - loop
root.mainloop()
