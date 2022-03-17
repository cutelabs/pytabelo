# This Python file uses the following encoding: utf-8
#
# Copyright 2022 naracanto <https://naracanto.github.io>.
#
# This file is part of Tabelo-QtPy <https://github.com/tabelolabs/tabelo-qtpy>.
#
# Tabelo-QtPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tabelo-QtPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tabelo-QtPy.  If not, see <https://www.gnu.org/licenses/>.
#

from PySide2.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout


class PreferencesDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setMinimumSize(800, 600)
        self.setWindowTitle(self.tr("Preferences"))


        # Button box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.close)

        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.addStretch(1)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)