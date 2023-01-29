from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # : type hints for function parameters
        self.is_busy = False

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas_trivia = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.label_trivia = self.canvas_trivia.create_text(
            150,
            125,
            width="280",
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas_trivia.grid(row=1, column=0, columnspan=2, pady=50)

        button_true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=button_true_img, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        button_false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=button_false_img, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_trivia.config(bg="white")
        if self.quiz.still_has_questions():
            self.is_busy = False
            self.score_label.config(text=f"Score: {self.quiz.score} / {len(self.quiz.question_list)}")
            question_text = self.quiz.next_question()
            self.canvas_trivia.itemconfig(self.label_trivia, text=question_text)
        else:
            self.score_label.config(font=("Arial", 16, "bold"))
            self.canvas_trivia.itemconfig(self.label_trivia, text="You've reached the end of the quiz.")

    def true_pressed(self):
        if not self.is_busy:
            self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        if not self.is_busy:
            self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.is_busy = True
        if is_right:
            self.canvas_trivia.config(bg="green")
        else:
            self.canvas_trivia.config(bg="red")
        self.window.after(1000, self.get_next_question)
