"""
/***************************************************************************
Name                 : Hello World Widget
Description          : Widget for showing hello world.
Date                 : 08/October/2020
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
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel
)

import sys


class HelloWorldWdgt(QWidget):
    """
    This is a class for our Hello World PyQt application widget.
    """

    def __init__(self, parent=None):
        super(HelloWorldWdgt, self).__init__(parent)
        # Setting the dialog title
        self.setWindowTitle("Hello World - josephkariuki.com")
        self.setFixedWidth(400)
        # Setting the layout to vertical box layout.
        self.layout = QVBoxLayout()
        # Creating a label with hello world text.
        self.label = QLabel("Hello World! This is a PyQt widget.")
        # Creating a line edit
        self.layout.addWidget(self.label)
        # Setting the layout
        self.setLayout(self.layout)


app = QApplication(sys.argv)
my_widget = HelloWorldWdgt()
my_widget.show()
sys.exit(app.exec_())
