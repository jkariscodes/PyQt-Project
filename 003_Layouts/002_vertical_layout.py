"""
/***************************************************************************
Name                 : Vertical layout of controls
Description          : Dialog widgets arranged in vertical layout.
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
    QVBoxLayout
)


class VLayout(QDialog):
    """
    Vertical layout.
    """

    def __init__(self, parent=None):
        super(VLayout, self).__init__(parent)
        self.title = 'Vertical layout - josephkariuki.com'
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
        self.vertical_layout()
        # Set the button label text
        self.first_button.setText("One")
        self.second_button.setText("Two")
        self.third_button.setText("Three")

    def vertical_layout(self):
        """
        Create vertical layout.
        """
        v_layout = QVBoxLayout()
        # Add controls in layout
        v_layout.addWidget(self.first_button)
        v_layout.addWidget(self.second_button)
        v_layout.addWidget(self.third_button)
        self.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = VLayout()
    my_dialog.show()
    sys.exit(app.exec_())
