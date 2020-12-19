"""
/***************************************************************************
Name                 : Empty dialog
Description          : An empty dialog.
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
    QDialog
)


class TheDialog(QDialog):
    """
    This is a class for an PyQt dialog.
    """

    def __init__(self, parent=None):
        super(TheDialog, self).__init__(parent)
        self.title = 'Dialog - josephkariuki.com'
        self.left = 200
        self.top = 250
        self.width = 400
        self.height = 300
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        # Set the dialog title
        self.setWindowTitle(self.title)
        # Set the size of the dialog
        self.setGeometry(
            self.left,
            self.top,
            self.width,
            self.height
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = TheDialog()
    my_dialog.show()
    sys.exit(app.exec_())
