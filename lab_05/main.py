#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *


def lock(points_list, canvas_class, list_box):
    if len(points_list[-1]) > 1:
        start = points_list[-1][0]
        stop = points_list[-1][-1]
        canvas_class.canvas.create_line(round(start[0]), round(start[1]), round(
            stop[0]), round(stop[1]), width=1, fill="black")

        points_list.append(list())
        list_box.insert(END, "_"*8)


def fill(canvas_class):
    pass


def delayed_fill(canvas_class):
    pass


def add_point(points_list, point, canvas_class, list_box):
    if point in points_list[-1]:
        print_error("Такая точка уже имеется в данном многоугольнике!")
        return
    points_list[-1].append(point)

    list_box.insert(END, point)

    # print(points_list[-1])

    if len(points_list[-1]) > 1:
        start = points_list[-1][-1]
        stop = points_list[-1][-2]
        canvas_class.canvas.create_line(round(start[0]), round(start[1]), round(
            stop[0]), round(stop[1]), width=1, fill="black")
    elif len(points_list[-1]) == 1:
        canvas_class.print_pixel(points_list[-1][0][0], points_list[-1][0][1])


def add_point_click(event, canvas_class, list_box, points_list):
    add_point(points_list, [event.x, event.y], canvas_class, list_box)


def add_point_entry(point_coordinates, list_box, canvas_class, points_list):
    point = list(get_two_answer(point_coordinates.get()))
    if point[0] == FALSE:
        return
    add_point(points_list, point, canvas_class, list_box)


def clear(canvas_class, list_box, points_list):
    canvas_class.clear_all()

    list_box.delete(1, list_box.size())

    for i in range(len(points_list) - 1, -1, -1):
        del points_list[i]

    points_list.append([])
    # print(points_list)


def main():
    root = Tk()
    points_list = [[]]
    # Лабораторная работа №5.
    settings_interface(root, "1200x800", "Растровое заполнение областей")

    canvas_class = paint_class(root)
    list_box = create_list_box(root, [800, 325])

    create_button("Выбрать цвет заполнения",
                  canvas_class.choose_color_line, [1000, 25])
    # create_button("Заполнять фоновым цветом",
    #   canvas_class.draw_color_background, [1000, 60])

    create_label(root, "Координаты точки:", [1000, 100])
    entry_point_coordinates = create_entry(root, [1000, 125])

    create_button("Добавить точку", lambda arg1=entry_point_coordinates, arg2=list_box, arg3=canvas_class,
                  arg4=points_list: add_point_entry(arg1, arg2, arg3, arg4), [1000, 165])

    create_button("Замкнуть", lambda arg1=points_list,
                  arg2=canvas_class, arg3=list_box: lock(arg1, arg2, arg3), [1000, 200])

    create_button(
        "Заполнить", lambda arg1=canvas_class: fill(arg1), [1000, 675])

    create_button(
        "Заполнить с задержкой", lambda arg1=canvas_class: delayed_fill(arg1), [1000, 725])

    create_button("Стереть всё", lambda arg1=canvas_class, arg2=list_box, arg3=points_list:
                  clear(arg1, arg2, arg3), [1000, 775])
    canvas_class.canvas.bind('<Button-1>', lambda event,
                             arg1=canvas_class, arg2=list_box, arg3=points_list: add_point_click(event, arg1, arg2, arg3))

    root.mainloop()


if __name__ == "__main__":
    main()
