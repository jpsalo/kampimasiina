import tkinter as tk
import config
import page


def on_select(condition_variable, button):
    condition = condition_variable.get()
    if condition != 0:
        button.config(state=tk.NORMAL)
    return


def on_done(activate_next_page, append_data, gender_variable, age_variable):
    append_data(gender_variable.get(), age_variable.get())
    activate_next_page()


def generate_page(root, width, activate_next_page, append_data):
    gender_variable = tk.IntVar()
    age_variable = tk.IntVar()

    frame = page.generate_frame(root)

    page.generate_title(frame, 'Taustakysymykset')

    content_text = 'Ennen kokeen alkamista tarvitsemme muutaman tiedon taustastasi:'
    page.generate_content(frame, width, content_text)

    button = page.generate_button(frame,
                                  'Jatka',
                                  lambda: on_done(activate_next_page, append_data, gender_variable, age_variable),
                                  True)
    button.config(state=tk.DISABLED)

    iframe1 = page.generate_frame(frame)

    gender_label = page.generate_label(iframe1, 'Sukupuoli', config.large_font)
    gender_label.pack(side=tk.LEFT, padx=5)

    page.generate_radio_button(
            iframe1,
            gender_variable,
            'Muu / En halua sanoa',
            3,
            lambda: on_select(age_variable, button),
            font=config.large_font)
    page.generate_radio_button(
            iframe1,
            gender_variable,
            'Mies',
            2,
            lambda: on_select(age_variable, button),
            font=config.large_font)
    page.generate_radio_button(
            iframe1,
            gender_variable,
            'Nainen',
            1,
            lambda: on_select(age_variable, button),
            font=config.large_font)

    iframe1.pack(expand=1, fill=tk.X, padx=config.body_padding)

    iframe2 = page.generate_frame(frame)

    age_label = page.generate_label(iframe2, 'Ikäsi', config.large_font)
    age_label.pack(side=tk.LEFT, padx=5)

    ages = list(range(18, 100))
    drop = tk.OptionMenu(iframe2, age_variable, *ages, command=lambda x: on_select(gender_variable, button))
    drop.pack()

    iframe2.pack(expand=1, fill=tk.X, padx=config.body_padding)

    page.pack_button(button)

    return frame
