import tkinter as tk
from random import randint

import config
import landing
import background_questions
import instructions
import experiment


def get_experiment_type():
    random_experiment = randint(-1, 1)
    if random_experiment == -1:
        return 'negative'
    elif random_experiment == 0:
        return 'neutral'
    else:
        return 'positive'


pages = []


def forget_other_pages(current_page):
    for page in pages:
        if current_page != page:
            page.pack_forget()


def activate_landing():
    landing_data = landing.generate_page(root,
                                         window_w,
                                         window_h,
                                         activate_background_questions)
    landing_data.pack(padx=20, pady=40)
    pages.append(landing_data)


def activate_background_questions():
    background_questions_data = background_questions.generate_page(root,
                                                                   window_w,
                                                                   window_h,
                                                                   activate_instructions)
    forget_other_pages(background_questions_data)
    background_questions_data.pack(padx=20, pady=40)
    pages.append(background_questions_data)


def activate_instructions():
    experiment_type = get_experiment_type()
    instructions_data = instructions.generate_page(root,
                                                   window_w,
                                                   window_h,
                                                   activate_experiment,
                                                   experiment_type)
    forget_other_pages(instructions_data)
    instructions_data.pack(padx=20, pady=40)
    pages.append(instructions_data)


def activate_experiment(experiment_type):
    # Hide the rest and show the second page
    experiment_data = experiment.generate_page(root,
                                               window_w,
                                               window_h,
                                               experiment_type)
    forget_other_pages(experiment_data)
    experiment_data.pack(padx=20, pady=40)
    experiment.refresh_page(root, activate_third_page)
    pages.append(experiment_data)


def activate_third_page():
    print('third')


# Create main window
root = tk.Tk()


# Full screen
window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (window_w, window_h))
root.configure(background=config.background_color)


activate_landing()

# Start tkinter event - loop
root.mainloop()
