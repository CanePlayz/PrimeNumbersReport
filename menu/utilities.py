import tkinter as tk

import report.main as mainReport


def createWindow():
    global window

    window = tk.Tk()
    window.title("Primes Runtime Comparison")
    window.geometry("330x70")
    window.resizable(False, False)


def createLabel():
    labelHeading = tk.Label(master=window,
                            text="Calculate Prime Numbers up to:",
                            justify="left")

    labelHeading.place(x=10,
                       y=10,
                       width=175,
                       height=20)


def createEntry():
    global entryLimit
    entryLimit = tk.Entry(master=window,
                          background="white",
                          justify="right")

    entryLimit.place(x=200,
                     y=10,
                     width=120,
                     height=20)


def createButton():
    buttonReport = tk.Button(master=window,
                             text="Generate Report",
                             command=mainReport.createReportWindow)

    buttonReport.place(x=200,
                       y=40,
                       width=120,
                       height=20)
