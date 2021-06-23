"""
/***************************************************************************
Name                 : Hello World Main Window
Description          : A window showing hello world.
Date                 : 09/October/2020
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


class HelloWorldWindow(QMainWindow):
    """
    This is a class for our Hello World PyQt application window.
    """

    def __init__(self, parent=None):
        super(HelloWorldWindow, self).__init__(parent)
        # Setting the window title
        self.setWindowTitle("Main window - josephkariuki.com")
        # Setting the width of window
        self.setFixedWidth(500)


app = QApplication(sys.argv)
my_dialog = HelloWorldWindow()
my_dialog.show()
sys.exit(app.exec_())
