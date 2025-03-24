import tkinter as tk
from tkinter import messagebox
import random

# Data for cultural stories
cultural_stories = {
    "Taj Mahal": "The Taj Mahal, built by Emperor Shah Jahan in memory of his wife Mumtaz Mahal, is one of the Seven Wonders of the World. It symbolizes love and is made of white marble.",
    "Diwali": "Diwali, also known as the Festival of Lights, celebrates the return of Lord Rama to Ayodhya after 14 years of exile. People light lamps and burst crackers to celebrate this joyous occasion.",
    "Kathak": "Kathak is one of the eight classical dance forms of India. Originating from North India, it narrates stories through intricate footwork, hand gestures, and facial expressions."
}

# Data for the heritage quiz
quiz_questions = [
    {
        "question": "Where is the Sun Temple located?",
        "options": ["Konark", "Puri", "Jaipur", "Kolkata"],
        "answer": "Konark"
    },
    {
        "question": "Which dance form originates from Kerala?",
        "options": ["Kathakali", "Bharatanatyam", "Odissi", "Garba"],
        "answer": "Kathakali"
    },
    {
        "question": "Which monument is called the 'Symbol of Love'?",
        "options": ["Taj Mahal", "Qutub Minar", "Hawa Mahal", "Charminar"],
        "answer": "Taj Mahal"
    }
]

# App class
class RevivingTheRoots:
    def __init__(self, root):
        self.root = root
        self.root.title("Reviving The Roots: Learn and Quiz")
        self.root.geometry("600x400")

        # Main menu frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        self.title_label = tk.Label(self.main_frame, text="Heritage Explorer", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=20)

        # Story button
        self.story_button = tk.Button(self.main_frame, text="Cultural Stories", font=("Arial", 14), command=self.show_stories)
        self.story_button.pack(pady=10)

        # Quiz button
        self.quiz_button = tk.Button(self.main_frame, text="Heritage Quiz", font=("Arial", 14), command=self.start_quiz)
        self.quiz_button.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(self.main_frame, text="Exit", font=("Arial", 14), command=root.quit)
        self.exit_button.pack(pady=10)

        # Quiz data
        self.quiz_index = 0
        self.score = 0

    def show_stories(self):
        """Display cultural stories."""
        self.clear_frame()

        tk.Label(self.main_frame, text="Cultural Stories", font=("Arial", 18, "bold")).pack(pady=10)
        for title, story in cultural_stories.items():
            tk.Label(self.main_frame, text=f"{title}:", font=("Arial", 14, "bold"), anchor="w").pack(fill=tk.X, pady=5)
            tk.Label(self.main_frame, text=story, font=("Arial", 12), wraplength=500, justify="left").pack(fill=tk.X, padx=20, pady=5)

        tk.Button(self.main_frame, text="Back to Menu", font=("Arial", 14), command=self.return_to_menu).pack(pady=20)

    def start_quiz(self):
        """Start the heritage quiz."""
        self.quiz_index = 0
        self.score = 0
        self.load_quiz_question()

    def load_quiz_question(self):
        """Load the next quiz question."""
        if self.quiz_index >= len(quiz_questions):
            self.show_quiz_result()
            return

        self.clear_frame()
        question_data = quiz_questions[self.quiz_index]

        # Display question
        tk.Label(self.main_frame, text=f"Question {self.quiz_index + 1}:", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.main_frame, text=question_data["question"], font=("Arial", 14), wraplength=500).pack(pady=10)

        # Display options
        for option in question_data["options"]:
            tk.Button(self.main_frame, text=option, font=("Arial", 12), width=40,
                      command=lambda opt=option: self.check_answer(opt)).pack(pady=5)

    def check_answer(self, selected_option):
        """Check the selected answer and load the next question."""
        correct_answer = quiz_questions[self.quiz_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! That's the correct answer.")
        else:
            messagebox.showerror("Incorrect!", f"The correct answer was: {correct_answer}.")

        self.quiz_index += 1
        self.load_quiz_question()

    def show_quiz_result(self):
        """Display the final quiz result."""
        self.clear_frame()

        result_text = f"You scored {self.score} out of {len(quiz_questions)}!"
        tk.Label(self.main_frame, text="Quiz Complete!", font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(self.main_frame, text=result_text, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.main_frame, text="Back to Menu", font=("Arial", 14), command=self.return_to_menu).pack(pady=20)

    def return_to_menu(self):
        """Return to the main menu."""
        self.clear_frame()
        self.__init__(self.root)

    def clear_frame(self):
        """Clear all widgets in the current frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = RevivingTheRoots(root)
    root.mainloop()
