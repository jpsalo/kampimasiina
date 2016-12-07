import page


def generate_page(root, activate_next_page):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Mikä on olosi tällä hetkellä?')

    page.generate_button(frame, 'Valmis', activate_next_page)

    return frame
