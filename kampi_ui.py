import tkinter as tk
from tkinter import TOP

# Globals
background_color = 'purple3'
text_color = 'white'
big_font = ("Helvetica", 40)
small_font = ("Helvetica", 20)


def activate_initial_page():
    initial_page.pack(padx=20, pady=40)


def activate_background_questions_page():
    # Hide the rest and show the second page
    initial_page.pack_forget()
    background_questions_page.pack(padx=20, pady=40)


# Create main window
root = tk.Tk()


# Full screen
window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (window_w, window_h))
root.configure(background=background_color)


# Create pages

# Initial page
initial_page = tk.Frame(root, width=window_w, height=window_h)
initial_page.configure(background=background_color)
initial_page.pack(padx=20, pady=40)
initial_page_teksti = tk.Label(initial_page, text='Pyöritä ja Ansaitse',
                               bg=background_color, fg=text_color, font=big_font)
initial_page_teksti.pack(side=TOP)
initial_page_leipateksti = ("Ansaitse rahaa pyörittämällä kampea." +
                            "Näet hankkimasi rahat ruudulla. Yliopiston tutkija maksaa ansaitsemasi summan " +
                            "välittömästi kun olet lopettanut pyörittämisen.")
initial_page_leipa = tk.Label(initial_page, text=initial_page_leipateksti,
                              bg=background_color, fg=text_color, font=small_font, wraplength=400, justify='center')
initial_page_leipa.pack(side=TOP)


initial_page_next_page_button = tk.Button(initial_page, text="Haluan osallistua tutkimukseen",
                                          command=activate_background_questions_page)
initial_page_next_page_button.pack()


# Background questions page
background_questions_page = tk.Frame(root, width=window_w, height=window_h)
background_questions_page.configure(background=background_color)
background_questions_page.pack(padx=20, pady=400)
background_questions_page_teksti_progress = tk.Label(background_questions_page,
                                                     text='●●●●●●●', bg=background_color, fg=text_color, font=big_font)
background_questions_page_teksti_progress.pack(side=TOP)
background_questions_page_teksti1 = tk.Label(background_questions_page, text='title', bg=background_color,
                                             fg=text_color,
                                             font=big_font)
background_questions_page_teksti1.pack(side=TOP)
background_questions_page_teksti2 = tk.Label(background_questions_page, text="", bg=background_color, fg=text_color,
                                             font=big_font)
background_questions_page_teksti2.pack(side=TOP)
background_questions_page_teksti3 = tk.Label(background_questions_page, text='title', bg=background_color,
                                             fg=text_color,
                                             font=big_font)
background_questions_page_teksti3.pack(side=TOP)
background_questions_page_teksti4 = tk.Label(background_questions_page, text="", bg=background_color, fg=text_color,
                                             font=big_font)
background_questions_page_teksti4.pack(side=TOP)


activate_initial_page()

# Start tkinter event - loop
root.mainloop()
