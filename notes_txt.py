#почни тут створювати додаток з розумними замітками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QTextEdit, QLineEdit, QListWidget, QInputDialog
import json

        


tag = "Тэги"
text_n = "Текст"





app = QApplication([])
win = QWidget()
win.resize(850, 600)
win.setWindowTitle("Умные заметки")
field_text = QTextEdit()
field_text.setPlaceholderText(text_n)
field_tag = QLineEdit()
field_tag.setPlaceholderText("Введите тэг")
list_tag = QListWidget()
list_title = QListWidget()
label_title = QLabel()
label_title.setText("Список заметок")
label_tag = QLabel()
label_tag.setText("Список тэгов")

#Инструкция[Уже что-то сломал?[руководство[бесполезность[



#Сделано для запуска считывания из файла(если есть)
try:
    with open("notes_data.txt", "r", encoding = "utf-8") as file:
        
        notes = dict()
        for line in file:
            notes_s = dict()
            tag_s = list()
            lay = line.split("[")
            title_s = lay[0]
            text_s = lay[1]
            notes_s[text_n] = text_s
            for i in range(2, len(lay)):
                if lay[i] != "\n":
                    tag_s.append(lay[i])
            notes_s[tag] = tag_s
            notes[title_s] = notes_s
except:
    notes = {
        "Инструкция" : {
            "Текст" : "Уже что-то сломал?",
            "Тэги" : ["руководство", "бесполезность"]
            }
        }


















def save_changes():
    with open("notes_data.txt", "w", encoding = "utf-8") as file:        
        for title in notes:
            file.write(title)
            file.write("[")
            file.write(notes[title][text_n])
            file.write("[")
            for tag_n in notes[title][tag]:
                file.write(tag_n)
                file.write("[")
            file.write("\n")

    










def show_note():

    name = list_title.selectedItems()[0].text()
    field_text.setText(notes[name][text_n])
    list_tag.clear()
    list_tag.addItems(notes[name][tag])






def show_note():

    name = list_title.selectedItems()[0].text()
    field_text.setText(notes[name][text_n])
    list_tag.clear()
    list_tag.addItems(notes[name][tag])

def save_note():

    if list_title.selectedItems():
        text = field_text.toPlainText()
        name = list_title.selectedItems()[0].text()
        notes[name][text_n] = text
        save_changes()

    else:
        message = QMessageBox()
        message.setWindowTitle("Внимание!")
        message.setText("Заметка не выбрана")
        message.exec_()
    
def add_note():
    dialog, result = QInputDialog.getText(
        win, "Добавить заметку", "Название заметки:"
    )
    if result:
        
        notes[dialog] = {
            "Текст" : "", 
            "Тэги" : []
            }
        list_title.clear()
        list_title.addItems(notes.keys())

        list_tag.clear()
        field_text.clear()

        #ДЫЫЫЫЫЫЫЫАААААААААААААААА
        list_title.setCurrentRow(len(list_title)-1)

        save_changes()

def del_note():
    if list_title.selectedItems():
        name = list_title.selectedItems()[0].text()
        del notes[name]
        save_changes()
        field_text.clear()
        list_tag.clear()
        list_title.clear()
        list_title.addItems(notes.keys())
    else:
        message = QMessageBox()
        message.setWindowTitle("Внимание!")
        message.setText("Заметка не выбрана")
        message.exec_()





#Тэги
def add_tag():
    if list_title.selectedItems():
        tag_s = field_tag.text()

        name = list_title.selectedItems()[0].text()
        notes[name][tag].append(tag_s)


        field_tag.clear()
        list_tag.clear()
        list_tag.addItems(notes[name][tag])

        save_changes()
    else:
        message = QMessageBox()
        message.setWindowTitle("Внимание!")
        message.setText("Заметка не выбрана")
        message.exec_()

def del_tag():
    if list_title.selectedItems():
        
        name = list_title.selectedItems()[0].text()

        if list_tag.selectedItems():

            tag_s = list_tag.selectedItems()[0].text()
            notes[name][tag].remove(tag_s)

            list_tag.clear()
            list_tag.addItems(notes[name][tag])

            save_changes()


        else:

            message = QMessageBox()
            message.setWindowTitle("Внимание!")
            message.setText("Тэг не выбран")
            message.exec_()
            
        
    
    else:
        message = QMessageBox()
        message.setWindowTitle("Внимание!")
        message.setText("Заметка не выбрана")
        message.exec_()




