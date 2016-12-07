import page


def generate_page(root, width):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Kiitos osallistumisestasi!')

    content_text = 'Tutkija maksaa nyt sinulle keräämäsi rahasumman:'

    page.generate_content(frame, width, content_text)

    return frame
