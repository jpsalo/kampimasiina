import page


def generate_page(root, width, activate_next_frame):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Osallistu tieteelliseen tutkimukseen')

    content_text = (
            'Tämä koe pyrkii selvittämään ihmisen motivaatiota ja hyvinvointia erilaisten työtehtävien aikana. '
            'Tehtävässä sinulle maksetaan pieni summa rahaa kahvan pyörittämisestä: 1 sentti joka 4. sekunti, '
            'joka tuntipalkaksi muutettuna tarkoittaa 9 € / tunti. Voit pyörittää kahvaa haluamasi ajan. '
            'Maksimissaan viisitoista minuuttia, mutta voit lopettaa koska vain aiemminkin. '
            'Lopetettuasi kahvan pyörittämisen, '
            'pyydämme sinua vastaamaan kolmeen kysymykseen koskien senhetkistä tuntemuksiasi. '
            'Sen jälkeen tutkija maksaa sinulle keräämäsi rahasumman.')

    content_text += '\n\n'

    content_text += (
            'Tutkimus on osa sisäisen motivaation osatekijöitä '
            'ja psykologisia perustarpeita kartoittavaa tutkimusprojektia. '
            'Vastaavana tutkijana toimii Frank Martela Helsingin yliopistolta.\n'
            'frank.martela@helsinki.fi\n'
            '050-5707916')

    content_text += '\n\n'

    content_text += (
            'Hyvä tietää ennen tutkimukseen osallistumista:\n\n'
            '- Tutkimukseen osallistuminen on vapaaehtoista.\n\n'
            '- Osallistujilla on oikeus kysyä lisätietoja tutkimuksesta '
            'ja keskeyttää osallistuminen tutkimukseen milloin tahansa seuraamuksitta ja syytä ilmoittamatta.\n\n'
            '- Vastauksia käsitellään ehdottoman luotettavasti: '
            'Emme kerää mitään sellaista tietoa osallistujista, joista heidät voisi tunnistaa.\n\n'
            '- Tutkimuksessa kerättyjä tietoja hyödynnetään tieteellisissä julkaisuissa.')

    page.generate_content(frame, width, content_text)

    page.generate_button(frame, 'Haluan osallistua\ntutkimukseen', activate_next_frame)

    return frame
