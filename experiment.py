import time
import tkinter as tk

import config
import KampiLaskuri


timer_reset_time = time.time()
time_elapsed = time.time()-timer_reset_time


def generate_page(root, window_w, window_h, experiment_type):
    global page_initialized_time

    global page_teksti_progress
    global page_teksti2

    page = tk.Frame(root, width=window_w, height=window_h)
    page.configure(background=config.background_color)
    page.pack(padx=20, pady=400)
    page_teksti_progress = tk.Label(page,
                                    text='●●●●●●●',
                                    bg=config.background_color,
                                    fg=config.text_color,
                                    font=config.big_font)
    page_teksti_progress.pack(side=tk.TOP)

    if experiment_type == 'negative':
        text = 'Negative'
    elif experiment_type == 'neutral':
        text = 'Neutral'
    elif experiment_type == 'positive':
        text = 'Positive'

    page_teksti1 = tk.Label(page,
                            text=text,
                            bg=config.background_color,
                            fg=config.text_color,
                            font=config.big_font)

    page_teksti1.pack(side=tk.TOP)
    page_teksti2 = tk.Label(page,
                            text="",
                            bg=config.background_color,
                            fg=config.text_color,
                            font=config.big_font)
    page_teksti2.pack(side=tk.TOP)
    page_teksti3 = tk.Label(page,
                            text='title',
                            bg=config.background_color,
                            fg=config.text_color,
                            font=config.big_font)
    page_teksti3.pack(side=tk.TOP)
    page_teksti4 = tk.Label(page,
                            text="",
                            bg=config.background_color,
                            fg=config.text_color,
                            font=config.big_font)
    page_teksti4.pack(side=tk.TOP)

    page_initialized_time = time.time()
    return page


def update_text(text):
    page_teksti2.configure(text=text)
    page_teksti2.pack()


def refresh_progress():
    page_teksti_progress.configure(text='●' *
                                   int(config.progress_indicator_time_limit-time_elapsed) +
                                   '○'*int(time_elapsed))


def refresh_page(root, activate_next_page):
    global time_elapsed
    global timer_reset_time
    global earned

    now_time = time.time()
    earned = (now_time - page_initialized_time) * config.euros_per_hour/3600
    earned_teksti = '{0:.2f}'.format(earned) + ' €'
    update_text(earned_teksti)

    if (time_elapsed < config.test_time_limit):
        result = KampiLaskuri.read_serial()
        if not result:
            time_elapsed = time.time()-timer_reset_time
            refresh_progress()
        else:
            timer_reset_time = time.time()
        root.tokansivunPaivitysTehtava = root.after(100, refresh_page,
                                                    root,
                                                    activate_next_page)
    else:
        root.after_cancel(root.tokansivunPaivitysTehtava)
        activate_next_page()
