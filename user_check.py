from tkinter import *

root = Tk()

# Фиксированные размеры окна
root.geometry('1000x500')
root.resizable(False, False)

root.title('Вход – Прогнозирование отчисленных студентов')

# Поле ввода имени пользователя
label_name = Label(root, text='Введите имя пользователя')
username_entry = Entry(root)
label_name.pack(padx=10, pady=10)
username_entry.pack(padx=10, pady=10)

# Поле ввода пароля
label_password = Label(root, text='Введите пароль')
password_entry = Entry(root)
label_password.pack(padx=10, pady=10)
password_entry.pack(padx=10, pady=10)

# Кнопка "Вход"
entered_btn = Button(root, text='Войти в систему')
entered_btn.pack(padx=10, pady=10)

root.mainloop()