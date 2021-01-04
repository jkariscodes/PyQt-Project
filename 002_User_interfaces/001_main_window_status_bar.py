"""
/***************************************************************************
Name                 : Main window with status bar
Description          : Window containing a status bar.
Date                 : 17/October/2020
copyright            : (C) 2020 by Joseph Kariuki
email                : joehene@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow
)


class WindowStatusBar(QMainWindow):
    """
    This is a class for an PyQt application window.
    """

    def __init__(self, parent=None):
        super(WindowStatusBar, self).__init__(parent)
        self.title = 'Main window and status bar - josephkariuki.com'
        self.left = 100
        self.top = 150
        self.width = 450
        self.height = 280
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface wnd widgets.
        """
        # Set the window title
        self.setWindowTitle(self.title)
        # Set the size of the window
        self.setGeometry(
            self.left,
            self.top,
            self.width,
            self.height
        )
        # Status bar message
        self.statusBar().showMessage('This is a status bar message.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = WindowStatusBar()
    my_dialog.show()
    sys.exit(app.exec_())
