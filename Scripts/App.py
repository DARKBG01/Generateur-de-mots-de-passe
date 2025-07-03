from PySide6 import QtWidgets,QtGui
from Interface import Ui_MainWindow
import qrcode
import os
from PIL import Image

print(os.getcwd())
class App(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Connection()
        self.Settings()
        #self.showMaximized()
        print(self.geometry())
        print(QtGui.QGuiApplication.primaryScreen().size())

    def Connection(self):
        self.information.textChanged.connect(self.Generate_Qrcode)
        self.path_button.clicked.connect(self.Path)
        self.save.clicked.connect(self.Save_Image)
        self.actionQuitter.triggered.connect(self.Quitter)
        self.actionA_Propos.triggered.connect(self.Help)

    def Get_Size(self):
        try:
            qr_size = Image.open("Assets/.Cache/image.png").size
            self.label_2.setText(f"{qr_size[0]} X {qr_size[1]}")
        except:
            self.label_2.setText(f"0 X 0")

    def Settings(self):
        self.information.setPlaceholderText("Entrez Votre Text ....")
        self.change_size.addItems(["100 x 100","150 x 150","200 x 200","250 x 250","300 x 300"])
        self.label_2.setText(f"0 X 0")
        self.qrcode_image.setPalette(QtGui.QColor("red"))
        #self.path.setText("/home/isclef/Bureau/Qrcode.png")


    def Generate_Qrcode(self):
        self.qrcode_image.setPalette(QtGui.QColor("red"))
        info = f"{self.information.toPlainText()}"
        if os.path.isfile("Assets/.Cache/image.png"):
            os.remove("Assets/.Cache/image.png")
            qrcode.make(data=info).save("Assets/.Cache/image.png")
        else:
            qrcode.make(data=info).save("Assets/.Cache/image.png")
            print(info)
        self.qrcode_image.clear()
        self.qrcode_image.setPixmap(QtGui.QPixmap("Assets/.Cache/image.png").scaled(460,460))
        self.Get_Size()

    def Path(self):
        self.file = QtWidgets.QFileDialog.getSaveFileName(dir="Image.png")
        self.path.setText(self.file[0])

    def Save_Image(self):
        info = f"{self.information.toPlainText()}"
        if os.path.isfile(self.file[0]):
            os.remove(self.file[0])
            qrcode.make(data=info).save(self.file[0])
        else:
            qrcode.make(data=info).save(self.file[0])

        self.qrcode_image.setPalette(QtGui.QColor(9, 243, 34))

        #msg = QtWidgets.QMessageBox()
        #msg.information(self,"Success","Enregistrer !")
        #msg.show()


        print(self.file)

    def Quitter(self):
        self.close()

    def Help(self):
        msg = QtWidgets.QMessageBox()
        msg.information(self,"Help",f"Merci d'utiliser mon logiciel\n\n {' V.1.0.0 '.center(20,'=')}")
        msg.show()


app = QtWidgets.QApplication()
app.setStyle("fusion")
win = App()
win.show()
app.exec()