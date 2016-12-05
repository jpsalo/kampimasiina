import tkinter as tk

import config
import initial_page
import background_questions_page

pages = []


def forget_other_pages(current_page):
    for page in pages:
        if current_page != page:
            page.pack_forget()


def activate_initial_page():
    initial_page_data = initial_page.generate_initial_page(root, window_w,
                                                           window_h,
                                                           activate_background_questions_page)
    initial_page_data.pack(padx=20, pady=40)
    pages.append(initial_page_data)


def activate_background_questions_page():
    # Hide the rest and show the second page
    background_questions_page_data = background_questions_page.generate_background_questions_page(root,
                                                                                                  window_w,
                                                                                                  window_h)
    forget_other_pages(background_questions_page_data)
    background_questions_page_data.pack(padx=20, pady=40)


# Create main window
root = tk.Tk()


# Full screen
window_w = root.winfo_screenwidth()
window_h = root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (window_w, window_h))
root.configure(background=config.background_color)


# Create pages

activate_initial_page()

# Start tkinter event - loop
root.mainloop()
