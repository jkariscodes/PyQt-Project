"""
/***************************************************************************
Name                 : Empty widget
Description          : An empty widget.
Date                 : 19/December/2020
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
    QWidget
)


class TheWidget(QWidget):
    """
    This is a class for an PyQt widget.
    """

    def __init__(self, parent=None):
        super(TheWidget, self).__init__(parent)
        self.title = 'Widget - josephkariuki.com'
        self.left = 150
        self.top = 150
        self.width = 380
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = TheWidget()
    my_dialog.show()
    sys.exit(app.exec_())
