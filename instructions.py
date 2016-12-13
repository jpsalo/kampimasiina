import page


def get_experiment_text(experiment_type):
    if experiment_type == 'neutral':
        text = ('Kun pyörität kahvaa, sinulle kertyy rahaa.\n'
                'Saat 1 sentin joka 4. sekunti.\n'
                'Tuntipalkkasi on siis 9 € / tunti.\n'
                'Kun olet valmis, tutkija maksaa sinulle kertyneen rahasumman käteisellä.')
    else:
        text = ('Kun pyörität kahvaa, tapahtuu kaksi asiaa:\n\n'
                '1) SINULLE KERTYY RAHAA\n'
                'Saat 1 sentin joka 4. sekunti.\n'
                'Tuntipalkkasi on siis 9 € / tunti.\n'
                'Kun olet valmis, tutkija maksaa sinulle kertyneen rahasumman käteisellä.\n\n')
        if experiment_type == 'negative':
            text += (
                    '2) PUNAISELLE RISTILLE KERTYY VÄHEMMÄN RAHAA\n'
                    'Tutkija tekee kokeiden jälkeen lahjoituksen Punaiselle Ristille.\n'
                    'Mutta niin kauan kuin pyörität kahvaa, '
                    'Punainen risti saa 1 sentin vähemmän rahaa joka 16. sekunti.\n'
                    'Eli kahvan pyöritys vähentää Punaiselle Ristille tehtävää lahjoitusta.')
        elif experiment_type == 'positive':
            text += (
                    '2) PUNAISELLE RISTILLE KERTYY RAHAA\n'
                    'Punainen Risti saa 1 sentin joka 16. sekunti.\n'
                    'Kokeiden jälkeen tutkija maksaa kertyneen rahasumman Punaiselle Ristille.')

    return text


def generate_page(root, width, activate_next_frame, experiment_type):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Ohjeet')

    content_text = (
            'Tehtävänäsi on pyörittää kahvaa.\n\n'
            'Voit pyörittää kahvaa niin kauan kuin haluat (maksimissaan 15 minuuttia)\n.'
            'Pyörittämisnopeudella ei ole vaikutusta tulokseen, '
            'joten ei ole mitään hyötyä pyörittää kahvaa erityisen nopeasti.\n\n'
            'Voit lopettaa pyörittämisen koska vain itse haluat.\n\n')

    content_text += get_experiment_text(experiment_type)

    page.generate_content(frame, width, content_text)

    page.generate_button(frame, 'Aloita koe', lambda: activate_next_frame(experiment_type))

    return frame
