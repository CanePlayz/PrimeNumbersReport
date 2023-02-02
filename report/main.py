import utilities as reportUtils


def createReportWindow():
    reportUtils.calculateValues()
    reportUtils.createReportWindow()
    reportUtils.createButtonToExit()
    reportUtils.createButtonForList()
    reportUtils.createNewReportButton()
    reportUtils.reportWindow.mainloop()
