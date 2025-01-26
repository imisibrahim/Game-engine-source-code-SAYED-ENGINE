import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QSplitter, QWidget, 
                          QVBoxLayout, QHBoxLayout, QDockWidget, QMenuBar,
                          QStatusBar, QFileDialog)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from editor.code_editor import CodeEditor
from editor.viewport import Viewport

class SayedEngine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sayed Engine ")
        self.setGeometry(100, 100, 1920, 1080)
        
        self.init_ui()
        self.init_menubar()
        self.init_statusbar()
        
    def init_ui(self):
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        
        # Create main splitter
        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left side - Code Editor
        self.code_editor = CodeEditor()
        
        # Right side - 3D Viewport
        self.viewport = Viewport()
        
        # Add to splitter
        self.main_splitter.addWidget(self.code_editor)
        self.main_splitter.addWidget(self.viewport)
        
        # Set initial sizes (40% left, 60% right)
        self.main_splitter.setSizes([768, 1152])
        
        # Add splitter to layout
        self.layout.addWidget(self.main_splitter)
        
    def init_menubar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New Project", self.new_project)
        file_menu.addAction("Open Project", self.open_project)
        file_menu.addAction("Save Project", self.save_project)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addSeparator()
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        
        # Save Action
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        menubar.addAction(save_action)
        
        # Open Action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        menubar.addAction(open_action)
        
        # Compile Action
        compile_action = QAction("Compile", self)
        compile_action.triggered.connect(self.code_editor.execute_code)
        menubar.addAction(compile_action)
        
        # Run Action
        run_action = QAction("Run", self)
        run_action.triggered.connect(self.run_game)
        menubar.addAction(run_action)
    
    def init_statusbar(self):
        self.statusBar().showMessage("Ready")
    
    def new_project(self):
        pass
    
    def open_project(self):
        pass
    
    def save_project(self):
        pass
    
    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.code_editor.toPlainText())

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as f:
                code = f.read()
                self.code_editor.setPlainText(code)

    def run_game(self):
        # Create a new window for the game
        self.game_window = GameWindow(self)
        self.game_window.show()

def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Create and show main window
    window = SayedEngine()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
