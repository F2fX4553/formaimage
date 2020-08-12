from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image

import matplotlib.pyplot as plt
import numpy as np

ton = Tk()
ton.iconbitmap('foldricon.ico')
ton.title('Secret Files')
ton.config(background='#CDD0D4')

fw = 800  # hajm width ta3 lforma
fh = 600  # hajm height ta3 lforma
x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
ton.geometry('%dx%d+%d+%d' % (fw, fh, x, y))  # han jm3t kolch

panel1 = PanedWindow(bd = 1,relief ='raised',bg = 'grey')
panel1.pack(fill = BOTH,expand = 1)


lft_label = Label(panel1 ,bg = 'white',width = 15)
panel1.add(lft_label)

def formaphoto():
    imag = Toplevel()
    imag.iconbitmap('foldricon.ico')
    imag.title('Secret Files')
    imag.config(background='#CDD0D4')
    fw = 800
    fh = 500
    x = (imag.winfo_screenwidth() - fw) / 2
    y = (imag.winfo_screenheight() - fh) / 2
    imag.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    my_menu = Menu(imag)
    imag.config(menu = my_menu)

    def openfilename():

        openimage = filedialog.askopenfilename( title="Choose Image",filetypes=(("Images", ""
                                                            ".PNG;.JPEG;*.JPG;*.GIF;*.BMP;"),("All files", ".")))


        img_path = ImageTk.PhotoImage(Image.open(openimage))
        #imag_button = Label(imag,image=img_path)


        nr = 5  # number of rows
        nc = 4  # number of columns

        imag_button = []

        for i in range(nr * nc):
            imag_button.append(Label(imag, image=img_path))
            imag_button[-1].grid(row=i // nc, column=i % nc)

        #imag_button.place(x = 10,y = 10)




        openfilename(False)







    def savefilename():
        imag.Filename = filedialog.asksaveasfilename(title='Select A File',filetypes=(('png fies', '*.png'), ('all files', '*.*')))

        image_my = ImageTk.PhotoImage(Image.open(imag.Filename))
        imag_button = Label(imag, image=image_my)
        imag_button.place(x=5, y=5)
        savefilename()



    menu = Menu(imag)

    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New Save", command=savefilename)
    filemenu.add_command(label="Open", command= openfilename)
    filemenu.add_command(label="Save", command=savefilename)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=imag.destroy)

    imag.config(menu=menu)

    imag.grab_set()
def formaviduo():
    vido = Toplevel()
    vido.iconbitmap('foldricon.ico')
    vido.title('Secret Files')
    vido.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 500  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    vido.geometry('%dx%d+%d+%d' % (fw, fh, x, y))
    my_menu = Menu(vido)
    vido.config(menu=my_menu)

    def openfilenames():
        vido.Filename = filedialog.askopenfilename(title='Select A File',filetypes=(('MP4 fies', '*.mp4'), ('all files', '*.*')))
        image_my = ImageTk.PhotoImage(Image.open(vido.Filename))
        imag_button = Label(vido, image=image_my)
        imag_button.place(x=5, y=5)
        openfilenames()

    def savefilenames():
        vido.Filename = filedialog.asksaveasfilename(title='Select A File',filetypes=(('MP4 fies', '*.mp4'), ('all files', '*.*')))
        image_my = ImageTk.PhotoImage(Image.open(vido.Filename))
        imag_button = Label(vido, image=image_my)
        imag_button.place(x=5, y=5)
        savefilenames()

    menu = Menu(vido)

    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New Save", command=savefilenames)
    filemenu.add_command(label="Open", command=openfilenames)
    filemenu.add_command(label="Save", command=savefilenames)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=vido.destroy)

    vido.config(menu=menu)

    vido.grab_set()

def formamusic():
    miosc = Toplevel()
    miosc.iconbitmap('foldricon.ico')
    miosc.title('Secret Files')
    miosc.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    miosc.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    miosc.grab_set()

def formatxt():
    txttt = Toplevel()
    txttt.iconbitmap('foldricon.ico')
    txttt.title('Secret Files')
    txttt.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    txttt.geometry('%dx%d+%d+%d' % (fw, fh, x, y))


    txttt.grab_set()

def formahtml():

    htmll = Toplevel()
    htmll.iconbitmap('foldricon.ico')
    htmll.title('Secret Files')
    htmll.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    htmll.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    htmll.grab_set()

