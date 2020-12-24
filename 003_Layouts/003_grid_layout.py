"""
/***************************************************************************
Name                 : Grid layout of controls
Description          : Dialog widgets arranged in grid layout.
Date                 : 20/December/2020
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
    QDialog,
    QPushButton,
    QGridLayout
)


class GridLayout(QDialog):
    """
    Grid layout.
    """

    def __init__(self, parent=None):
        super(GridLayout, self).__init__(parent)
        self.title = 'Grid layout - josephkariuki.com'
        self.first_button = QPushButton(self)
        self.second_button = QPushButton(self)
        self.third_button = QPushButton(self)
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle(self.title)
        self.setGeometry(400, 400, 300, 260)
        self.grid_layout()
        # Set the button label text
        self.first_button.setText("One")
        self.second_button.setText("Two")
        self.third_button.setText("Three")

    def grid_layout(self):
        """
        Create grid layout.
        """
        g_layout = QGridLayout()
        # Add controls in layout
        g_layout.addWidget(self.first_button, 0, 0)
        g_layout.addWidget(self.second_button, 0, 1)
        g_layout.addWidget(self.third_button, 0, 2)
        # Create more buttons
        g_layout.addWidget(QPushButton("4"), 1, 0)
        g_layout.addWidget(QPushButton("5"), 1, 1)
        g_layout.addWidget(QPushButton("6"), 1, 2)
        self.setLayout(g_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = GridLayout()
    my_dialog.show()
    sys.exit(app.exec_())
