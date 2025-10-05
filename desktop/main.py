from PySide6 import QtWidgets as qtw
from app.logic.main import MainWindow
from app.utils.json import JsonEngine

import asyncio
import json
import sys
import os


async def start():
    json_engine = JsonEngine()

    curr_dir = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(curr_dir, "data")

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    user_file = os.path.join(data_dir, "user.json")

    if not os.path.isfile(user_file):
        with open(user_file, 'w+', encoding="utf-8-sig") as f:
            json.dump({"history": []}, f, indent=2)
    
    app = qtw.QApplication(sys.argv)
 
    window = MainWindow(json_engine)
    window.show()
 
    sys.exit(app.exec())
 
 
if __name__ == '__main__':
    asyncio.run(start())