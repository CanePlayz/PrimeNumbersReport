from tkinter import Tk, ttk, font
import report.main as mainReport

# import report.main as mainReport


""" class App:
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Segoe UI",
                                   size=8) """


def createWindow():
    global window

    window = Tk()
    window.title("Primes Runtime Comparison")
    window.geometry("355x83")
    window.resizable(False, False)
    # app = App(window)
    # window.option_add("*font", "Segoe UI", 20)


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
