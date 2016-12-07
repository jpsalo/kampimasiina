import time
import tkinter as tk
import page

import config
import KampiLaskuri


timer_reset_time = time.time()
time_elapsed = time.time()-timer_reset_time


def generate_page(root, width, activate_next_page, experiment_type):
    global frame_initialized_time

    global progress
    global earnings_counter

    frame = page.generate_frame(root)

    page.generate_title(frame, 'Pyöritä kampea niin kauan kuin haluat')

    progress = tk.Label(frame,
                        text='●●●●●●●',
                        bg=config.background_color,
                        fg=config.text_color,
                        font=config.big_font)
    progress.pack(side=tk.TOP)

    content_text = ('HUOM: Pyöritysnopeudella ei ole väliä.'
                    'Nopea pyöritys ei [UNDERLINE] tuota enemmän rahaa.')

    page.generate_content(frame, width, content_text)

    earnings_counter = tk.Label(frame,
                                text='',
                                bg=config.background_color,
                                fg=config.text_color,
                                font=config.big_font)
    earnings_counter.pack(side=tk.TOP)

    if experiment_type == 'negative' or experiment_type == 'positive':
        if experiment_type == 'negative':
            text = 'Negative'
        elif experiment_type == 'positive':
            text = 'Positive'

        emotion_measure_counter = tk.Label(frame,
                                           text=text,
                                           bg=config.background_color,
                                           fg=config.text_color,
                                           font=config.big_font)

        emotion_measure_counter.pack(side=tk.TOP)

    page.generate_button(frame, 'Kun olet pyörittänyt tarpeeksi,\npaina tästä', activate_next_page)

    frame_initialized_time = time.time()
    return frame


def update_text(text):
    earnings_counter.configure(text=text)
    earnings_counter.pack()


def refresh_progress():
    progress.configure(text='●' *
                       int(config.progress_indicator_time_limit-time_elapsed) +
                       '○'*int(time_elapsed))


def refresh_page(root, activate_next_frame):
    global time_elapsed
    global timer_reset_time
    global earned

    now_time = time.time()
    earned = (now_time - frame_initialized_time) * config.euros_per_hour/3600
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
                                                    activate_next_frame)
    else:
        root.after_cancel(root.tokansivunPaivitysTehtava)
        activate_next_frame()
