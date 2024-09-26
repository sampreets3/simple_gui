# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_gui/simple.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.grbBoxTimerUpdateValues = QtWidgets.QGroupBox(self.centralwidget)
        self.grbBoxTimerUpdateValues.setObjectName("grbBoxTimerUpdateValues")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.grbBoxTimerUpdateValues)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_state_x = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.label_state_x.setObjectName("label_state_x")
        self.gridLayout_4.addWidget(self.label_state_x, 0, 0, 1, 1)
        self.robot_state_x = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.robot_state_x.setObjectName("robot_state_x")
        self.gridLayout_4.addWidget(self.robot_state_x, 0, 1, 1, 1)
        self.label_state_y = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.label_state_y.setObjectName("label_state_y")
        self.gridLayout_4.addWidget(self.label_state_y, 1, 0, 1, 1)
        self.robot_state_y = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.robot_state_y.setObjectName("robot_state_y")
        self.gridLayout_4.addWidget(self.robot_state_y, 1, 1, 1, 1)
        self.label_state_theta = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.label_state_theta.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_state_theta.setObjectName("label_state_theta")
        self.gridLayout_4.addWidget(self.label_state_theta, 2, 0, 1, 1)
        self.robot_state_theta = QtWidgets.QLabel(self.grbBoxTimerUpdateValues)
        self.robot_state_theta.setObjectName("robot_state_theta")
        self.gridLayout_4.addWidget(self.robot_state_theta, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.grbBoxTimerUpdateValues, 0, 3, 2, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 2, 1)
        self.grpBoxPubSub = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxPubSub.setObjectName("grpBoxPubSub")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grpBoxPubSub)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_subscriber = QtWidgets.QLabel(self.grpBoxPubSub)
        self.label_subscriber.setObjectName("label_subscriber")
        self.gridLayout_2.addWidget(self.label_subscriber, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.grpBoxPubSub)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.btn_publisher = QtWidgets.QPushButton(self.grpBoxPubSub)
        self.btn_publisher.setObjectName("btn_publisher")
        self.gridLayout_2.addWidget(self.btn_publisher, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.grpBoxPubSub, 0, 0, 1, 2)
        self.grpBoxSrvCall = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxSrvCall.setObjectName("grpBoxSrvCall")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.grpBoxSrvCall)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spinBox_num_b = QtWidgets.QSpinBox(self.grpBoxSrvCall)
        self.spinBox_num_b.setObjectName("spinBox_num_b")
        self.gridLayout_3.addWidget(self.spinBox_num_b, 0, 5, 1, 1)
        self.label_num_a = QtWidgets.QLabel(self.grpBoxSrvCall)
        self.label_num_a.setObjectName("label_num_a")
        self.gridLayout_3.addWidget(self.label_num_a, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(102, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.spinBox_num_a = QtWidgets.QSpinBox(self.grpBoxSrvCall)
        self.spinBox_num_a.setObjectName("spinBox_num_a")
        self.gridLayout_3.addWidget(self.spinBox_num_a, 0, 1, 1, 1)
        self.btn_call_add_two_ints_srv = QtWidgets.QPushButton(self.grpBoxSrvCall)
        self.btn_call_add_two_ints_srv.setObjectName("btn_call_add_two_ints_srv")
        self.gridLayout_3.addWidget(self.btn_call_add_two_ints_srv, 0, 6, 1, 1)
        self.label_num_b = QtWidgets.QLabel(self.grpBoxSrvCall)
        self.label_num_b.setObjectName("label_num_b")
        self.gridLayout_3.addWidget(self.label_num_b, 0, 4, 1, 1)
        self.label_result_srv_call = QtWidgets.QLabel(self.grpBoxSrvCall)
        self.label_result_srv_call.setObjectName("label_result_srv_call")
        self.gridLayout_3.addWidget(self.label_result_srv_call, 1, 0, 1, 1)
        self.label_result_add_two_ints = QtWidgets.QLabel(self.grpBoxSrvCall)
        self.label_result_add_two_ints.setObjectName("label_result_add_two_ints")
        self.gridLayout_3.addWidget(self.label_result_add_two_ints, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.grpBoxSrvCall, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple GUI ROS"))
        self.grbBoxTimerUpdateValues.setTitle(_translate("MainWindow", "Timer Update Values:"))
        self.label_state_x.setText(_translate("MainWindow", "X: "))
        self.robot_state_x.setText(_translate("MainWindow", " "))
        self.label_state_y.setText(_translate("MainWindow", "Y: "))
        self.robot_state_y.setText(_translate("MainWindow", " "))
        self.label_state_theta.setText(_translate("MainWindow", "theta"))
        self.robot_state_theta.setText(_translate("MainWindow", " "))
        self.grpBoxPubSub.setTitle(_translate("MainWindow", "Publisher and Subscriber:"))
        self.label_subscriber.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "I heard: "))
        self.btn_publisher.setText(_translate("MainWindow", "Publish"))
        self.grpBoxSrvCall.setTitle(_translate("MainWindow", "Service Request and Response:"))
        self.label_num_a.setText(_translate("MainWindow", "TextLabel"))
        self.btn_call_add_two_ints_srv.setText(_translate("MainWindow", "Add Two Ints"))
        self.label_num_b.setText(_translate("MainWindow", "TextLabel"))
        self.label_result_srv_call.setText(_translate("MainWindow", "Result:"))
        self.label_result_add_two_ints.setText(_translate("MainWindow", " "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
