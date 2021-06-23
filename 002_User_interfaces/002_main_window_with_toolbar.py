"""
/***************************************************************************
Name                 : Main window with tool bar
Description          : Window containing a tool bar.
Date                 : 23/June/2021
copyright            : (C) 2021 by Joseph Kariuki
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
    QMainWindow,
    QToolBar
)


class WindowToolBar(QMainWindow):
    """
    This is a class for an PyQt application window.
    """

    def __init__(self, parent=None):
        super(WindowToolBar, self).__init__(parent)
        self.title = 'Main window with tool bar - josephkariuki.com'
        self.left = 100
        self.top = 150
        self.width = 450
        self.height = 280
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
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
        # Create a toolbar
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)
        # Add a toolbar action
        tool_bar.addAction('Exit', self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = WindowToolBar()
    my_dialog.show()
    sys.exit(app.exec_())
