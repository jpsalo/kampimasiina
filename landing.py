import tkinter as tk

import config


def generate_page(root, activate_next_page):
    page = tk.Frame(root)
    page.configure(background=config.background_color)

    title = tk.Label(page,
                     text='Osallistu tieteelliseen tutkimukseen',
                     bg=config.background_color,
                     fg=config.text_color,
                     font=config.big_font)
    title.pack(side=tk.TOP)

    content_text = ("Ansaitse rahaa pyörittämällä kampea." +
                    "Näet hankkimasi rahat ruudulla. Yliopiston tutkija maksaa ansaitsemasi summan " +
                    "välittömästi kun olet lopettanut pyörittämisen.")

    content = tk.Label(page,
                       text=content_text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=400,
                       justify='center')
    content.pack(side=tk.TOP)

    next_page_button = tk.Button(page,
                                 text="Haluan osallistua tutkimukseen",
                                 command=activate_next_page)
    next_page_button.pack()

    return page
