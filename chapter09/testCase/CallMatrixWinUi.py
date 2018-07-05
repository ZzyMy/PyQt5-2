import sys
from PyQt5.QtWidgets import *
from Ui_MatrixWinUi import Ui_MatrixWin

class CallMatrixWinUi(QWidget):
    def __init__(self, parent=None):
        super(CallMatrixWinUi, self).__init__(parent)
        self.ui = Ui_MatrixWin()
        self.ui.setupUi(self)
        self.initUi()
    
    #初始化窗口
    def initUi(self):
        scrollVal = self.ui.tequilaScrollBar.value()
        self.ui.selScrollBarLbl.setText(str(scrollVal))
        sliderVal = self.ui.iceHorizontalSlider.value()
        self.ui.selIceSliderLbl.setText(str(sliderVal))
        
    #获得一个量酒器的重量，单位：克
    def getJiggers(self):
        jiggersTequila = self.ui.tequilaScrollBar.value()
        jiggersIce = self.ui.iceHorizontalSlider.value()
        jiggersTripleSec = self.ui.tripleSecSpinBox.value()
        jiggersLimeJuice = float(self.ui.limeJuiceLineEdit.text())
        return jiggersTequila + jiggersTripleSec + jiggersLimeJuice + jiggersIce
    
    #获得量酒器的体积，单位：升
    def getLiters(self):
        #返回鸡尾酒的总容量（升）
        return 0.0444*self.getJiggers()
    
    #获得搅拌速度
    def getSpeedName(self):
        speedButton = self.ui.speedButtonGroup.checkedButton()
        if speedButton is None:
            return None
        return speedButton.text()
    
    #单击"OK"按钮后，把响应的结果显示在resultText文本框里
    def uiAccept(self):
        print('*CallMatrixWinUi accept*')
        print('The volume of drinks is {0} liters({1} jiggers).'.format(self.getLiters(), self.getJiggers()))
        print('The blender is running at speed "{0}".'.format(self.getSpeedName()))
        msg1= '饮料量为：{0}升({1}个量酒器)。'.format(self.getLiters(), self.getJiggers())
        msg2='调酒器的搅拌速度是："{0}"。'.format(self.getSpeedName())
        self.ui.resultText.clear()
        self.ui.resultText.append(msg1)
        self.ui.resultText.append(msg2)
    
    #单击"Cancel"按钮，关闭窗口。
    def uiReject(self):
        print('*CallMatrixWinUi reject*')
        #Cancel.
        self.close()
    
    #单击清除按钮，清空操作结果。
    def uiClear(self):
        print('*CallMatrixWinUi uiClear*')
        self.ui.resultText.clear()
    
    def uiScrollBarValueChanged(self):
        print('*uiScrollBarValueChanged----*')
        pos = self.ui.tequilaScrollBar.value()
        self.ui.selScrollBarLbl.setText(str(pos))
    
    def uiIceSliderValueChanged(self):
        print('* uiIceSliderValueChanged----*')
        pos = self.ui.iceHorizontalSlider.value()
        self.ui.selIceSliderLbl.setText(str(pos))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CallMatrixWinUi()
    demo.show()
    sys.exit(app.exec())
