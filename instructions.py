import tkinter as tk

import config


def generate_page(root, window_w, window_h, activate_next_page, experiment_type):
    page = tk.Frame(root, width=window_w, height=window_h)
    page.configure(background=config.background_color)
    page.pack(padx=20, pady=40)

    if experiment_type == 'negative':
        text = 'Negative'
    elif experiment_type == 'neutral':
        text = 'Neutral'
    elif experiment_type == 'positive':
        text = 'Positive'

    page_teksti = tk.Label(page,
                           text=text,
                           bg=config.background_color,
                           fg=config.text_color,
                           font=config.big_font)

    page_teksti.pack(side=tk.TOP)
    page_leipateksti = ("Ansaitse rahaa pyörittämällä kampea." +
                        "Näet hankkimasi rahat ruudulla. Yliopiston tutkija maksaa ansaitsemasi summan " +
                        "välittömästi kun olet lopettanut pyörittämisen.")
    page_leipa = tk.Label(page,
                          text=page_leipateksti,
                          bg=config.background_color,
                          fg=config.text_color,
                          font=config.small_font,
                          wraplength=400,
                          justify='center')
    page_leipa.pack(side=tk.TOP)

    page_next_page_button = tk.Button(page,
                                      text="Haluan osallistua tutkimukseen",
                                      command=lambda: activate_next_page(experiment_type))
    page_next_page_button.pack()
    return page
