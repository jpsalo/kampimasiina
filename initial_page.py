import tkinter as tk

import config


def generate_initial_page(root, window_w, window_h, activate_next_page):
    initial_page = tk.Frame(root, width=window_w, height=window_h)
    initial_page.configure(background=config.background_color)
    initial_page.pack(padx=20, pady=40)
    initial_page_teksti = tk.Label(initial_page, text='Pyöritä ja Ansaitse',
                                   bg=config.background_color, fg=config.text_color, font=config.big_font)
    initial_page_teksti.pack(side=tk.TOP)
    initial_page_leipateksti = ("Ansaitse rahaa pyörittämällä kampea." +
                                "Näet hankkimasi rahat ruudulla. Yliopiston tutkija maksaa ansaitsemasi summan " +
                                "välittömästi kun olet lopettanut pyörittämisen.")
    initial_page_leipa = tk.Label(initial_page, text=initial_page_leipateksti,
                                  bg=config.background_color,
                                  fg=config.text_color, font=config.small_font,
                                  wraplength=400,
                                  justify='center')
    initial_page_leipa.pack(side=tk.TOP)

    initial_page_next_page_button = tk.Button(initial_page, text="Haluan osallistua tutkimukseen",
                                              command=activate_next_page)
    initial_page_next_page_button.pack()
    return initial_page
