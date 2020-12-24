"""
/***************************************************************************
Name                 : Form layout of controls
Description          : Dialog widgets arranged in form layout.
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
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QFormLayout
)


class FormLayout(QDialog):
    """
    Form layout.
    """

    def __init__(self, parent=None):
        super(FormLayout, self).__init__(parent)
        self.title = 'Form layout - josephkariuki.com'
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle(self.title)
        self.setGeometry(400, 400, 300, 260)
        self.form_layout()

    def form_layout(self):
        """
        Create form layout.
        """
        f_layout = QFormLayout()
        # Set the button label text
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        # Add rows in form layout
        f_layout.addRow(QLabel("First Name:"), QLineEdit())
        f_layout.addRow(QLabel("Last Name:"), QLineEdit())
        f_layout.addRow(QLabel("Email:"), QLineEdit())
        f_layout.addRow(button_box)
        self.setLayout(f_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_dialog = FormLayout()
    my_dialog.show()
    sys.exit(app.exec_())
