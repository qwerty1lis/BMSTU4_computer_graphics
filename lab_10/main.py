#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *
from solution import *


def main():
    root = Tk()

    settings_interface(root, "1200x800", "Лабораторная работа №10")

    canvas_class = paint_class(root)

    choice_func = option_menu(root, CHOICE, [1000, 30])

    create_label(root, "Пределы по x:", [1000, 100])
    borders_x = create_entry(root, [1000, 125])

    create_label(root, "Шаг по x:", [1000, 150])
    step_x = create_entry(root, [1000, 175])

    create_label(root, "Пределы по z:", [1000, 225])
    borders_z = create_entry(root, [1000, 250])

    create_label(root, "Шаг по z:", [1000, 275])
    step_z = create_entry(root, [1000, 300])

    # create_button("Отобразить", lambda arg1=canvas_class, arg2=cutter, arg3=contour:
    #               SolutionWrapper(arg1, arg2, arg3), [1000, 700])
    create_button(
        "Отобразить", lambda arg1=choice_func, arg2=[borders_x, borders_z], arg3=[step_x, step_z], arg4=canvas_class:  SolutionWrapper(arg1, arg2, arg3, arg4), [1000, 700])

    root.mainloop()


if __name__ == "__main__":
    main()