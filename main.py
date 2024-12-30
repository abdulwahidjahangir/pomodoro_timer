from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
COLOR_PINK = "#e2979c"
COLOR_RED = "#e7305b"
COLOR_GREEN = "#9bdeac"
COLOR_YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_DURATION_MINUTES = 25
SHORT_BREAK_DURATION_MINUTES = 5
LONG_BREAK_DURATION_MINUTES = 20
cycle_count = 0
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global cycle_count
    cycle_count = 0
    checkmark_label.config(text="")
    title_label.config(text="Timer", fg=COLOR_GREEN)
    canvas.itemconfig(timer_display, text="00:00")
    window.after_cancel(timer_id)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global cycle_count
    cycle_count += 1

    work_seconds = WORK_DURATION_MINUTES * 60
    short_break_seconds = SHORT_BREAK_DURATION_MINUTES * 60
    long_break_seconds = LONG_BREAK_DURATION_MINUTES * 60

    if cycle_count % 8 == 0:
        start_countdown(long_break_seconds)
        title_label.config(text="Break", fg=COLOR_RED)
    elif cycle_count % 2 == 0:
        start_countdown(short_break_seconds)
        title_label.config(text="Break", fg=COLOR_PINK)
    else:
        start_countdown(work_seconds)
        title_label.config(text="Work", fg=COLOR_GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(seconds_remaining):
    minutes = seconds_remaining // 60
    seconds = seconds_remaining % 60
    if seconds <= 9:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_display, text=f"{minutes}:{seconds}")
    if seconds_remaining > 0:
        global timer_id
        timer_id = window.after(1000, start_countdown, seconds_remaining - 1)
    else:
        start_pomodoro()
        completed_sessions = cycle_count // 2
        checkmarks = ["✅" for _ in range(completed_sessions)] or ""
        checkmark_label.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=COLOR_YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=COLOR_GREEN, bg=COLOR_YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=COLOR_YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_display = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 18, "bold"), command=start_pomodoro)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 18, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=(FONT_NAME, 12, "bold"), fg=COLOR_GREEN, bg=COLOR_YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
