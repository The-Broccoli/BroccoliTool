import tkinter as tk
from tkinter import ttk

# ======================================================================
# == FONCTIONS

def generatorCommand():
    triggercommand1.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(entryMap1.get(), entryCellin1.get(), entryMap2.get(),entryCellout2.get()))
    triggercommand2.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(entryMap2.get(), entryCellin2.get(), entryMap1.get(),entryCellout1.get()))

def copy1():
    frame1.clipboard_clear()
    a = triggercommand1.cget("text")
    frame1.clipboard_append(a)

def copy2():
    frame1.clipboard_clear()
    a = triggercommand2.cget("text")
    frame1.clipboard_append(a)

# ======================================================================
# == GUI

tkTop = tk.Tk()
tkTop.title("Trigger Generator")
tkTop.geometry('465x210')
tkTop.iconbitmap('favicon.ico')
tkTop.resizable(width=False, height=False)
 
notebook = ttk.Notebook(tkTop)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='    Map to Map    ')
notebook.add(frame2, text='    Singel Map    ')
notebook.place(x=10, y=10)

tkLabelTop = tk.Label(tkTop, text="BroccoliTool 0.2 - https://github.com/The-Broccoli")
tkLabelTop.place(x=10, y=185)

# == Description Labes

descriptionLabe1 = tk.Label(frame1,text="MAP-ID")
descriptionLabe1.grid(column=1, row=0,padx=2 ,pady=5, sticky="s")

descriptionLabe2 = tk.Label(frame1,text="Cell-IN")
descriptionLabe2.grid(column=2, row=0,padx=2 ,pady=5)

descriptionLabe2 = tk.Label(frame1,text="Cell-OUT")
descriptionLabe2.grid(column=3, row=0,padx=2 ,pady=5)

descriptionLabe1 = tk.Label(frame1,text="Map 1")
descriptionLabe1.grid(column=0, row=1,padx=10 ,pady=2)

descriptionLabe1 = tk.Label(frame1,text="Map 2")
descriptionLabe1.grid(column=0, row=2,padx=10 ,pady=2)

# == Entrys

entryMap1 = tk.Entry(frame1)
entryMap1.grid(column=1, row=1,padx=2 ,pady=2)

entryCellin1 = tk.Entry(frame1)
entryCellin1.grid(column=2, row=1,padx=2 ,pady=2)

entryCellout1 = tk.Entry(frame1)
entryCellout1.grid(column=3, row=1,padx=2 ,pady=2)

entryMap2 = tk.Entry(frame1)
entryMap2.grid(column=1, row=2,padx=2 ,pady=2)

entryCellin2 = tk.Entry(frame1)
entryCellin2.grid(column=2, row=2,padx=2 ,pady=2)

entryCellout2 = tk.Entry(frame1)
entryCellout2.grid(column=3, row=2,padx=2 ,pady=2)

# == Reading Button

readingButton = tk.Button(frame1,text="Reading", width=10, height=1, command=generatorCommand)
readingButton.grid(column=1, row=3,padx=5 ,pady=20, sticky='nw')

# == Coyp Button

copyButton1 = tk.Button(frame1,text="Copy Map 1", command=copy1)
copyButton1.grid(column=2, row=3, sticky='e')

copyButton2 = tk.Button(frame1,text="Copy Map 2", command=copy2)
copyButton2.grid(column=3, row=3, sticky='w')

# == Trigger Commands

triggercommand1 = tk.Label(frame1, text="empty")
triggercommand2 = tk.Label(frame1, text="empty")

# == Mainloop

tk.mainloop()

# ======================================================================