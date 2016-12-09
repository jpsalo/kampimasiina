import time
import tkinter as tk
import page

import config
import crank


def generate_page(root, width, activate_next_page, experiment_type):
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

    return frame


def update_text(text):
    earnings_counter.configure(text=text)
    earnings_counter.pack()


def refresh_progress(result, time_elapsed, progress_data):
    time_elapsed = int(time.time() - progress_data['time_since_last_progress'])
    time_elapsed = min(int(config.progress_indicator_time_limit / 1000), time_elapsed)
    time_remaining = int(config.progress_indicator_time_limit / 1000 - time_elapsed)

    if progress_data['progress_in_progress']:
        if time_remaining:
            progress_data['time_elapsed'] = (progress_data['total_time'] + time.time() -
                                             progress_data['initialized_time'])
        else:
            progress_data['progress_in_progress'] = False
            progress_data['total_time'] += time.time() - progress_data['initialized_time']

    if result:
        progress_data['time_since_last_progress'] = time.time()
        progress.configure(text='●●●●●●●')
        if not progress_data['progress_in_progress']:
            progress_data['progress_in_progress'] = True
            progress_data['initialized_time'] = time.time()
    else:
        progress.configure(text='●' * time_remaining + '○' * time_elapsed)

    return progress_data


def update_earnings(time_elapsed):
    update_text(str(int(time_elapsed / 4) / 100) + ' €')


def do_refresh_page(root, activate_next_frame, experiment_initialized_time, progress_data):
    time_elapsed = time.time() - experiment_initialized_time

    if (time_elapsed < config.test_time_limit):
        result = crank.read_serial()
        refresh_progress(result, time_elapsed, progress_data)
        update_earnings(progress_data['time_elapsed'])
        root.experiment_refresher = root.after(100,
                                               do_refresh_page,
                                               root,
                                               activate_next_frame,
                                               experiment_initialized_time,
                                               progress_data)
    else:
        root.after_cancel(root.experiment_refresher)
        activate_next_frame()


def refresh_page(root, activate_next_frame, experiment_initialized_time):
    progress_data = {
            'time_since_last_progress': time.time(),
            'time_elapsed': 0,
            'total_time': 0,
            'progress_in_progress': True,
            'initialized_time': time.time()
            }

    do_refresh_page(root, activate_next_frame, experiment_initialized_time, progress_data)
