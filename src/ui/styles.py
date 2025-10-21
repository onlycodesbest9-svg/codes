"""Styling and themes for RecursiveLearn."""


LIGHT_THEME = """
QMainWindow {
    background-color: #f5f5f5;
}

QWidget {
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 13px;
    color: #212121;
}

QPushButton {
    background-color: #2196F3;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-size: 14px;
    font-weight: 600;
    min-height: 40px;
}

QPushButton:hover {
    background-color: #1976D2;
    cursor: pointer;
}

QPushButton:pressed {
    background-color: #0D47A1;
}

QPushButton:disabled {
    background-color: #BDBDBD;
    color: #757575;
}

QPushButton#secondaryButton {
    background-color: #EEEEEE;
    color: #212121;
    border: 2px solid #BDBDBD;
}

QPushButton#secondaryButton:hover {
    background-color: #E0E0E0;
    border: 2px solid #9E9E9E;
}

QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: white;
    border: 2px solid #BDBDBD;
    border-radius: 6px;
    padding: 10px;
    font-size: 14px;
    color: #212121;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 2px solid #2196F3;
    outline: none;
}

QLabel {
    color: #212121;
    font-size: 13px;
}

QLabel#titleLabel {
    font-size: 28px;
    font-weight: bold;
    color: #1565C0;
    padding: 10px 0px;
}

QLabel#sectionTitle {
    font-size: 20px;
    font-weight: 600;
    color: #212121;
    margin-top: 15px;
    margin-bottom: 10px;
}

QGroupBox {
    border: 2px solid #E0E0E0;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 15px;
    font-weight: 600;
    background-color: white;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #1976D2;
}

QTabWidget::pane {
    border: 2px solid #E0E0E0;
    border-radius: 8px;
    background-color: white;
}

QTabBar::tab {
    background-color: #EEEEEE;
    color: #666666;
    border: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 10px 20px;
    margin-right: 2px;
    font-weight: 500;
}

QTabBar::tab:selected {
    background-color: white;
    color: #2196F3;
}

QTabBar::tab:hover {
    background-color: #E3F2FD;
}

QListWidget {
    background-color: white;
    border: 2px solid #E0E0E0;
    border-radius: 6px;
    padding: 5px;
}

QListWidget::item {
    border-radius: 4px;
    padding: 8px;
    margin: 2px;
}

QListWidget::item:selected {
    background-color: #E3F2FD;
    color: #1976D2;
}

QListWidget::item:hover {
    background-color: #F5F5F5;
}

QScrollBar:vertical {
    border: none;
    background-color: #F5F5F5;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #BDBDBD;
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: #9E9E9E;
}

QComboBox {
    background-color: white;
    border: 2px solid #E0E0E0;
    border-radius: 6px;
    padding: 6px;
}

QComboBox:hover {
    border: 2px solid #2196F3;
}

QCheckBox {
    spacing: 8px;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #BDBDBD;
    border-radius: 4px;
    background-color: white;
}

QCheckBox::indicator:checked {
    background-color: #2196F3;
    border: 2px solid #2196F3;
    image: url(check.png);
}
"""

DARK_THEME = """
QMainWindow {
    background-color: #1E1E1E;
}

QWidget {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 12px;
    color: #E0E0E0;
    background-color: #1E1E1E;
}

QPushButton {
    background-color: #0D47A1;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 13px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #1565C0;
}

QPushButton:pressed {
    background-color: #0A3D91;
}

QPushButton:disabled {
    background-color: #424242;
    color: #757575;
}

QPushButton#secondaryButton {
    background-color: #424242;
    color: #E0E0E0;
}

QPushButton#secondaryButton:hover {
    background-color: #616161;
}

QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #2D2D2D;
    border: 2px solid #424242;
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
    color: #E0E0E0;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 2px solid #1976D2;
}

QLabel {
    color: #E0E0E0;
    background-color: transparent;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: bold;
    color: #42A5F5;
}

QLabel#sectionTitle {
    font-size: 18px;
    font-weight: 600;
    color: #BDBDBD;
    margin-top: 10px;
}

QGroupBox {
    border: 2px solid #424242;
    border-radius: 8px;
    margin-top: 12px;
    padding-top: 15px;
    font-weight: 600;
    background-color: #2D2D2D;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #42A5F5;
}

QTabWidget::pane {
    border: 2px solid #424242;
    border-radius: 8px;
    background-color: #2D2D2D;
}

QTabBar::tab {
    background-color: #2D2D2D;
    color: #9E9E9E;
    border: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 10px 20px;
    margin-right: 2px;
    font-weight: 500;
}

QTabBar::tab:selected {
    background-color: #424242;
    color: #42A5F5;
}

QTabBar::tab:hover {
    background-color: #383838;
}

QListWidget {
    background-color: #2D2D2D;
    border: 2px solid #424242;
    border-radius: 6px;
    padding: 5px;
}

QListWidget::item {
    border-radius: 4px;
    padding: 8px;
    margin: 2px;
    color: #E0E0E0;
}

QListWidget::item:selected {
    background-color: #0D47A1;
    color: white;
}

QListWidget::item:hover {
    background-color: #383838;
}

QScrollBar:vertical {
    border: none;
    background-color: #2D2D2D;
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #616161;
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: #757575;
}

QComboBox {
    background-color: #2D2D2D;
    border: 2px solid #424242;
    border-radius: 6px;
    padding: 6px;
    color: #E0E0E0;
}

QComboBox:hover {
    border: 2px solid #1976D2;
}

QComboBox QAbstractItemView {
    background-color: #2D2D2D;
    color: #E0E0E0;
    selection-background-color: #0D47A1;
}

QCheckBox {
    spacing: 8px;
    color: #E0E0E0;
}

QCheckBox::indicator {
    width: 20px;
    height: 20px;
    border: 2px solid #616161;
    border-radius: 4px;
    background-color: #2D2D2D;
}

QCheckBox::indicator:checked {
    background-color: #1976D2;
    border: 2px solid #1976D2;
}

QTextBrowser {
    background-color: #2D2D2D;
    border: 2px solid #424242;
    border-radius: 6px;
    padding: 10px;
    color: #E0E0E0;
}

QMessageBox {
    font-size: 13px;
}

QMessageBox QPushButton {
    min-width: 80px;
}
"""


def get_stylesheet(theme='light'):
    """Get stylesheet for the specified theme."""
    if theme == 'dark':
        return DARK_THEME
    return LIGHT_THEME
