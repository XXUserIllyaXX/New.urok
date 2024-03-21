from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

app = QApplication([])
main_window = QWidget()
main_window.setFixedSize(700, 800)
main_window.setWindowTitle("Замітки")

main_layout = QHBoxLayout()
text_field = QTextEdit()
main_layout.addWidget(text_field)

function_line = QVBoxLayout()
main_layout.addLayout(function_line)

list_title = QLabel("Список заміток")
function_line.addWidget(list_title)
note_list = QListWidget()
function_line.addWidget(note_list)

notes_layout = QHBoxLayout()
add_note = QPushButton("Створити замітку")
del_note = QPushButton("Видалити замітку")
notes_layout.addWidget(add_note)
notes_layout.addWidget(del_note)
function_line.addLayout(notes_layout)
save_note = QPushButton("Зберегти замітку")
function_line.addWidget(save_note)

tag_title = QLabel("Список тегів")
function_line.addWidget(tag_title)
tag_list = QListWidget()
function_line.addWidget(tag_list)

tags_layout = QHBoxLayout()
add_tag = QPushButton("Створити тег")
del_tag = QPushButton("Видалити тег")
tags_layout.addWidget(add_tag)
tags_layout.addWidget(del_tag)
function_line.addLayout(tags_layout)

tag_edit = QLineEdit()
function_line.addWidget(tag_edit)
save_tag = QPushButton("Зберегти тег")
function_line.addWidget(save_tag)

main_window.setLayout(main_layout)
main_window.show()

# у віджет-список додати інформацію про замітки

def active_note():
    # отримати назву елемента списку, який зараз вибраний
    title = note_list.selectedItems()[0].text()
    # інформація цієї замітки з'явилася на екрані
    # отримати замітку по її назві
    note = notes_data[title] # з даних про замітки взяти замітку, на яку ми натиснули
    text_field.setText(note['опис'])
    # очистити список тегів
    tag_list.clear()
    # вставити нові теги
    tag_list.addItems(note['теги'])
# коли на елемент списку натиснуть
note_list.itemClicked.connect(active_note)


def noteSaving():
    text = text_field.toPlainText() # зберегти текст із цього віджета
    # як дізнатися назву замітки, яка зараз використовується
    title = note_list.selectedItems()[0].text()
    notes_data[title]["опис"] = text

save_note.clicked.connect(noteSaving)

def delete_note():
    title = note_list.selectedItems()[0].text()
    # видалення замітки
    del notes_data[title]
    # перезаписати віджет списку
    note_list.clear()
    note_list.addItems(notes_data)
del_note.clicked.connect(delete_note)

'''
    Завдання - зробити функцію, що визначає яка замітка зараз вибрана (ЇЇ назву)
    Потім вона видаляється із словника заміток (notes_data)
'''

app.exec_()  # після того, як програма закінчила роботу
note_list.addItems(notes_data)
with open('data.json', 'w', encoding='UTF-8') as file:
    # завантажити файл json
    json_dump(notes_data, file)