def search_tag():
    if list_tag.selectedItems():


        try:
            app.title_prog = list_title.selectedItems()[0].text()  #Зачем?
        except:
            app.title_prog = "all"





        tag_s = list_tag.selectedItems()[0].text()

        tag_list = list()

        for title in notes:

            if tag_s in notes[title][tag]:
                tag_list.append(title)

        list_title.clear()
        list_title.addItems(tag_list)

        list_tag.clear()
        list_tag.addItem(tag_s)

        button[5].hide()
        button[6].show()
    else:
        message = QMessageBox()
        message.setWindowTitle("Внимание!")
        message.setText("Тэг не выбран")
        message.exec_()

def unsearch_tag():
    list_title.clear()
    list_title.addItems(notes.keys())
    
    list_tag.clear()
    field_text.clear()

    #Для этого ! ! !

    if app.title_prog == "all":
        list_f_tag = list()
        for tag_n in notes:

            t = notes[tag_n]['Тэги']

            for t1 in t:

                if t1 in list_f_tag:
                    t = t

                else:
                    list_tag.addItem(t1)
                    list_f_tag.append(t1)
    else:
        list_tag.addItems(notes[app.title_prog][tag]) 

        field_text.setText(notes[app.title_prog][text_n])

    button[5].show()
    button[6].hide()

def show_all_tag():
    list_title.clear()
    list_title.addItems(notes.keys())

    list_tag.clear()
    list_f_tag = list()
    for tag_n in notes:

        t = notes[tag_n]['Тэги']

        for t1 in t:

            if t1 in list_f_tag:
                t = t

            else:
                list_tag.addItem(t1)
                list_f_tag.append(t1)

    field_text.clear()





















save_changes()



list_title.addItems(notes.keys())

list_f_tag = list()
for tag_n in notes:

    t = notes[tag_n]['Тэги']

    for t1 in t:

        if t1 in list_f_tag:
            t = t

        else:
            list_tag.addItem(t1)
            list_f_tag.append(t1)





p_b1 = QPushButton("Создать заметку")
p_b2 = QPushButton("Удалить заметку")
p_b3 = QPushButton("Сохранить заметку")
p_b4 = QPushButton("Добавить тэг")
p_b5 = QPushButton("Открепить тэг от заметки")
p_b6 = QPushButton("Искать заметки по тэгу")
p_b7 = QPushButton("Перестать искать заметки по тэгу")
p_b8 = QPushButton("Показать все тэги")


button = [p_b1, p_b2, p_b3, p_b4, p_b5, p_b6, p_b7, p_b8]

H_main_main = QHBoxLayout()
V1 = QVBoxLayout()
V2 = QVBoxLayout()
H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()


V1.addWidget(field_text)
H_main_main.addLayout(V1, stretch=1)

V2.addWidget(label_title, alignment = Qt.AlignLeft)
V2.addWidget(list_title)

H1.addWidget(button[0], alignment = Qt.AlignVCenter )
H1.addWidget(button[1], alignment = Qt.AlignVCenter )
V2.addLayout(H1)


V2.addWidget(button[2])
V2.addWidget(label_tag, alignment = Qt.AlignLeft)
V2.addWidget(list_tag)

V2.addWidget(field_tag)

H2.addWidget(button[3])
H2.addWidget(button[4])
V2.addLayout(H2)



H3.addWidget(button[5])
H3.addWidget(button[6])
button[6].hide()

H3.addWidget(button[7])

V2.addLayout(H3)





H_main_main.addLayout(V1)
H_main_main.addLayout(V2)







list_title.itemClicked.connect(show_note)

button[0].clicked.connect(add_note)
button[1].clicked.connect(del_note)
button[2].clicked.connect(save_note)


button[3].clicked.connect(add_tag)
button[4].clicked.connect(del_tag)
button[5].clicked.connect(search_tag)
button[6].clicked.connect(unsearch_tag)
button[7].clicked.connect(show_all_tag)




win.setLayout(H_main_main)

win.show()
app.exec_()