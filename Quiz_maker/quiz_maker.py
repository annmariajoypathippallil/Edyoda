import json
import random
from pyfiglet import Figlet
from prettytable import PrettyTable

class QuizWorld:
    def __init__(self):
        self.user_answer_dict = {}
        self.question_number = 5
        self.q_number = 1
        self.q_num = 1

    def print_box(self, text):
        line = '+' + '-' * (len(text) + 2) + '+'
        print(line)
        print('| ' + text + ' |')
        print(line)

    def load_questions(self):
        with open("questions.json") as file:
            data = json.load(file)
        self.questions = dict(data)

    def generate_quiz(self):
        shuffled_keys = list(self.questions.keys())
        random.shuffle(shuffled_keys)
        self.shuffled_question = {}

        for i in shuffled_keys:
            self.shuffled_question[i] = self.questions[i]
            if self.q_num == self.question_number:
                break
            self.q_num += 1

    def display_quiz(self):
        for quiz in self.shuffled_question.values():
            opt_number = 97
            print(self.q_number, ". ", quiz[1])
            answer_options = quiz[2]
            random.shuffle(answer_options)
            for option in answer_options:
                print("\t", chr(opt_number), ") ", option)
                opt_number += 1

            selected_answer = input("Select an option ")
            self.print_box(selected_answer)
            if selected_answer not in ['a', 'b', 'c', 'd']:
                print("Invalid option")
                self.q_number += 1
                continue
            else:
                self.user_answer_dict[quiz[0]] = quiz[2][ord(selected_answer) - 97]
                self.q_number += 1

    def load_answer_key(self):
        with open("key.json") as file:
            data = json.load(file)
        self.answer_dict = dict(data)

    def calculate_score(self):
        total_marks = 0
        for i in self.user_answer_dict.keys():
            if self.user_answer_dict[i] == self.answer_dict[str(i)]:
                total_marks += 1
        return total_marks

    def run_quiz(self):
        f = Figlet(font='slant', width=150)
        t = PrettyTable()
        banner_text = f.renderText("WELCOME TO QUIZ WORLD")
        print(banner_text)

        self.load_questions()
        self.generate_quiz()
        self.display_quiz()
        self.load_answer_key()
        total_marks = self.calculate_score()

        t.field_names = ["Your detailed report", ""]
        t.add_row(["Total correct answers ", total_marks])
        t.add_row(["Total incorrect answers ", self.question_number - total_marks])
        t.add_row(["-----------------------", "-----"])
        t.add_row(["Total marks", str(total_marks) + '/' + str(self.question_number)])
        print(t)

        perc = (total_marks / self.question_number) * 100
        if perc >= 80:
            print("\033[1mCongratulations, you won.\033[0m")
        else:
            print("\033[1mSorry, you lost!\033[0m")
quiz = QuizWorld()
quiz.run_quiz()
