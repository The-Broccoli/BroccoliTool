from tkinter import *

# ======================================================================
# == FONCTIONS

def generatorCommand():
    triggercommand1.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(entryMap1.get(), entryCellin1.get(), entryMap2.get(),entryCellout2.get()))
    triggercommand2.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(entryMap2.get(), entryCellin2.get(), entryMap1.get(),entryCellout1.get()))

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
mainwindow.geometry("455x250")
mainwindow.iconbitmap('favicon.ico')
# fixed size
mainwindow.resizable(width=False, height=False)

# == Description Labes

descriptionLabe1 = Label(mainwindow,text="MAP-ID", justify ="left")
descriptionLabe1.grid(column=1, row=0,padx=2 ,pady=5)

descriptionLabe2 = Label(mainwindow,text="Cell-IN", justify ="left")
descriptionLabe2.grid(column=2, row=0,padx=2 ,pady=5)

descriptionLabe2 = Label(mainwindow,text="Cell-OUT", justify ="left")
descriptionLabe2.grid(column=3, row=0,padx=2 ,pady=5)

descriptionLabe1 = Label(mainwindow,text="Map 1", justify ="left")
descriptionLabe1.grid(column=0, row=1,padx=10 ,pady=2)

descriptionLabe1 = Label(mainwindow,text="Map 2", justify ="left")
descriptionLabe1.grid(column=0, row=2,padx=10 ,pady=2)

# == Entrys

entryMap1 = Entry(mainwindow)
entryMap1.grid(column=1, row=1,padx=2 ,pady=2)

entryCellin1 = Entry(mainwindow)
entryCellin1.grid(column=2, row=1,padx=2 ,pady=2)

entryCellout1 = Entry(mainwindow)
entryCellout1.grid(column=3, row=1,padx=2 ,pady=2)

entryMap2 = Entry(mainwindow)
entryMap2.grid(column=1, row=2,padx=2 ,pady=2)

entryCellin2 = Entry(mainwindow)
entryCellin2.grid(column=2, row=2,padx=2 ,pady=2)

entryCellout2 = Entry(mainwindow)
entryCellout2.grid(column=3, row=2,padx=2 ,pady=2)

# == Reading Button

readingButton = Button(mainwindow,text="Reading", width=10, height=1, command=generatorCommand)
readingButton.grid(column=1, row=3,padx=5 ,pady=20, sticky='nw')

copyButton1 = Button(mainwindow,text="Copy", width=5, height=1, command=copy1)
copyButton1.place(x=12, y=150)

copyButton2 = Button(mainwindow,text="Copy", width=5, height=1, command=copy2)
copyButton2.place(x=12, y=180)

# == Trigger Command

triggercommand1 = Label(mainwindow, text="empty")
triggercommand1.place(x=64, y=153, width=380, height=20)

triggercommand2 = Label(mainwindow, text="empty")
triggercommand2.place(x=64, y=183, width=380, height=20)

mainwindow.mainloop()

# ======================================================================