'''

'''

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        #        setGeometry Parameters: starting point x, starting point y, width, height
        self.setGeometry(50, 100, 800, 600)
        #        sets initial size of window
        #        self.Title titles the window
        self.setWindowTitle("Inventory Database")
        #        self.setWindowIcon(QtGui.QIcon('Linecons_database.svg.png'))

        label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('background.jpg')
        label.setPixmap(pixmap)
        # Puts picture as background

        label.setScaledContents(True)
        # Scales picture to original Window size
        label.move(50, 0)
        label.resize(800, 600)

        self.tabs = QtWidgets.QTabWidget()
        self.tabs.resize(300, 200)

        self.tab1 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tab2 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab2, "Tab 2")

        self.centralwidget = self
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(0, 0, 150, 600)
        # self.frame.resize(300,300)
        self.frame.setStyleSheet("background-color: rgb(105,105,105)")

        extractAction = QtWidgets.QAction("&Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        self.home()

    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        # btn.resize()
        btn.move(700, 550)

        self.show()

    def close_application(self):
        print("Closed")
        sys.exit()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
