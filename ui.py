from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, width=400, height=600)

        self.canvas = Canvas(width=300, height=230, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.right_img = PhotoImage(file="true.png")
        self.wrong_img = PhotoImage(file="false.png")

        # BUTTONS
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.got_right)
        self.right_button.grid(row=2, column=0, pady=30, padx=30)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.got_wrong)
        self.wrong_button.grid(row=2, column=1, pady=30, padx=30)

        # LABEL
        self.score_count = 0
        self.label = Label(text=f"Score: {self.score_count}", bg=THEME_COLOR, font=("arial", 15),
                           fg="white")
        self.label.grid(row=0, column=1, pady=10)
        self.question = Label(text="Question here", bg="White", fg="Black", font=("Arial", 20, "italic"))
        self.question.place(relx=0.5, rely=0.38, anchor="center")

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question.config(text=q_text, wraplength=280)
        else:
            self.question.config(text="END!", bg="white")
            self.canvas.config(bg="white")
            self.canvas.update()
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def got_right(self):
        if self.quiz.check_answer("true"):
            self.canvas.config(bg="green")
            self.question.config(text="CORRECT", bg="green")
            self.score_count += 1
            self.label.config(text=f"Score: {self.score_count}")
        else:
            self.canvas.config(bg="red")
            self.question.config(text="WRONG", bg="red")

        self.canvas.update()
        self.window.after(1000, self.reset_color())
        self.next_question()

    def got_wrong(self):
        if not self.quiz.check_answer("false"):
            self.canvas.config(bg="red")
            self.question.config(text="WRONG", bg="red")
            self.canvas.update()
        else:
            self.canvas.config(bg="green")
            self.question.config(text="CORRECT", bg="green")
            self.score_count += 1
            self.label.config(text=f"Score: {self.score_count}")

        self.canvas.update()
        self.window.after(1000, self.reset_color())
        self.next_question()

    def reset_color(self):
        self.canvas.config(bg="white")
        self.question.config(bg="white")