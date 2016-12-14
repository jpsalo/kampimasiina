import tkinter as tk

import config
import page
import utilities


def generate_page(root, width, earnings):
    frame = page.generate_frame(root)

    page.generate_title(frame, 'Kiitos osallistumisestasi!')

    content_text = 'Tutkija maksaa nyt sinulle keräämäsi rahasumman:'

    iframe1 = page.generate_frame(frame)

    content = page.generate_content(iframe1, width, content_text, True)
    content.pack(side=tk.TOP)

    earnings = tk.Label(
            iframe1,
            text=utilities.to_euros(earnings),
            bg=config.background_color,
            fg=config.text_color,
            font=config.big_font)
    earnings.pack(side=tk.TOP)

    iframe1.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    return frame
