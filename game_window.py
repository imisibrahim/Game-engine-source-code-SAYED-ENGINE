from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QKeyEvent

class FPSPlayer:
    def __init__(self):
        self.position = [0, 0, 0]

    def update(self):
        pass  # Placeholder for player update logic

class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Game Window")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        
        # Timer for game loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)  # Approximately 60 FPS

        # Initialize player
        self.fps_player = FPSPlayer()
        self.fps_player.position = [0, 1, -5]  # Starting position

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # Add viewport or game elements here
        layout.addWidget(QLabel("This is where the game will run!"))
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def update_game(self):
        # Update game logic here
        self.fps_player.update()  # Update player position
        print(f"Player Position: {self.fps_player.position}")  # Debug output

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_W:
            self.fps_player.position[2] += 0.1  # Move forward
        elif event.key() == Qt.Key_S:
            self.fps_player.position[2] -= 0.1  # Move backward
        elif event.key() == Qt.Key_A:
            self.fps_player.position[0] -= 0.1  # Move left
        elif event.key() == Qt.Key_D:
            self.fps_player.position[0] += 0.1  # Move right
        self.update()  # Refresh the window

    def closeEvent(self, event):
        self.timer.stop()  # Stop the timer when closing the window
        event.accept()
