import tkinter as tk

import config


def generate_page(root, activate_next_page):
    page = tk.Frame(root)
    page.configure(background=config.background_color)

    question = tk.Label(page,
                        text='Mikä on olosi tällä hetkellä?',
                        bg=config.background_color,
                        fg=config.text_color,
                        font=config.big_font)
    question.pack(side=tk.TOP)

    next_page_button = tk.Button(page,
                                 text='Valmis',
                                 command=activate_next_page)
    next_page_button.pack()

    return page
