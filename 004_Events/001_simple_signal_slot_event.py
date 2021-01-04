"""
/***************************************************************************
Name                 : Signals and Slots
Description          : Events using PyQt signals and slots.
Date                 : 04/January/2020
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
    QWidget,
    QFormLayout,
    QPushButton,
    QMessageBox,
    QHBoxLayout
)


class SignalAndSlot(QWidget):
    def __init__(self, parent=None):
        super(SignalAndSlot, self).__init__(parent)
        self.title = 'Signals and Slots - josephkariuki.com'
        self.first_button = QPushButton(text="Button1")
        self.second_button = QPushButton(text="Button2")
        self.third_button = QPushButton(text="Button3")
        # Connecting the signals to their corresponding slots
        self.first_button.clicked.connect(self.on_first_button_click)
        self.second_button.clicked.connect(self.on_second_button_click)
        self.third_button.clicked.connect(self.on_third_button_click)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(400, 400, 300, 260)
        h_layout = QHBoxLayout()
        # Add controls in layout
        h_layout.addWidget(self.first_button)
        h_layout.addWidget(self.second_button)
        h_layout.addWidget(self.third_button)
        self.setLayout(h_layout)

    def on_first_button_click(self):
        """
        Slot raised when the first button is clicked.
        """
        QMessageBox.information(
            self,
            "Message",
            "Button 1 has been clicked."
        )

    def on_second_button_click(self):
        """
        Slot raised when second button is clicked.
        """
        QMessageBox.information(
            self,
            "Message",
            "Button 2 has been clicked."
        )

    def on_third_button_click(self):
        """
        Slot raised when third button is clicked.
        """
        QMessageBox.information(
            self,
            "Message",
            "Button 3 has been clicked."
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = SignalAndSlot()
    my_dialog.show()
    sys.exit(app.exec_())
