import tkinter as tk
from tkinter import filedialog as fd

import report.utilities as reportUtils


def createListWindow():
    global listWindow
    listWindow = tk.Tk()
    listWindow.title("Prime Numbers List")
    listWindow.geometry("800x600")
    listWindow.resizable(False, False)

    labelList = tk.Label(master=listWindow,
                         text="Prime Numbers from 1 to " +
                         str(reportUtils.limit),
                         background="gray")
    labelList.place(x=10,
                    y=10,
                    width=780,
                    height=30)


def printListOnWindow():
    textList = tk.Text(master=listWindow)
    textList.place(x=10,
                   y=50,
                   width=780,
                   height=500)
    textList.insert(tk.END, str(reportUtils.primes))


def createButtonToCloseList():
    def close():
        listWindow.destroy()

    buttonClose = tk.Button(master=listWindow,
                            text="Close List",
                            command=close)
    buttonClose.place(x=10,
                      y=560,
                      width=160,
                      height=30)


def createButtonForFile():
    def getListAsFile():
        file = fd.asksaveasfile(defaultextension=".txt")
        if file is None:
            return
        file.write(str(reportUtils.primes))
        file.close()

    buttonGetListAsFile = tk.Button(master=listWindow,
                                    text="Save List as File",
                                    command=getListAsFile)

    buttonGetListAsFile.place(x=630,
                              y=560,
                              width=160,
                              height=30)
