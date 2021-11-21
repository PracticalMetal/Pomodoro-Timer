from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
MARKS = ""

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    global MARKS
    REPS += 1
    if REPS % 2 != 0:
        timer.config(text="Working", fg=RED)
        count_down(WORK_MIN*60)
        # checkmark.config(text=MARKS+"✔")
        # MARKS+="✔"
    elif REPS % 2 == 0 and REPS % 8 != 0:
        timer.config(text="Break", fg=GREEN)
        count_down(SHORT_BREAK_MIN*60)
    else:
        timer.config(text="Break", fg=GREEN)
        count_down(LONG_BREAK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global MARKS
    start.config(state="disabled")
    min = str(count//60)
    sec = str(count % 60)
    if len(min) == 1:
        min = '0'+min
    if len(sec) == 1:
        sec = '0'+sec

    canvas.itemconfig(pomo_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, count_down, count-1)

    else:
        start.config(state="normal")

        if (REPS+1) % 2 != 0:
            timer.config(text="Working", fg=RED)

        elif (REPS+1) % 2 == 0 and (REPS+1) % 8 != 0:
            timer.config(text="Break", fg=GREEN)

        else:
            timer.config(text="Break", fg=GREEN)
    if count <= 0 and REPS % 2 != 0:
        checkmark.config(text=MARKS+"✔")
        MARKS += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
pomo_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# creating a label
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.config(pady=20)
timer.grid(row=0, column=1)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(20))
checkmark.grid(row=3, column=1)

# creating buttons
start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset")
reset.grid(row=2, column=2)


window.mainloop()
