import time
import tkinter as tk
import page

import config
import crank


def calculate_counter_value(time_elapsed, interval_seconds, negative=False):
    counter_value = int(time_elapsed / interval_seconds) / 100
    if negative and counter_value != 0:
        counter_value *= -1
    return counter_value


def on_done(append_data, activate_next_page, experiment_type, progress_data):
    earnings = calculate_counter_value(progress_data['time_elapsed'], config.earnings_measure_interval_seconds)
    emotion_measure_counter = 0
    if experiment_type is 'negative' or experiment_type is 'positive':
        negative_measure = True if experiment_type is 'negative' else False
        emotion_measure_counter = calculate_counter_value(progress_data['time_elapsed'],
                                                          config.emotion_measure_interval_seconds,
                                                          negative_measure)
    append_data(experiment_type, earnings, emotion_measure_counter)
    activate_next_page()


def generate_page(root, width, activate_next_page, experiment_type, append_data):
    global progress
    global earnings_counter

    data = {}

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

    iframe2 = tk.Frame(frame)

    if experiment_type is 'neutral':
        earnings_counter = tk.Label(iframe2,
                                    bg=config.background_color,
                                    fg=config.text_color,
                                    font=config.big_font)
        earnings_counter.pack(side=tk.TOP)
        tk.Label(iframe2, text='Sinulle kertyvät rahat').pack()
    else:
        iframe3 = tk.Frame(iframe2)
        earnings_counter = tk.Label(iframe3,
                                    bg=config.background_color,
                                    fg=config.text_color,
                                    font=config.big_font)
        earnings_counter.configure()
        earnings_counter.pack()
        tk.Label(iframe3, text='Sinulle kertyvät rahat').pack()
        iframe3.pack(side=tk.LEFT)

        iframe4 = tk.Frame(iframe2)
        global emotion_measure_counter
        emotion_measure_counter = tk.Label(iframe4,
                                           bg=config.background_color,
                                           fg=config.text_color,
                                           font=config.big_font)

        emotion_measure_counter.pack()
        tk.Label(iframe4, text='Hyväntekeväisyyteen lahjoitettavat rahat').pack()
        iframe4.pack(side=tk.RIGHT)

    iframe2.pack(expand=1, fill=tk.X, padx=config.body_padding)

    page.generate_button(frame,
                         'Kun olet pyörittänyt tarpeeksi,\npaina tästä',
                         lambda: on_done(append_data, activate_next_page, experiment_type, data))

    return {'frame': frame, 'data': data}


def update_earnings_text(text):
    earnings_counter.configure(text=text)


def update_emotion_measure_counter_text(text):
    emotion_measure_counter.configure(text=text)


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


def counter_formatter(time_elapsed, interval_seconds, negative=False):
    counter_value = calculate_counter_value(time_elapsed, interval_seconds, negative)
    counter_value = format(counter_value, '.2f').replace('.', ',') + ' €'
    return counter_value


def update_earnings(time_elapsed):
    earnings = counter_formatter(time_elapsed, config.earnings_measure_interval_seconds)
    update_earnings_text(earnings)


def update_emotion_measure_counter(time_elapsed, experiment_type):
    if experiment_type is 'negative' or experiment_type is 'positive':
        negative_measure = True if experiment_type is 'negative' else False
        emotion_measure_counter = counter_formatter(time_elapsed,
                                                    config.emotion_measure_interval_seconds,
                                                    negative_measure)
        update_emotion_measure_counter_text(emotion_measure_counter)


def do_refresh_page(root, activate_next_frame, experiment_initialized_time, progress_data, experiment_type):
    time_elapsed = time.time() - experiment_initialized_time

    if (time_elapsed < config.test_time_limit):
        result = crank.read_serial()
        refresh_progress(result, time_elapsed, progress_data)
        update_earnings(progress_data['time_elapsed'])
        update_emotion_measure_counter(progress_data['time_elapsed'], experiment_type)
        root.experiment_refresher = root.after(100,
                                               do_refresh_page,
                                               root,
                                               activate_next_frame,
                                               experiment_initialized_time,
                                               progress_data,
                                               experiment_type)
    else:
        root.after_cancel(root.experiment_refresher)
        activate_next_frame()


def refresh_page(root, activate_next_frame, experiment_initialized_time, experiment_type, progress_data):
    progress_data['time_since_last_progress'] = time.time()
    progress_data['time_elapsed'] = 0
    progress_data['total_time'] = 0
    progress_data['progress_in_progress'] = True
    progress_data['initialized_time'] = time.time()

    do_refresh_page(root, activate_next_frame, experiment_initialized_time, progress_data, experiment_type)
