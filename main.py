from tkinter import *
from time import time
from tkinter import messagebox as mb
import global_vars

def show_help():
    mb.showinfo(message="жми кнопку быстреееееее")

def show_record():
    record = ""
    with open('cliker_record.txt', 'r', encoding= "utf-8") as f:
        record_list = f.readlines()
        record = "".join(record_list)
    mb.showinfo(message=record)
def show_about():
    mb.showinfo(message="долго делал.....")

def cliker():
    counter_counter = 0
    start = time()
    def chec_record(name: str, points: int) ->None:
        with open('cliker_record.txt', 'r+') as f:

            record_list = f.readlines()
            new_record_list = [line.strip('\n').split() for line in record_list]
            index = 0
            for line_num in new_record_list:
                if points > int(line_num[2]):
                    new_record_list.insert(index, [str(index + 1), name, str(points)])
                    break
            for line_num in range(index + 1, len(new_record_list)):
                record_list = [" ".join(i) + "\n" for i in new_record_list]
            f.seek(0)

            f.writelines(record_list)

            new_record_list[line_num][0] = str(line_num + 1)
            print(new_record_list)
    def on_click():
        if global_vars.cc ==0:
            global_vars.sc = time()

        start = time()
        if time()-global_vars.sc<3:
            global_vars.cc += 1
            lbl.config(text=f"Кликов\n{ global_vars.cc}")
        else:
            confirm = mb.showinfo(message=f'Хватит ЖАть!\nваш результат { global_vars.cc}!')
            if confirm=="ok":
                global_vars.sc = time()
                global_vars.cc = 0

    root = Tk()
    root.geometry('600x400')
    root.resizable(False, False)
    icon_img = PhotoImage(file="index.png")
    root.iconphoto(False, icon_img)
    """
    создаем главное меню
    """
    mainmenu = Menu(root)
    root.config(menu = mainmenu)

   # mainmenu.add_command(label = "выход", command = root.destroy)
   # mainmenu.add_command(label = "cправка")


    filemenu = Menu(mainmenu, tearoff = 0)
    filemenu.add_command(label = "выход", command = root.destroy)

    refmenu = Menu(mainmenu, tearoff = 1)
    refmenu.add_command(label = "помощь", command = show_help)
    refmenu.add_command(label="о программе", command=show_about)
    refmenu.add_command(label="рекорды", command=show_record)

    mainmenu.add_cascade(label = "файл", menu = filemenu)
    mainmenu.add_cascade(label="справка", menu = refmenu)


    btn = Button(text = 'Жми сюда!',
                  font=("Comic Sans", 15, 'bold'),
                  width = 50,
                  height = 3,
                  bg='red',
                  fg='yellow',
                  relief=RIDGE,
                  bd=10,
                  command=on_click)


    lbl = Label(text ="Кликов\n0",
              font=("Comic Sans", 15, 'bold'),
              width = 50,
              height = 3,)
    lbl.pack()
    btn.pack()
    root.mainloop()

if __name__=="__main__":

    cliker()

    # name = input('Enter player name ')
    # points = int(input('Enter points'))
