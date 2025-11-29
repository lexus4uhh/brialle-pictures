from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QFileDialog, QVBoxLayout, QWidget, QListWidget
)

from main_symbs import get_symbols, print_symbols

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Choosing files and directory")
window.setGeometry(100, 100, 500, 400)

list_widget = QListWidget()

files = []
directory = ""

button_files = QPushButton("Choose files")
def select_files():
    global files
    options = QFileDialog.Options()
    files, _ = QFileDialog.getOpenFileNames(
        window,
        "choose images",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp);;All file (*)",
        options=options
    )
    if files:
        list_widget.addItems(files)
        print(f"Chosen files: {files}")

button_files.clicked.connect(select_files)

button_dir = QPushButton("Choose directory to save in .txt")
def select_directory():
    global directory
    directory = QFileDialog.getExistingDirectory(
        window,
        "Choose directory",
        ""
    )
    if directory:
        list_widget.addItem(f"Directory: {directory}")
        print(f"Directory: {directory}")

button_dir.clicked.connect(select_directory)

button_ok = QPushButton("Done")
def ok():
    print(files, directory)
    if files and directory:
        for i in files:
            symbs = get_symbols(i)
            file_name = i.split("/")[-1].split(".")[0]
            output_path = f"{directory}/{file_name}.txt"
            print_symbols(symbs, output_path)
button_ok.clicked.connect(ok)

layout = QVBoxLayout()
layout.addWidget(button_files)
layout.addWidget(button_dir)
layout.addWidget(list_widget)
layout.addWidget(button_ok)


container = QWidget()
container.setLayout(layout)
window.setCentralWidget(container)

window.show()

app.exec_()
