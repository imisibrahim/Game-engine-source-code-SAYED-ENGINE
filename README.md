# Sayed Engine

A real-time game development environment with a modern UI and powerful features.

## Features

- Modern dark-themed code editor with:
  - Python syntax highlighting
  - Line numbers
  - Current line highlighting
- 3D viewport with:
  - OpenGL rendering
  - Camera controls (orbit, pan, zoom)
  - Reference grid

## Installation

1. Make sure you have Python 3.9+ installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Engine

1. Navigate to the project directory:
   ```
   cd path/to/sayed_engine
   ```

2. Run the main script:
   ```
   python main.py
   ```

## Controls

### Viewport Navigation
- Left Mouse Button: Orbit camera
- Mouse Wheel: Zoom in/out

### Code Editor
- Standard text editing controls
- Syntax highlighting for Python
- Line numbers for easy reference

## Project Structure

- `main.py` - Main application entry point
- `editor/` - Editor-related components
  - `code_editor.py` - Code editor implementation
  - `viewport.py` - 3D viewport implementation
- `requirements.txt` - Python package dependencies
