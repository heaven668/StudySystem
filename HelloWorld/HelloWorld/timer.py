# -*- coding: utf-8 -*-
from threading import Timer
from CheckTransactions import *


def printHello():
    checkall(request)
    checkstudentinfo(_uid)
    checkmanagerinfo(_uid)
    checkteacherinfo(_uid)
    checkcourseinfo(_uid)
    checkmark(_uid)
    checkselectcourse(_uid)
    formattercourseinfo(_grade, _term, _composition)
    t = Timer(5, printHello)
    t.start()
if __name__ == "__main__":
    printHello()
