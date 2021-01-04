"""
/***************************************************************************
Name                 : Multiple Tab Widgets
Description          : An widget with multiple tabs.
Date                 : 04/January/2021
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
    QCheckBox,
    QRadioButton,
    QComboBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class TabWidget(QWidget):
    """
    This is a class for an PyQt widget with multiple tabs.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widgets - josephkariuki.com")
        self.resize(300, 130)

        # Vertical box layout
        self.v_layout = QVBoxLayout()
        # Setting the top level layout
        self.setLayout(self.v_layout)

        # Tab widget with 3 tabs
        tabs = QTabWidget()
        tabs.addTab(self.tab_one(), "Tab1")
        tabs.addTab(self.tab_two(), "Tab2")
        tabs.addTab(self.tab_three(), "Tab3")
        self.v_layout.addWidget(tabs)

    def tab_one(self):
        """
        Create a first tab user interface.
        """
        tab_one = QWidget()
        v1_layout = QVBoxLayout()
        v1_layout.addWidget(QRadioButton("Radio button 1"))
        v1_layout.addWidget(QRadioButton("Radio button 2"))
        tab_one.setLayout(v1_layout)
        return tab_one

    def tab_two(self):
        """
        Creates a second tab user interface.
        """
        tab_two = QWidget()
        v2_layout = QVBoxLayout()
        v2_layout.addWidget(QCheckBox("Checkbox 1"))
        v2_layout.addWidget(QCheckBox("Checkbox 2"))
        tab_two.setLayout(v2_layout)
        return tab_two

    def tab_three(self):
        """
        Creates a third tab user interface.
        """
        tab_three = QWidget()
        v3_layout = QVBoxLayout()
        combo_box = QComboBox()
        combo_box.addItems(["Item 1", "Item 2", "Item 3"])
        v3_layout.addWidget(combo_box)
        tab_three.setLayout(v3_layout)
        return tab_three


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TabWidget()
    window.show()
    sys.exit(app.exec_())