def formapdf():

    pdff = Toplevel()
    pdff.iconbitmap('foldricon.ico')
    pdff.title('Secret Files')
    pdff.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    pdff.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    pdff.grab_set()

def formacss():

    csss = Toplevel()
    csss.iconbitmap('foldricon.ico')
    csss.title('Secret Files')
    csss.config(background='#CDD0D4')
    fw = 800  # hajm width ta3 lforma
    fh = 600  # hajm height ta3 lforma
    x = (ton.winfo_screenwidth() - fw) / 2  # hna ydi hjm licron o yn9s mno width ta3 lforma wy9smha 3la 2
    y = (ton.winfo_screenheight() - fh) / 2 - 50  # hna ydi hjm licron o yn9s height ta3 lforma wy9smha 3la 2 o yn9slh 50
    csss.geometry('%dx%d+%d+%d' % (fw, fh, x, y))

    csss.grab_set()


l = ttk.Label(panel1, text='Photos', font='None 10', background='white')
l.place(x=6, y=5)

photo = PhotoImage(file = 'photo1.png')
btn = Button(panel1,image = photo,border = 0,bg = 'white',command = formaphoto)
btn.place(x = 60,y = 1)

l2 = ttk.Label(panel1, text='Video', font='None 10', background='white')
l2.place(x=6, y=45)

photo2 = PhotoImage(file = 'photo2.png')
btn2 = Button(panel1,image = photo2,border = 0,bg = 'white',command = formaviduo)
btn2.place(x = 60,y = 40)


l3 = ttk.Label(panel1, text='Music', font='None 10', background='white')
l3.place(x=6, y=90)

photo3 = PhotoImage(file = 'photo3.png')
btn3 = Button(panel1,image = photo3,border = 0,bg = 'white',command = formamusic)
btn3.place(x = 60,y = 85)

l4 = ttk.Label(panel1, text='Texts', font='None 10', background='white')
l4.place(x=6, y=130)

btn5 = Button(panel1, text='TXT', font='None 10', border=0, bg='white',command = formatxt)
#btn5.place(x=60, y=160)

btn6 = Button(panel1, text='HTML', font='None 10', border=0, bg='white',command = formahtml)
#btn6.place(x=60, y=195)

btn7 = Button(panel1, text='PDF', font='None 10', border=0, bg='white',command = formapdf)
#btn7.place(x=60, y=230)


btn8 = Button(panel1, text='CSS', font='None 10', border=0, bg='white',command = formacss)


def show():
    btn5.place(x=60, y=160)
    btn6.place(x=60, y=195)
    btn7.place(x=60, y=230)
    btn8.place(x =60,y=260)



photo4 = PhotoImage(file = 'photo4.png')
btn4 = Button(panel1,image = photo4,border = 0,bg = 'white',command = show)
btn4.place(x = 60,y = 125)

#########################################################################################################
panel_2 = PanedWindow(panel1,orient = VERTICAL,bd = 1,relief = 'raised',bg = 'white') # hdi lforma2
panel1.add(panel_2)

###############################
frem = Frame(panel_2)
frem.place(x = 0,y = 0)
photo5 = PhotoImage(file = 'photo5.png')
l5 = Button(panel_2,image = photo5,border = 0,background='white',command = formaphoto)
l5.place(x=150, y=120)

photo6 = PhotoImage(file = 'photo6.png')
l6 = Button(panel_2,image = photo6,border = 0,background='white',command = formaviduo)
l6.place(x=20, y=120)

photo7 = PhotoImage(file = 'photo7.png')
l7 = Button(panel_2,image = photo7,border = 0,background='white')
l7.place(x=530, y=10)

photo8 = PhotoImage(file = 'photo8.png')
l8 = Button(panel_2,image = photo8,border = 0,background='white')
l8.place(x=400, y=10)

photo9 = PhotoImage(file = 'photo9.png')
l9 = Button(panel_2,image = photo9,border = 0,background='white')
l9.place(x=280, y=10)

photo10 = PhotoImage(file = 'photo10.png')
l10 = Button(panel_2,image = photo10,border = 0,background='white')
l10.place(x=150, y=10)

photo11 = PhotoImage(file = 'photo11.png')
l11 = Button(panel_2,image = photo11,border = 0,background='white')
l11.place(x=20, y=10)

#ton.resizable(False,False)
ton.mainloop()
