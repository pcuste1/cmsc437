from Tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple menu")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New", command=self.onNew)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Print", command=self.onPrint)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        enterMenu = Menu(menubar)
        enterMenu.add_command(label="Easy", command=self.onEasy)
        enterMenu.add_command(label="Complete", command=self.onComplete)
        menubar.add_cascade(label="Enter", menu=enterMenu)

    def onNew(self):
        print("do New")

    def onOpen(self):
        print("do Open")

    def onPrint(self):
        print("do Print")

    def onExit(self):
        self.quit()

    def onEasy(self):
        print("do Easy")

    def onComplete(self):
        print("do Complete")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
    
if __name__=='__main__':
    main()