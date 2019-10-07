# menuTitle: Font Window
# shortCut : command + control + w

from vanilla import FloatingWindow, Button, List
from mojo.roboFont import FontsList
from mojo.events import addObserver, removeObserver
from mojo.UI import AskYesNoCancel


key = 'windowposition'


class fontWindow(object):

    def __init__(self):

        fontsList = FontsList(AllFonts())
        fontsList.sortBy('openTypeOS2WeightClass')
        self.fontList = fontsList



        padding = 10
        listHeight = 145
        width = 210
        height = 220

        addObserver(self, 'updateWindow', 'fontWillOpen')
        addObserver(self, 'updateWindow', 'fontDidClose')



        self.w = FloatingWindow((width, height), 'FontWindow', autosaveName=key)

        x = y = padding
        self.w.fonts = List (
            (x, y, width - padding*2, listHeight),
            [f.info.familyName + ' ' + f.info.styleName for f in self.fontList],
            selectionCallback=self.getFontsCallback,
            allowsMultipleSelection=False)

        self.w.buttonOpen = Button((10, -55, 90, 15), 'Open Font', sizeStyle = 'small', callback=self.openFont)
        self.w.buttonCloseFont = Button((110, -55, 90, 15), 'Close Font', sizeStyle = 'small', callback=self.closeFont)
        self.w.buttonClose = Button((110, -30, 90, 15), 'Close Window', sizeStyle = 'small', callback=self.closeWindow)

        self.w.open()


    def getFontsCallback(self, sender):
        f = AllFonts()
        selectionList = sender.getSelection()
        for i in selectionList:
            num = i
        self.requestedFont = self.fontList[num]
        activeFontWindow = self.requestedFont.document().getMainWindow()
        activeFontWindow.show()


    def updateWindow(self, sender):
        self.w.close()
        removeObserver(self, 'fontWillOpen')
        removeObserver(self, 'fontDidClose')
        fontWindow()


    def closeWindow(self, sender):
        self.w.close()
        removeObserver(self, 'fontWillOpen')
        removeObserver(self, 'fontDidClose')

    def openFont(self, sender):
        f = OpenFont()

    def closeFont(self,sender):
        askCloseFont = AskYesNoCancel('Do you want to close the font?\n Unsaved changes will be lost!')
        if askCloseFont == 1:
            closeFontWindow = self.requestedFont.document().getMainWindow()
            closeFontWindow.close()
            #####
            # f = AllFonts()
            # selectionList = sender.getSelection()
            # for i in selectionList:
            #     num = i
            # selectedFonts = self.fontList[num]
            # selectedFonts.close()
            #####


        else:
            pass


fontWindow()
