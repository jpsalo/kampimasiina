import csv
import tkinter as tk
from random import randint
import time

import config
import landing
import background_questions
import instructions
import experiment
import questionnaire
import thank_you

pages = []
output = []


def append_data(*args):
    global output
    output += list(args)


def save_output():
    output_csv = open('output.csv', 'a')
    csv_writer = csv.writer(output_csv)
    csv_writer.writerow(output)


def get_experiment_type():
    random_experiment = randint(-1, 1)
    if random_experiment == -1:
        return 'negative'
    elif random_experiment == 0:
        return 'neutral'
    else:
        return 'positive'


def forget_other_pages(current_page):
    for page in pages:
        if current_page != page:
            page.pack_forget()


def activate_page(page):
    forget_other_pages(page)
    page.pack(fill=tk.BOTH, expand=tk.YES)
    pages.append(page)


def activate_landing():
    landing_data = landing.generate_page(root, window_w, activate_background_questions)
    activate_page(landing_data)


def activate_background_questions():
    background_questions_data = background_questions.generate_page(root,
                                                                   window_w,
                                                                   activate_instructions,
                                                                   append_data)
    activate_page(background_questions_data)


def activate_instructions():
    experiment_type = get_experiment_type()
    instructions_data = instructions.generate_page(root, window_w, activate_experiment, experiment_type)
    activate_page(instructions_data)


def activate_experiment(experiment_type):
    experiment_data = experiment.generate_page(root, window_w, activate_questionnaire, experiment_type, append_data)
    activate_page(experiment_data['frame'])
    experiment_initialized = time.time()
    experiment.refresh_page(
            root,
            activate_questionnaire,
            experiment_initialized,
            experiment_type,
            experiment_data['data'],
            append_data)


def activate_questionnaire(earnings):
    questionnaire_data = questionnaire.generate_page(root, activate_thank_you, earnings, append_data)
    activate_page(questionnaire_data)


def activate_thank_you(earnings):
    thank_you_data = thank_you.generate_page(root, window_w, earnings)
    activate_page(thank_you_data)
    save_output()


# Create main window
root = tk.Tk()

# Full screen
window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()
root.attributes("-fullscreen", True)

root.configure(background=config.background_color)

activate_landing()

# Start tkinter event - loop
root.mainloop()
