# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_quickdraw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuickDraw(object):
    def setupUi(self, QuickDraw):
        QuickDraw.setObjectName("QuickDraw")
        QuickDraw.resize(399, 275)
        self.gridLayout = QtWidgets.QGridLayout(QuickDraw)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(QuickDraw)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.exampleComboBox = QtWidgets.QComboBox(QuickDraw)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exampleComboBox.sizePolicy().hasHeightForWidth())
        self.exampleComboBox.setSizePolicy(sizePolicy)
        self.exampleComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exampleComboBox.setObjectName("exampleComboBox")
        self.exampleComboBox.addItem("")
        self.exampleComboBox.addItem("")
        self.exampleComboBox.addItem("")
        self.exampleComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.exampleComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 2, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QuickDraw)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 13, 0, 1, 1)
        self.geometryTextEdit = QtWidgets.QPlainTextEdit(QuickDraw)
        self.geometryTextEdit.setEnabled(True)
        self.geometryTextEdit.setStatusTip("")
        self.geometryTextEdit.setPlainText("")
        self.geometryTextEdit.setObjectName("geometryTextEdit")
        self.gridLayout.addWidget(self.geometryTextEdit, 9, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(QuickDraw)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.zoomCheckBox = QtWidgets.QCheckBox(QuickDraw)
        self.zoomCheckBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zoomCheckBox.setChecked(True)
        self.zoomCheckBox.setObjectName("zoomCheckBox")
        self.horizontalLayout.addWidget(self.zoomCheckBox)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 0, 1, 1)

        self.retranslateUi(QuickDraw)
        self.buttonBox.accepted.connect(QuickDraw.accept)
        self.buttonBox.rejected.connect(QuickDraw.reject)
        QtCore.QMetaObject.connectSlotsByName(QuickDraw)

    def retranslateUi(self, QuickDraw):
        _translate = QtCore.QCoreApplication.translate
        QuickDraw.setWindowTitle(_translate("QuickDraw", "QuickDraw"))
        self.label.setText(_translate("QuickDraw", "Enter geometries and/or choose examples: "))
        self.exampleComboBox.setToolTip(_translate("QuickDraw", "<html><head/><body><p>These are example geometries which can be edited after selecting them</p></body></html>"))
        self.exampleComboBox.setItemText(0, _translate("QuickDraw", "Bounding box"))
        self.exampleComboBox.setItemText(1, _translate("QuickDraw", "Point"))
        self.exampleComboBox.setItemText(2, _translate("QuickDraw", "Line"))
        self.exampleComboBox.setItemText(3, _translate("QuickDraw", "Polygon"))
        self.geometryTextEdit.setToolTip(_translate("QuickDraw", "<html><head/><body><p>Enter your geometries here. </p><p>Use the <span style=\" font-weight:600;\">What\'s This? </span>tool for more information.</p></body></html>"))
        self.geometryTextEdit.setWhatsThis(_translate("QuickDraw", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; text-decoration: underline;\">Editing Geometries</span></p><p>Enter and edit your geometries here. Geometries can be input as <span style=\" font-weight:600;\">points</span>, <span style=\" font-weight:600;\">polylines</span>, <span style=\" font-weight:600;\">polygons</span> and <span style=\" font-weight:600;\">bounding boxes</span> in the following formats:</p><p><span style=\" font-weight:600;\">Points: </span><span style=\" font-style:italic;\">x,y</span><br/><span style=\" font-weight:600;\">Polylines </span>and <span style=\" font-weight:600;\">polygons: </span><span style=\" font-style:italic;\">x1,y1,x2,y2,x3,y3 etc.</span><br/><span style=\" font-weight:600;\">Bounding box: </span><span style=\" font-style:italic;\">xmin,ymin : xmax,ymax</span></p><p>Coordinates are comma separated (whitespace is ignored). It is assumed that coordinates are entered in the same <span style=\" font-weight:600;\">projection</span> as the map. </p><p>The difference between a polyline and a polygon is that in a polygon the final coordinate pair must match the initial coordinate pair, thus closing the line. Complex polygons with holes are not supported. The bounding box format is shorthand for creating a rectangular polygon, and is the same format as that used for the QGIS extents shown in the status bar.</p><p><span style=\" font-weight:600;\">Multiple geometries</span> are supported: there is one geometry per line.</p><p><span style=\" font-weight:600;\">Deleting</span> or <span style=\" font-weight:600;\">editing</span> geometries and pressing <span style=\" font-weight:600;\">OK</span> or <span style=\" font-weight:600;\">Apply </span>will update the canvas.</p></body></html>"))
        self.clearButton.setText(_translate("QuickDraw", "Clear"))
        self.zoomCheckBox.setToolTip(_translate("QuickDraw", "<html><head/><body><p>After clicking <span style=\" font-weight:600;\">OK</span> zoom the map to the combined extent of the geometries.</p></body></html>"))
        self.zoomCheckBox.setText(_translate("QuickDraw", "Zoom to geometries"))

