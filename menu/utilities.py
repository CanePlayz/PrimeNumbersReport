from tkinter import Tk, font, ttk

import report.main as mainReport


def createWindow():
    global window

    window = Tk()
    window.title("Primes Runtime Comparison")
    window.geometry("355x83")
    window.resizable(False, False)
    print("Screen height: " + str(Tk.winfo_screenheight(window)))
    print("Screen width: " + str(Tk.winfo_screenwidth(window)))


def createLabel():
    labelHeading = ttk.Label(master=window,
                             text="Calculate prime numbers up to:",
                             justify="center")

    labelHeading.place(x=10,
                       y=10,
                       width=205,
                       height=28)


def createEntry():
    global entryLimit
    entryLimit = ttk.Entry(master=window,
                           background="white")

    entryLimit.place(x=225,
                     y=10,
                     width=120,
                     height=28)


def createButtons():
    def exitProgram():
        exit()

    buttonExit = ttk.Button(master=window,
                            text="Exit",
                            command=exitProgram)

    buttonExit.place(x=10,
                     y=50,
                     width=120,
                     height=25)

    buttonReport = ttk.Button(master=window,
                              text="Generate Report",
                              command=mainReport.createReportWindow)

    buttonReport.place(x=225,
                       y=50,
                       width=120,
                       height=25)
