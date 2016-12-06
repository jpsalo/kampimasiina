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

    content_text = ('Tämä koe pyrkii selvittämään ihmisen motivaatiota ja hyvinvointia erilaisten työtehtävien aikana. '
                    'Tehtävässä sinulle maksetaan pieni summa rahaa kahvan pyörittämisestä: 1 sentti joka 4. sekunti, '
                    'joka tuntipalkaksi muutettuna tarkoittaa 9€ / tunti. Voit pyörittää kahvaa haluamasi ajan. '
                    'Maksimissaan viisitoista minuuttia, mutta voit lopettaa koska vain aiemminkin. '
                    'Lopetettuasi kahvan pyörittämisen, '
                    'pyydämme sinua vastaamaan kolmeen kysymykseen koskien senhetkistä tuntemuksiasi. '
                    'Sen jälkeen tutkija maksaa sinulle keräämäsi rahasumman.')

    content_text += '\n\n'

    content_text += ('Tutkimus on osa sisäisen motivaation osatekijöitä '
                     'ja psykologisia perustarpeita kartoittavaa tutkimusprojektia. '
                     'Vastaavana tutkijana toimii Frank Martela Helsingin yliopistolta.\n'
                     'frank.martela@helsinki.fi [UNDERLINE]\n'
                     '050-5707916')

    content_text += '\n\n'

    content_text += ('Hyvä tietää ennen tutkimukseen osallistumista:\n\n'
                     '- Tutkimukseen osallistuminen on vapaaehtoista.\n\n'
                     '- Osallistujilla on oikeus kysyä lisätietoja tutkimuksesta '
                     'ja keskeyttää osallistuminen tutkimukseen milloin tahansa seuraamuksitta '
                     'ja syytä ilmoittamatta.\n\n'
                     '- Vastauksia käsitellään ehdottoman luotettavasti: '
                     'Emme kerää mitään sellaista tietoa osallistujista, joista heidät voisi tunnistaa.\n\n'
                     '- Tutkimuksessa kerättyjä tietoja hyödynnetään tieteellisissä julkaisuissa.')

    content = tk.Label(page,
                       text=content_text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=400,
                       justify='center')
    content.pack(side=tk.TOP)

    next_page_button = tk.Button(page,
                                 text='Haluan osallistua tutkimukseen',
                                 command=activate_next_page)
    next_page_button.pack()

    return page
