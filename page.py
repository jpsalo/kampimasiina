import tkinter as tk

import config


def generate_frame(root):
    frame = tk.Frame(root)
    frame.configure(background=config.background_color)
    return frame


def generate_title(frame, text):
    title = tk.Label(frame,
                     text=text,
                     bg=config.background_color,
                     fg=config.text_color,
                     font=config.big_font)
    title.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def generate_content(frame, width, text, skip_pack=False):
    content = tk.Label(frame,
                       text=text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=width-config.body_padding)
    if not skip_pack:
        content.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    return content


def generate_button(frame, text, command, skip_pack=False):
    button = tk.Button(frame,
                       text=text,
                       font=config.button_font,
                       command=command)
    if not skip_pack:
        pack_button(button)

    return button


def generate_radio_button(frame, variable, text, value, command, skip_pack=False, **keyword_parameters):
    radio_button = tk.Radiobutton(frame,
                                  text=text,
                                  variable=variable,
                                  value=value,
                                  command=command)
    if 'font' in keyword_parameters:
        radio_button.config(font=keyword_parameters['font'])
    if not skip_pack:
        pack_radio_button(radio_button)
    return radio_button


def pack_button(widget):
    widget.pack(side=tk.TOP, fill=tk.Y, expand=1)


def pack_radio_button(widget):
    widget.pack(side=tk.RIGHT, anchor=tk.W)
