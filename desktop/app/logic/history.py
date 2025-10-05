from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from app.ui.history_window import Ui_w_HistoryWindow
 
 
class HistoryWindow(qtw.QMainWindow, Ui_w_HistoryWindow):
    def __init__(self, json_engine):
        super().__init__()

        self.json_engine = json_engine
 
        self.setupUi(self)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        player_history = self.json_engine.get_player_history() or None

        if not player_history:
            pass
        
        self.populate_history(player_history)

    def populate_history(self, history_data):
        scroll_widget = self.scra_history.widget()
        layout = qtw.QVBoxLayout(scroll_widget)
        
        if not history_data:
            no_history_label = qtw.QLabel("No game history available")
            no_history_label.setAlignment(qtc.Qt.AlignCenter)
            layout.addWidget(no_history_label)
            
        else:
            for game in reversed(history_data):
                game_text = f"Username: {game.get('username', 'Unknown')} | Answer: {game.get('answer', 'N/A')} | Tries Left: {game.get('tries_left', 'N/A')}"
                game_label = qtw.QLabel(game_text)
                game_label.setAlignment(qtc.Qt.AlignCenter)
                layout.addWidget(game_label)
        
        layout.addStretch()