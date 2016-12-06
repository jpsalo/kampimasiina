import tkinter as tk

import config


def generate_page(root):
    page = tk.Frame(root)
    page.configure(background=config.background_color)

    title = tk.Label(page,
                     text='Kiitos osallistumisestasi!',
                     bg=config.background_color,
                     fg=config.text_color,
                     font=config.big_font)
    title.pack(side=tk.TOP)

    content_text = 'Tutkija maksaa nyt sinulle keräämäsi rahasumman:'

    content = tk.Label(page,
                       text=content_text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=400,
                       justify='center')
    content.pack(side=tk.TOP)

    return page
