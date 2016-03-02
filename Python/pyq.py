import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
  
win = pg.plot()
win.setWindowTitle('pyqtgraph example: BarChart')
  
y = np.arange(1, 10)
N = len(y)
x = range(N)
  
bg1 = pg.BarGraphItem(x=x, height=y, width=0.6, brush='b')
  
win.addItem(bg1)

  
  
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()