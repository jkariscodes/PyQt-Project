"""
/***************************************************************************
Name                 : Widget with buttons
Description          : An widget with two buttons.
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
    QDialog,
    QPushButton
)


class WidgetButton(QDialog):
    """
    This is a class for an PyQt widget with buttons.
    """

    def __init__(self, parent=None):
        super(WidgetButton, self).__init__(parent)
        self.title = 'Widget with buttons - josephkariuki.com'
        self.first_button = QPushButton(self)
        self.second_button = QPushButton(self)
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle(self.title)
        self.setGeometry(400, 400, 300, 260)
        # Set the button label text
        self.first_button.setText("Button One")
        self.second_button.setText("Button Two")
        # Set the placement of the buttons within the widget
        self.first_button.move(100, 100)
        self.second_button.move(100, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = WidgetButton()
    my_dialog.show()
    sys.exit(app.exec_())
