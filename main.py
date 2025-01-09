import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QMessageBox, QSizePolicy
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
from random import choice


class RockPaperScissors(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock-Paper-Scissors")
        self.setGeometry(100, 100, 600, 400)
        self.init_start_interface()

    def resource_path(self, relative_path):
        """ Get the absolute path for resources bundled with the executable. """
        try:
            # For PyInstaller, we use the _MEIPASS temporary folder
            base_path = sys._MEIPASS
        except Exception:
            # If running from source code, use the normal file path
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def init_start_interface(self):
        # Main widget and layout
        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: lightblue;")
        layout = QVBoxLayout()

        # Create a spacer to push the label in the center vertically
        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Title label (centered)
        self.title_label = QLabel("Welcome to Rock-Paper-Scissors!", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.title_label.setAlignment(Qt.AlignCenter)  # Center the text horizontally
        layout.addWidget(spacer)
        layout.addWidget(self.title_label)
        layout.addWidget(spacer)

        # Buttons
        play_button = QPushButton("Play", self)
        play_button.setStyleSheet("font-size: 16px;")
        play_button.clicked.connect(self.init_game_interface)
        layout.addWidget(play_button)

        rules_button = QPushButton("Rules", self)
        rules_button.setStyleSheet("font-size: 16px;")
        rules_button.clicked.connect(self.show_rules)
        layout.addWidget(rules_button)

        exit_button = QPushButton("Exit", self)
        exit_button.setStyleSheet("font-size: 16px;")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def init_game_interface(self):
        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: lightblue;")
        layout = QVBoxLayout()

        self.title_label = QLabel("Rock-Paper-Scissors", self)
        self.title_label.setStyleSheet("font-size: 48px; font-weight: bold; text-align: center;")
        layout.addWidget(self.title_label)

        self.result_label = QLabel("Computer chose: ", self)
        self.result_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        layout.addWidget(self.result_label)

        button_layout = QHBoxLayout()

        self.rock_button = QPushButton(self)
        self.rock_button.setIcon(QIcon(self.resource_path("Scripts/rock.png")))  # Use the resource_path method
        self.rock_button.setIconSize(QSize(100, 100))
        self.rock_button.setFixedSize(150, 150)
        self.rock_button.clicked.connect(lambda: self.play("Rock"))
        button_layout.addWidget(self.rock_button)

        self.paper_button = QPushButton(self)
        self.paper_button.setIcon(QIcon(self.resource_path("Scripts/paper.png")))  # Use the resource_path method
        self.paper_button.setIconSize(QSize(100, 100))
        self.paper_button.setFixedSize(150, 150)
        self.paper_button.clicked.connect(lambda: self.play("Paper"))
        button_layout.addWidget(self.paper_button)

        self.scissors_button = QPushButton(self)
        self.scissors_button.setIcon(QIcon(self.resource_path("Scripts/scissors.png")))  # Use the resource_path method
        self.scissors_button.setIconSize(QSize(100, 100))
        self.scissors_button.setFixedSize(150, 150)
        self.scissors_button.clicked.connect(lambda: self.play("Scissors"))
        button_layout.addWidget(self.scissors_button)

        layout.addLayout(button_layout)

        back_layout = QHBoxLayout()
        back_button = QPushButton("Back to Menu", self)
        back_button.setStyleSheet("font-size: 16px;")
        back_button.clicked.connect(self.init_start_interface)
        back_layout.addStretch(1)
        back_layout.addWidget(back_button)
        layout.addLayout(back_layout)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def show_rules(self):
        rules_window = QMessageBox(self)
        rules_window.setWindowTitle("Rules")
        rules_window.setText("""
        How to Play Rock-Paper-Scissors:

        - Rock beats Scissors.
        - Scissors beat Paper.
        - Paper beats Rock.

        Click one of the buttons to make your choice.
        The computer will randomly select its choice, and the winner will be determined.
        """)
        rules_window.setStandardButtons(QMessageBox.Ok)
        rules_window.exec_()

    def play(self, player_choice):
        computer_choice = choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(player_choice, computer_choice)
        self.result_label.setText(f"Computer chose: {computer_choice}\n{result}")

    @staticmethod
    def determine_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
                (player_choice == "Rock" and computer_choice == "Scissors") or
                (player_choice == "Scissors" and computer_choice == "Paper") or
                (player_choice == "Paper" and computer_choice == "Rock")
        ):
            return "You win!"
        else:
            return "Computer wins!"


if __name__ == "__main__":
    app = QApplication([])
    window = RockPaperScissors()
    window.show()
    app.exec_()
