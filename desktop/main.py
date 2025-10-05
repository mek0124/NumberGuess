from PySide6 import QtWidgets as qtw
from ui.main_window import Ui_w_MainWindow

import asyncio
import json
import sys
import os
import random


class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()
 
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
        
        self.start_new_game()

    def start_new_game(self):
        self.answer = random.randint(1, 20)
        self.tries_remaining = 5

        self.lb_tries_remaining.setText(f"{self.lb_tries_remaining.text().split(" ")[0]} {self.tries_remaining}")
        self.statusbar.clearMessage()
        
        self.le_user_guess.clear()
        self.le_user_guess.setFocus()

    def get_file_path(self, file_name: str = "user.json") -> str:
        curr_dir = os.path.abspath(os.path.dirname(__file__))
        data_dir = os.path.join(curr_dir, "data")

        if not os.path.isdir(data_dir):
            os.makedirs(data_dir, exist_ok=True)

        user_file = os.path.join(data_dir, "user.json")

        if not os.path.isdir(user_file):
            with open(user_file, 'w+', encoding="utf-8-sig") as f:
                json.dump({"history": []}, f, indent=2)

            return user_file
        
        return user_file

    def write_to_json(self, game_dict: dict) -> None:
        user_json_file = self.get_file_path()

        with open(user_json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)
            data["history"].append(game_dict)

            with open(user_json_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)

        return

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

            return self.write_to_json(game_dict)
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

            return self.write_to_json(game_dict)
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


async def start():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(curr_dir, "data")

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    user_file = os.path.join(data_dir, "user.json")

    if not os.path.isfile(user_file):
        with open(user_file, 'w+', encoding="utf-8-sig") as f:
            json.dump({"history": []}, f, indent=2)
    
    app = qtw.QApplication(sys.argv)
 
    window = MainWindow()
    window.show()
 
    sys.exit(app.exec())
 
 
if __name__ == '__main__':
    asyncio.run(start())