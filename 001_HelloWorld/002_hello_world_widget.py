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


class HelloWorld(QWidget):
    """
    This is a class for our Hello World PyQt application.
    """

    def __init__(self):
        QWidget.__init__(self)
        # Setting the dialog title
        self.setWindowTitle("Hello World application")
        self.setFixedWidth(300)
        # Setting the layout to vertical box layout.
        layout = QVBoxLayout()
        # Creating a label with hello world text.
        label = QLabel("Hello World! This is a PyQt dialog.")
        # Creating a line edit
        layout.addWidget(label)

        self.setLayout(layout)


app = QApplication(sys.argv)
my_dialog = HelloWorld()
my_dialog.show()
my_dialog.exec_()
