import tkinter as tk

import config


def generate_background_questions_page(root, window_w, window_h):
    background_questions_page = tk.Frame(root, width=window_w, height=window_h)
    background_questions_page.configure(background=config.background_color)
    background_questions_page.pack(padx=20, pady=400)
    background_questions_page_teksti_progress = tk.Label(background_questions_page,
                                                         text='●●●●●●●',
                                                         bg=config.background_color,
                                                         fg=config.text_color, font=config.big_font)
    background_questions_page_teksti_progress.pack(side=tk.TOP)
    background_questions_page_teksti1 = tk.Label(background_questions_page,
                                                 text='title', bg=config.background_color,
                                                 fg=config.text_color,
                                                 font=config.big_font)
    background_questions_page_teksti1.pack(side=tk.TOP)
    background_questions_page_teksti2 = tk.Label(background_questions_page,
                                                 text="",
                                                 bg=config.background_color, fg=config.text_color,
                                                 font=config.big_font)
    background_questions_page_teksti2.pack(side=tk.TOP)
    background_questions_page_teksti3 = tk.Label(background_questions_page, text='title', bg=config.background_color,
                                                 fg=config.text_color,
                                                 font=config.big_font)
    background_questions_page_teksti3.pack(side=tk.TOP)
    background_questions_page_teksti4 = tk.Label(background_questions_page,
                                                 text="",
                                                 bg=config.background_color, fg=config.text_color,
                                                 font=config.big_font)
    background_questions_page_teksti4.pack(side=tk.TOP)

    return background_questions_page
