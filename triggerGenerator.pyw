import tkinter as tk
from tkinter import ttk

# ======================================================================
# == magic

def frame1GeneratorCommand():
    triggercommand1.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(F1EntryMap1.get(), F1EntryCellin1.get(), F1EntryMap2.get(),F1EntryCellout2.get()))
    triggercommand2.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(F1EntryMap2.get(), F1EntryCellin2.get(), F1EntryMap1.get(),F1EntryCellout1.get()))

def frame2GeneratorCommand():
    triggercommand3.configure(text="REPLACE INTO`cestra_game`.`scripted_cells` (`MapID`, `CellID`, `ActionID`, `EventID`, `ActionsArgs`, `Conditions`) VALUES ('{}', '{}', '0', '1', '{},{}', '-1');".format(F2EntryMap1.get(), F2EntryCellin1.get(), F2EntryMap2.get(),F2EntryCellout2.get()))

def frame1Copy1():
    frame1.clipboard_clear()
    a = triggercommand1.cget("text")
    frame1.clipboard_append(a)

def frame1Copy2():
    frame1.clipboard_clear()
    a = triggercommand2.cget("text")
    frame1.clipboard_append(a)

def frame2Copy():
    frame2.clipboard_clear()
    a = triggercommand3.cget("text")
    frame2.clipboard_append(a)

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

# ======================================================================
# == Description Labes == Frame 1

descriptionLabe1 = tk.Label(frame1,text="MAP-ID")
descriptionLabe1.grid(column=1, row=0,padx=2 ,pady=5, sticky="s")

descriptionLabe2 = tk.Label(frame1,text="Cell-IN")
descriptionLabe2.grid(column=2, row=0,padx=2 ,pady=5)

descriptionLabe3 = tk.Label(frame1,text="Cell-OUT")
descriptionLabe3.grid(column=3, row=0,padx=2 ,pady=5)

descriptionLabe4 = tk.Label(frame1,text="Map 1")
descriptionLabe4.grid(column=0, row=1,padx=10 ,pady=2)

descriptionLabe5 = tk.Label(frame1,text="Map 2")
descriptionLabe5.grid(column=0, row=2,padx=10 ,pady=2)

# == Description Labes == Frame 2

descriptionLabe1 = tk.Label(frame2,text="Map ID", font="Helvetica 10 bold", fg="#6699cc",)
descriptionLabe1.grid(column=1, row=0,padx=2 ,pady=2, sticky="s")

descriptionLabe2 = tk.Label(frame2,text="Cell IN", font="Helvetica 10 bold", fg="#ff6633")
descriptionLabe2.grid(column=3, row=1,padx=2 ,pady=2)

descriptionLabe3 = tk.Label(frame2,text="Cell OUT", font="Helvetica 10 bold", fg="#ff9933")
descriptionLabe3.grid(column=3, row=2,padx=2 ,pady=2)

descriptionLabe4 = tk.Label(frame2,text="Map 1", font="Helvetica 10")
descriptionLabe4.grid(column=0, row=1,padx=10 ,pady=2)

descriptionLabe5 = tk.Label(frame2,text="Map 2", font="Helvetica 10")
descriptionLabe5.grid(column=0, row=2,padx=10 ,pady=2)

# ======================================================================
# == Entrys == Frame 1

F1EntryMap1 = tk.Entry(frame1)
F1EntryMap1.grid(column=1, row=1,padx=2 ,pady=2)

F1EntryCellin1 = tk.Entry(frame1)
F1EntryCellin1.grid(column=2, row=1,padx=2 ,pady=2)

F1EntryCellout1 = tk.Entry(frame1)
F1EntryCellout1.grid(column=3, row=1,padx=2 ,pady=2)

F1EntryMap2 = tk.Entry(frame1)
F1EntryMap2.grid(column=1, row=2,padx=2 ,pady=2)

F1EntryCellin2 = tk.Entry(frame1)
F1EntryCellin2.grid(column=2, row=2,padx=2 ,pady=2)

F1EntryCellout2 = tk.Entry(frame1)
F1EntryCellout2.grid(column=3, row=2,padx=2 ,pady=2)

# == Entrys == Frame 2

F2EntryMap1 = tk.Entry(frame2, width=10, bg="#6699cc")
F2EntryMap1.grid(column=1, row=1,padx=2 ,pady=2)

F2EntryCellin1 = tk.Entry(frame2, width=10, bg="#ff6633")
F2EntryCellin1.grid(column=2, row=1,padx=2 ,pady=2)

F2EntryMap2 = tk.Entry(frame2, width=10, bg="#6699cc")
F2EntryMap2.grid(column=1, row=2,padx=2 ,pady=2)

F2EntryCellout2 = tk.Entry(frame2, width=10, bg="#ff9933")
F2EntryCellout2.grid(column=2, row=2,padx=2 ,pady=2)

# ======================================================================
# == Reading Button  == Frame 1

readingButton = tk.Button(frame1,text="Reading", width=10, height=1, command=frame1GeneratorCommand)
readingButton.grid(column=1, row=3,padx=5 ,pady=20, sticky='nw')

# == Reading Button  == Frame 2

readingButton = tk.Button(frame2,text="Reading", width=10, height=1, command=frame2GeneratorCommand)
readingButton.grid(column=1, row=3,padx=5 ,pady=20, sticky='nw')

# ======================================================================
# == Coyp Button == Frame 1

copyButton1 = tk.Button(frame1,text="Copy Map 1", command=frame1Copy1)
copyButton1.grid(column=2, row=3, sticky='e')

copyButton2 = tk.Button(frame1,text="Copy Map 2", command=frame1Copy2)
copyButton2.grid(column=3, row=3, sticky='w')

# == Coyp Button == Frame 2

copyButton1 = tk.Button(frame2,text="Copy Trigger", command=frame2Copy)
copyButton1.grid(column=3, row=3, sticky='e')

# ======================================================================
# == Trigger Commands == Frame 1

triggercommand1 = tk.Label(frame1, text="empty")
triggercommand2 = tk.Label(frame1, text="empty")

# == Trigger Commands == Frame 2
triggercommand3 = tk.Label(frame2, text="empty")

# ======================================================================
# == Mainloop

tk.mainloop()

# ======================================================================