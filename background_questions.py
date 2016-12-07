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


def generate_radio_button(frame, gender_variable, text, value, age_variable, button):
    radio_button = tk.Radiobutton(frame,
                                  text=text,
                                  font=config.large_font,
                                  variable=gender_variable,
                                  value=value,
                                  command=lambda: on_select(age_variable, button))
    radio_button.pack(side=tk.RIGHT, anchor=tk.W)


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

    iframe1 = tk.Frame(frame)

    tk.Label(iframe1, text='Sukupuoli', font=config.large_font).pack(side=tk.LEFT, padx=5)

    generate_radio_button(iframe1, gender_variable, 'Muu / En halua sanoa', 3, age_variable, button)
    generate_radio_button(iframe1, gender_variable, 'Mies', 2, age_variable, button)
    generate_radio_button(iframe1, gender_variable, 'Nainen', 1, age_variable, button)

    iframe1.pack(expand=1, fill=tk.X, padx=config.body_padding)

    iframe2 = tk.Frame(frame)

    tk.Label(iframe2, text='Ikäsi', font=config.large_font).pack(side=tk.LEFT, padx=5)

    ages = list(range(18, 100))
    drop = tk.OptionMenu(iframe2, age_variable, *ages, command=lambda x: on_select(gender_variable, button))
    drop.pack()

    iframe2.pack(expand=1, fill=tk.X, padx=config.body_padding)

    page.pack_button(button)

    return frame
