# This Python file uses the following encoding: utf-8
import sys
import os
import urllib, json
import PySide2.QtQml
from OpenGL import GL
from PySide2.QtQuick import QQuickView
from PySide2.QtGui import QGuiApplication, QStringListModel, Qt
from PySide2.QtQml import QQmlApplicationEngine, QStringListModel


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
