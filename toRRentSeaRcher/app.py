import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

# Создание приложения
app = tk.Tk()
app.title('Searching App')
app.configure()

# Текстовая надпись
app_name = ttk.Label(app, text='Searcher', font='verdana 20 bold', foreground='gray')
app_name.grid(row=0, column=1)

# Лейбл
search_label = ttk.Label(app, text='Search')
search_label.grid(row=1, column=0)

# Поле для ввода информации
text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=1)


# Переменная для записи выбора поисковой системы
search_engine = StringVar()
search_engine.set('yandex')

# Функции поиска
def search():
    if text_field.get().strip() != '':
        if search_engine.get() == 'rutracker':
            webbrowser.open('https://rutracker.org/forum/tracker.php?nm=' + text_field.get())
        elif search_engine.get() == 'nnm':
            webbrowser.open('https://nnmclub.ro/forum/tracker.php' + text_field.get())
        elif search_engine.get() !='':
            webbrowser.open('https://yandex.ua/search/?lr=143&clid=2270516&win=375&text=' + text_field.get())

def searchButton():
    search()


def enterButton(event):
    search()

# Кнопка выполения поиска
btn_search = ttk.Button(app, text='Go...', width=10, command=searchButton)
btn_search.grid(row=1, column=2)

# Обработчик событий на нажатие кнопки Enter
text_field.bind('<Return>', enterButton)

# Select the torrent
radio_rutracker = ttk.Radiobutton(app, text='ruTracker', value='rutracker', variable=search_engine)
radio_rutracker.grid(row=2, column=1, sticky=W)

radio_nnm = ttk.Radiobutton(app, text='NNM - club', value='nnm', variable=search_engine)
radio_nnm.grid(row=2, column=2, sticky=E)

radio_yandex = ttk.Radiobutton(app, text='yandex', value='yandex', variable=search_engine)
radio_yandex.grid(row=2, column=0, sticky=S)

app.wm_attributes('-topmost', True)
text_field.focus()

app.mainloop()
