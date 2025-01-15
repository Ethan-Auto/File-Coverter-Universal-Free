from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QComboBox
from PySide6.QtGui import QPalette, QColor, QLinearGradient, QBrush, QFont
import sys
from converters.converter import FileConverter  # Import FileConverter
from utils.helper import validate_file_format, get_supported_formats  # Import helper functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.setGeometry(100, 100, 400, 200)
        self.converter = FileConverter()  # Initialize FileConverter

        self.dark_mode_enabled = True
        self.apply_dark_mode()
        self.apply_gradient_background()
        self.set_custom_fonts()

        self.layout = QVBoxLayout()

        self.label = QLabel("Select a file to convert:")
        self.layout.addWidget(self.label)

        self.select_button = QPushButton("Select File")
        self.select_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_button)

        self.output_format_label = QLabel("Select Output Format:")
        self.layout.addWidget(self.output_format_label)

        self.output_format_var = QComboBox(self)
        self.output_format_var.addItems(get_supported_formats())
        self.layout.addWidget(self.output_format_var)

        self.convert_button = QPushButton("Convert File")
        self.convert_button.clicked.connect(self.convert_file)
        self.layout.addWidget(self.convert_button)

        self.toggle_dark_mode_button = QPushButton("Toggle Dark Mode")
        self.toggle_dark_mode_button.clicked.connect(self.toggle_dark_mode)
        self.layout.addWidget(self.toggle_dark_mode_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def apply_dark_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(40, 40, 40))
        palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.Base, QColor(30, 30, 30))
        palette.setColor(QPalette.AlternateBase, QColor(40, 40, 40))
        palette.setColor(QPalette.ToolTipBase, QColor(220, 220, 220))
        palette.setColor(QPalette.ToolTipText, QColor(220, 220, 220))
        palette.setColor(QPalette.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        self.setPalette(palette)

    def apply_light_mode(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        palette.setColor(QPalette.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.AlternateBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, QColor(0, 0, 0))
        palette.setColor(QPalette.Button, QColor(255, 255, 255))
        palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

    def apply_gradient_background(self):
        gradient = QLinearGradient(0, 0, 400, 200)
        gradient.setColorAt(0, QColor(0, 0, 0))
        gradient.setColorAt(1, QColor(42, 130, 218))
        brush = QBrush(gradient)
        palette = self.palette()
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

    def set_custom_fonts(self):
        font = QFont("Arial", 10)
        self.setFont(font)

    def toggle_dark_mode(self):
        if self.dark_mode_enabled:
            self.apply_light_mode()
        else:
            self.apply_dark_mode()
        self.dark_mode_enabled = not self.dark_mode_enabled

    def select_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;Text Files (*.txt);;PDF Files (*.pdf);;CSV Files (*.csv)", options=options)
        if file_name:
            self.label.setText(f"Selected file: {file_name}")
            self.input_file = file_name

    def convert_file(self):
        input_file = self.input_file
        output_format = self.output_format_var.currentText()
        output_file, _ = QFileDialog.getSaveFileName(self, "Save File", "", f"*.{output_format}")

        if not input_file or not output_file:
            self.label.setText("Please select input and output files.")
            return

        input_format = input_file.split('.')[-1].lower()
        if not validate_file_format(input_file, get_supported_formats()):
            self.label.setText(f"Unsupported input file format: {input_format.upper()}")
            return

        if not self.converter.is_conversion_supported(input_format, output_format):
            self.label.setText(f"Conversion from {input_format.upper()} to {output_format.upper()} is not supported.")
            return

        try:
            if input_format == 'pdf' and output_format in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']:
                self.converter.convert_pdf_to_image(input_file, output_file, output_format)
            elif input_format in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'] and output_format == 'pdf':
                self.converter.convert_image_to_pdf(input_file, output_file)
            else:
                conversion_method = getattr(self.converter, f"convert_to_{output_format}")
                conversion_method(input_file, output_file)
            self.label.setText(f"File converted to {output_format.upper()} successfully.")
        except Exception as e:
            self.label.setText(f"An error occurred: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())