import tkinter as tk
import config
import page

button_texts = [u'\u2460', u'\u2461', u'\u2462', u'\u2463', u'\u2464']


def on_select(event, button, selection_value, question_type, questions_data, activate_selection, select_buttons):
    activate_selection(event, select_buttons)

    has_unselected = False
    for question in questions_data:
        if question['type'] is question_type:
            question['value'] = selection_value
            question['selected'] = True
        else:
            if 'selected' not in question:
                has_unselected = True

    if not has_unselected:
        button.config(state=tk.NORMAL)


def generate_question(frame, button, questions_data, question):
    iframe1 = tk.Frame(frame)
    page.generate_title(frame, question['title'])

    select_buttons = []

    for selection_value in range(1, 6):
        def make_lambda(button, selection_value, question_type, questions_data, activate_selection, select_buttons):
            # http://stackoverflow.com/a/14260871/7010222
            return lambda event: on_select(
                    event,
                    button,
                    selection_value,
                    question_type,
                    questions_data,
                    activate_selection,
                    select_buttons)

        button_text = button_texts[selection_value - 1]

        select_button = tk.Label(iframe1, text=button_text, font=config.jumbo_font, padx=10)
        select_button.bind(
                '<Button-1>',
                make_lambda(
                    button,
                    selection_value,
                    question['type'],
                    questions_data,
                    activate_selection,
                    select_buttons,
                    ))
        select_button.pack(side=tk.LEFT)
        select_buttons.append(select_button)

    iframe1.pack(padx=config.body_padding)


def on_done(append_data, questions_data, earnings, activate_next_page):
    sorted_questions_data = sorted(questions_data, key=lambda k: k['id'])
    values = [question['value'] for question in sorted_questions_data]
    append_data(*values)
    activate_next_page(earnings)


def generate_page(root, activate_next_page, earnings, append_data):
    questions_data = [{
        'type': 'feeling',
        'title': 'Mikä on olosi tällä hetkellä?',
        'id': 1
        },
        {
        'type': 'vitality',
        'title': 'Kuinka energinen on olosi tällä hetkellä?',
        'id': 2
        },
        {
        'type': 'meaningness',
        'title': 'Kuinka merkitykselliseltä kahvan pyörittäminen tuntui?',
        'id': 3
        }]

    frame = page.generate_frame(root)

    button = page.generate_button(
            frame,
            'Valmis',
            lambda: on_done(append_data, questions_data, earnings, activate_next_page),
            True)
    button.config(state=tk.DISABLED)

    for question in questions_data:
        generate_question(frame, button, questions_data, question)

    page.pack_button(button)

    return frame


def activate_selection(event, select_buttons):
    for widget in select_buttons:
        widget.configure(fg=config.inactive_button_color)
    event.widget.configure(fg=config.active_button_color)
