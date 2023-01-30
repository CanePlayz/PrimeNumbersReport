import tkinter as tk

import algorithms.algorithm1 as alg1
import algorithms.algorithm2 as alg2
import algorithms.algorithm3 as alg3
import algorithms.sieve as sieve
import menu.main as menuMain
import menu.utilities as menuUtils
import list.main as listMain

def calculateValues ():
    global limit
    global time1
    global time2
    global time3
    global time4
    global primes
    limit = int (menuUtils.entryLimit.get())
    time1 = alg1.main (limit)
    time2 = alg2.main (limit)
    time3 = alg3.main (limit)
    time4 = (sieve.main (limit))[0]
    primes = (sieve.main (limit))[1]
    menuUtils.window.destroy ()

def createReportWindow ():
    global reportWindow

    reportWindow = tk.Tk ()
    reportWindow.title ("Report")
    reportWindow.geometry ("790x250")
    reportWindow.resizable (False, False)


    ## HEADINGS

    labelHeading = tk.Label (master = reportWindow,
                              text = "Here's Your Report",
                              background = "light blue")
    labelHeading.place (x = 10,
                        y = 10,
                        width = 770,
                        height = 30)

    labelAlgorithms = tk.Label (master = reportWindow,
                                 text = "Algorithm",
                                 background = "Gray")
    labelAlgorithms.place (x = 10,
                           y = 50,
                           width = 120,
                           height = 30)

    labelAlgorithm1 = tk.Label (master = reportWindow,
                                 text = "Algorithm 1",
                                 background = "#FF9999")
    labelAlgorithm1.place (x = 140,
                           y = 50,
                           width = 120,
                           height = 30)

    labelAlgorithm2 = tk.Label (master = reportWindow,
                                 text = "Algorithm 2",
                                 background = "#FFD480")
    labelAlgorithm2.place (x = 270,
                           y = 50,
                           width = 120,
                           height = 30)

    labelAlgorithm3 = tk.Label (master = reportWindow,
                                 text = "Algorithm 3",
                                 background = "#FFE473")
    labelAlgorithm3.place (x = 400,
                           y = 50,
                           width = 120,
                           height = 30)

    labelSieve = tk.Label (master = reportWindow,
                            text = "Sieve",
                            background = "light green")
    labelSieve.place (x = 530,
                      y = 50,
                      width = 120,
                      height = 30)

    labelAverageTotal = tk.Label (master = reportWindow,
                                   text = "Average",
                                   background = "light blue")
    labelAverageTotal.place (x = 660,
                             y = 50,
                             width = 120,
                             height = 30)


    ## TIME

    labelTime = tk.Label (master = reportWindow,
                           text = "Time",
                           background = "Gray")
    labelTime.place (x = 10,
                     y = 90,
                     width = 120,
                     height = 30)

    labelAlgorithm1Time = tk.Label (master = reportWindow,
                                     text = str (round (time1, 5)) + " sec",
                                     background = "#FF9999")
    labelAlgorithm1Time.place (x = 140,
                               y = 90,
                               width = 120,
                               height = 30)

    labelAlgorithm2Time = tk.Label (master = reportWindow,
                                     text = str (round (time2, 5)) + " sec",
                                     background = "#FFD480")
    labelAlgorithm2Time.place (x = 270,
                               y = 90,
                               width = 120,
                               height = 30)

    labelAlgorithm3Time = tk.Label (master = reportWindow,
                                     text = str (round (time3, 5)) + " sec",
                                     background = "#FFE473")
    labelAlgorithm3Time.place (x = 400,
                               y = 90,
                               width = 120,
                               height = 30)

    labelSieveTime = tk.Label (master = reportWindow,
                                text = str (round (time4, 5)) + " sec",
                                background = "light green")
    labelSieveTime.place (x = 530,
                          y = 90,
                          width = 120,
                          height = 30)

    labelAverageTime = tk.Label (master = reportWindow,
                                  text = str (round (((time1 + time2 + time3 + time4) / 4), 5)) + " sec",
                                  background = "light blue")
    labelAverageTime.place (x = 660,
                            y = 90,
                            width = 120,
                            height = 30)


    ## IMPROVEMENT TO PREVIOUS ALGORITHM

    labelImprovement = tk.Label (master = reportWindow,
                                  text = "Improvement Pr.",
                                  background = "Gray")
    labelImprovement.place (x = 10,
                            y = 130,
                            width = 120,
                            height = 30)

    labelAlgorithm1Impro = tk.Label (master = reportWindow,
                                      text = "-",
                                      background = "#FF9999")
    labelAlgorithm1Impro.place (x = 140,
                                y = 130,
                                width = 120,
                                height = 30)

    labelAlgorithm2Impro = tk.Label (master = reportWindow,
                                      text = str (round (time1 - time2, 5)) + " sec",
                                      background = "#FFD480")
    labelAlgorithm2Impro.place (x = 270,
                                y = 130,
                                width = 120,
                                height = 30)

    labelAlgorithm3Impro = tk.Label (master = reportWindow,
                                      text = str (round (time2 - time3, 5)) + " sec",
                                      background = "#FFE473")
    labelAlgorithm3Impro.place (x = 400,
                                y = 130,
                                width = 120,
                                height = 30)

    labelSieveImpro = tk.Label (master = reportWindow,
                                 text = str (round (time3 - time4, 5)) + " sec",
                                 background = "light green")
    labelSieveImpro.place (x = 530,
                           y = 130,
                           width = 120,
                           height = 30)

    labelAverageImpro = tk.Label (master = reportWindow,
                                   text = str (round (((time1 - time2) + (time2 - time3) + (time3 - time4)) / 3, 5)) + " sec",
                                   background = "light blue")
    labelAverageImpro.place (x = 660,
                             y = 130,
                             width = 120,
                             height = 30)

    ## TOTAL IMPROVEMENT

    labelImprovementT = tk.Label (master = reportWindow,
                                   text = "Improvement T.",
                                   background = "Gray")
    labelImprovementT.place (x = 10,
                             y = 170,
                             width = 120,
                             height = 30)

    labelAlgorithm1ImproT = tk.Label (master = reportWindow,
                                       text = "-",
                                       background = "#FF9999")
    labelAlgorithm1ImproT.place (x = 140,
                                 y = 170,
                                 width = 120,
                                 height = 30)

    labelAlgorithm2ImproT = tk.Label (master = reportWindow,
                                       text = str (round (time1 - time2, 5)) + " sec",
                                       background = "#FFD480")
    labelAlgorithm2ImproT.place (x = 270,
                                 y = 170,
                                 width = 120,
                                 height = 30)

    labelAlgorithm3ImproT = tk.Label (master = reportWindow,
                                       text = str (round (time1 - time3, 5)) + " sec",
                                       background = "#FFE473")
    labelAlgorithm3ImproT.place (x = 400,
                                 y = 170,
                                 width = 120,
                                 height = 30)

    labelSieveImproT = tk.Label(master = reportWindow,
                                 text = str (round (time1 - time4, 5)) + " sec",
                                 background = "light green")
    labelSieveImproT.place (x = 530,
                            y = 170,
                            width = 120,
                            height = 30)

    labelAverageImproT = tk.Label (master = reportWindow,
                                    text = str (round (((time1 - time2) + (time1 - time3) + (time1 - time4)) / 3, 5)) + " sec",
                                    background = "light blue")
    labelAverageImproT.place (x = 660,
                              y = 170,
                              width = 120,
                              height = 30)

def createButtonToExit ():
    def exitProgram ():
        exit ()
    
    buttonExit = tk.Button (master = reportWindow,
                            text = "Exit",
                            command = exitProgram)
    buttonExit.place (x = 10,
                      y = 210,
                      width = 160,
                      height = 30)

def createButtonForList ():
    buttonOpenList = tk.Button (master = reportWindow,
                                 text = "See Prime Numbers",
                                 command = listMain.openListWindow)
    buttonOpenList.place (x = 315,
                          y = 210,
                          width = 160,
                          height = 30)

def createNewReportButton ():
    def newReport ():
        reportWindow.destroy ()
        menuMain.createMenu ()

    buttonNewReport = tk.Button (master = reportWindow,
                              text = "Generate New Report",
                              command = newReport)
    buttonNewReport.place (x = 620,
                           y = 210,
                           width = 160,
                           height = 30)