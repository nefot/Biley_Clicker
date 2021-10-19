from tkinter import *
from time import time
from tkinter import messagebox as mb

def cliker():
    counter = 0
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
        nonlocal counter , start
        if time()-start<3:
            counter += 1
            lbl.config(text=f"Кликов\n{counter}")
        else:
            confirm = mb.showinfo(message=f'Хватит ЖАть!\nваш результат {counter}!')
            if confirm=="ok":
                start = time()
                counter = 0

    root = Tk()
    root.geometry('600x400')
    root.resizable(False, False)
    icon_img = PhotoImage(file="index.png")
    root.iconphoto(False, icon_img)


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

    #cliker()

    name = input('Enter player name ')
    points = int(input('Enter points'))
