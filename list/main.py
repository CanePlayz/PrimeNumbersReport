import list.utilities as listUtils

def openListWindow ():
    listUtils.createListWindow ()
    listUtils.printListOnWindow ()
    listUtils.createButtonToCloseList ()
    listUtils.createButtonForFile ()
    listUtils.listWindow.mainloop ()