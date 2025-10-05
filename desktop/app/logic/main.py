from PySide6 import QtWidgets as qtw
from app.ui.main_window import Ui_w_MainWindow

import random


class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self, json_engine):
        super().__init__()

        self.json_engine = json_engine
 
        self.setupUi(self)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.le_user_guess.clear()
        self.le_user_guess.setFocus()
        self.le_user_guess.returnPressed.connect(self.check_answer)

        self.answer = None
        self.tries_remaining = 5
        
        self.pb_guess.clicked.connect(self.check_answer)
        self.pb_new_game.clicked.connect(self.start_new_game)

        self.actionHistory.triggered.connect(self.show_history)
        
        self.start_new_game()

    def show_history(self):
        from app.logic.history import HistoryWindow

        self.history_window = HistoryWindow(self.json_engine)
        self.history_window.pb_back.clicked.connect(self.show_main_window)

        self.hide()
        self.history_window.show()

    def show_main_window(self):
        if hasattr(self, 'history_window'):
            self.history_window.close()

        self.show()
        self.raise_()
        self.activateWindow()

    def start_new_game(self):
        self.answer = random.randint(1, 20)
        self.tries_remaining = 5

        self.lb_tries_remaining.setText(f"{self.lb_tries_remaining.text().split(" ")[0]} {self.tries_remaining}")
        self.statusbar.clearMessage()
        
        self.le_user_guess.clear()
        self.le_user_guess.setFocus()

    def check_answer(self):
        user_guess = int(self.le_user_guess.text())
        
        if user_guess < 1 or user_guess > 20:
            self.statusbar.showMessage(
                "Guess Must Be Between 1 and 20. Try Again",
                3000
            )
            return
        
        self.tries_remaining -= 1
        self.lb_tries_remaining.setText(f"{self.lb_tries_remaining.text().split(" ")[0]} {self.tries_remaining}")
        
        if user_guess == self.answer:
            self.statusbar.showMessage(
                f"Congratulations! You guessed the number {self.answer}!",
                5000
            )
            
            game_dict = {
                "username": "john_doe",
                "tries_left": self.tries_remaining,
                "answer": self.answer
            }

            return self.json_engine.write_to_json(game_dict)
        elif self.tries_remaining <= 0:
            self.statusbar.showMessage(
                f"Game Over! The number was {self.answer}",
                5000
            )
            
            game_dict = {
                "username": "john_doe",
                "tries_left": self.tries_remaining,
                "answer": self.answer
            }

            return self.json_engine.write_to_json(game_dict)
        elif user_guess < self.answer:
            self.statusbar.showMessage(
                f"Too low! {self.tries_remaining} tries remaining.",
                3000
            )
            return
        else:
            self.statusbar.showMessage(
                f"Too high! {self.tries_remaining} tries remaining.",
                3000
            )
            return