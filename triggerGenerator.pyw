from tkinter import *

# ======================================================================
# == FONCTIONS

def generatorCommand():
    triggercommand1.configure(text="ADDTRIGGER 0 {},{} -1".format(entryMap1.get(), entryCellout2.get()))
    triggercommand2.configure(text="ADDTRIGGER 0 {},{} -1".format(entryMap2.get(), entryCellout1.get()))

def copy1():
    mainwindow.clipboard_clear()
    a = triggercommand1.cget("text")
    mainwindow.clipboard_append(a)

def copy2():
    mainwindow.clipboard_clear()
    a = triggercommand2.cget("text")
    mainwindow.clipboard_append(a)

# ======================================================================
# == GUI

mainwindow = Tk()
mainwindow.title("Trigger Generator")
mainwindow.geometry("350x250")
mainwindow.iconbitmap('favicon.ico')

# == Description Labes

descriptionLabe1 = Label(mainwindow,text="Map ID", justify ="left")
descriptionLabe1.grid(column=1, row=0,padx=2 ,pady=5)

descriptionLabe2 = Label(mainwindow,text="Cell out", justify ="left")
descriptionLabe2.grid(column=2, row=0,padx=2 ,pady=5)

descriptionLabe1 = Label(mainwindow,text="Map 1", justify ="left")
descriptionLabe1.grid(column=0, row=1,padx=10 ,pady=2)

descriptionLabe1 = Label(mainwindow,text="Map 2", justify ="left")
descriptionLabe1.grid(column=0, row=2,padx=10 ,pady=2)

# == Entrys

entryMap1 = Entry(mainwindow)
entryMap1.grid(column=1, row=1,padx=2 ,pady=2)

entryCellout1 = Entry(mainwindow)
entryCellout1.grid(column=2, row=1,padx=2 ,pady=2)

entryMap2 = Entry(mainwindow)
entryMap2.grid(column=1, row=2,padx=2 ,pady=2)

entryCellout2 = Entry(mainwindow)
entryCellout2.grid(column=2, row=2,padx=2 ,pady=2)

# == Reading Button

readingButton = Button(mainwindow,text="Reading", width=10, height=1, command=generatorCommand)
readingButton.grid(column=1, row=3,padx=5 ,pady=20, sticky='nw')

copyButton1 = Button(mainwindow,text="Copy", width=5, height=1, command=copy1)
copyButton1.grid(column=0, row=4,padx=1 ,pady=1, sticky='se')

copyButton2 = Button(mainwindow,text="Copy", width=5, height=1, command=copy2)
copyButton2.grid(column=0, row=5,padx=1 ,pady=1, sticky='ne')

# == Trigger Command

triggercommand1 = Label(mainwindow, text="empty")
triggercommand1.grid(column=1, row=4,padx=1 ,pady=1, sticky='w')

triggercommand2 = Label(mainwindow, text="empty")
triggercommand2.grid(column=1, row=5,padx=1 ,pady=1, sticky='w')

mainwindow.mainloop()

# ======================================================================