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


def generate_content(frame, width, text):
    content = tk.Label(frame,
                       text=text,
                       bg=config.background_color,
                       fg=config.text_color,
                       font=config.small_font,
                       wraplength=width-200)
    content.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def generate_button(frame, text, command):
    button = tk.Button(frame,
                       text=text,
                       font=config.button_font,
                       command=command)
    button.pack(side=tk.TOP, fill=tk.Y, expand=1)
