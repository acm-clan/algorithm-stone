from PyQt5 import QtWidgets
import sys

AlgoFontSize = 24
AlgoFontSizeScaleBig = 1.5
AlgoFontSizeScaleNormal = 1.0
AlgoFontSizeScaleSmall = 0.5
AlgoFontSizeScaleVerySmall = 0.3

AlgoFontName = "Microsoft YaHei"
AlgoSerifFontName = "Source Han Serif CN"
AlgoSansSerifFontName = "Source Han Sans CN"
AlgoMonoFontName = "Consolas"

def screenScale():
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    scale = screen.logicalDotsPerInch()/96.0
    return scale

AlgoScreenScale = screenScale()


