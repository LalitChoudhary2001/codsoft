import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("To-Do List App")

        self.task_label = QLabel("Task:")
        self.task_input = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget()

        layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_label)
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()

def main():
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
