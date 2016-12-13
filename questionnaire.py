import tkinter as tk
import config
import page


def on_select(button, question_variable, question_type, questions_data):
    has_unselected = False
    for question in questions_data:
        if question['type'] is question_type:
            question['value'] = question_variable.get()
            question['selected'] = True
        else:
            if 'selected' not in question:
                has_unselected = True

    if not has_unselected:
        button.config(state=tk.NORMAL)


def generate_question(frame, button, questions_data, question):
    iframe1 = tk.Frame(frame)
    page.generate_title(frame, question['title'])

    question_variable = tk.IntVar()
    for selection_value in range(1, 6):
        radio_button = page.generate_radio_button(
                iframe1,
                question_variable,
                selection_value,
                selection_value,
                lambda: on_select(button, question_variable, question['type'], questions_data), True)
        radio_button.config(indicatoron=0)
        radio_button.pack(side=tk.LEFT)

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
