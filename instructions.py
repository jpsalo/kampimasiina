import tkinter as tk

import config


def get_experiment_text(experiment_type):
    if experiment_type == 'neutral':
        text = ('Kun pyörität kahvaa, sinulle kertyy rahaa [UNDERLINE].'
                'Saat 1 sentin joka 4. sekunti. Tuntipalkkasi on siis 9€ / tunti. '
                'Kun olet valmis, tutkija maksaa sinulle kertyneen rahasumman käteisellä.')
    else:
        text = ('Kun pyörität kahvaa, tapahtuu kaksi asiaa:\n'
                '1) Sinulle kertyy rahaa [UNDERLINE]. Saat 1 sentin joka 4. sekunti. '
                'Tuntipalkkasi on siis 9€ / tunti. '
                'Kun olet valmis, tutkija maksaa sinulle kertyneen rahasumman käteisellä.\n\n')
        if experiment_type == 'negative':
            text += ('2) Punaiselle Ristille kertyy vähemmän rahaa [UNDERLINE].'
                     'Tutkija tekee kokeiden jälkeen lahjoituksen Punaiselle Ristille. '
                     'Mutta niin kauan kuin pyörität kahvaa, '
                     'Punainen risti saa 1 sentin vähemmän rahaa joka 16. sekunti. '
                     'Eli kahvan pyöritys vähentää Punaiselle Ristille tehtävää lahjoitusta.')
        elif experiment_type == 'positive':
            text += ('2) Punaiselle Ristille kertyy rahaa [UNDERLINE].'
                     'Punainen Risti saa 1 sentin joka 16. sekunti. '
                     'Kokeiden jälkeen tutkija maksaa kertyneen rahasumman Punaiselle Ristille.')

    return text


def generate_page(root, activate_next_page, experiment_type):
    page = tk.Frame(root)
    page.configure(background=config.background_color)

    title = tk.Label(page,
                     text='Ohjeet',
                     bg=config.background_color,
                     fg=config.text_color,
                     font=config.big_font)

    title.pack(side=tk.TOP)

    content_text = ('Tehtävänäsi on pyörittää kahvaa.\n\n'
                    'Voit pyörittää kahvaa niin kauan kuin haluat (maksimissaan 15 minuuttia) '
                    'Pyörittämisnopeudella ei ole vaikutusta tulokseen, joten '
                    'ei ole mitään hyötyä pyörittää kahvaa erityisen nopeasti.\n\n'
                    'Voit lopettaa pyörittämisen koska vain itse haluat [UNDERLINE]\n\n')

    content_text += get_experiment_text(experiment_type)

    content = tk.Label(page,
                       text=content_text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=400,
                       justify='center')
    content.pack(side=tk.TOP)

    next_page_button = tk.Button(page,
                                 text='Aloita koe',
                                 command=lambda: activate_next_page(experiment_type))
    next_page_button.pack()

    return page
