import page


def generate_page(root, width, activate_next_page):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Taustakysymykset')

    content_text = 'Ennen kokeen alkamista tarvitsemme muutaman tiedon taustastasi:'
    page.generate_content(frame, width, content_text)

    page.generate_button(frame, 'Jatka', activate_next_page)

    return frame
