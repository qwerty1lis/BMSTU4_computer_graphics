import numpy as np
from functions_answer import int_answer, get_two_answer
from interface import print_error
from functions import *
from constants import *


def f(x):
    return sin(x)

# def f(x, z):
#     # return x * z * x
#     return x**2 / 20 + z**2 / 20
#     return 10 * (cos(x) * sin(z))


def float_horizon(borders_x, step_x, borders_z, step_z, canvas_class):
    # Инициализируем начальными значениями массивы горизонтов.
    # x = [0] * 10  # [0,0,...,0]
    top = {x: 0 for x in range(1, WIDTH)}  # Верхний.
    bottom = {x: HEIGHT for x in range(1, HEIGHT)}  # Нижний.

    x_start = -10
    x_stop = 10
    x_step = 0.5
    for x in np.arange(x_start, x_stop + x_step, x_step):
        x_next = x + x_step
        canvas_class.draw_line([x, f(x)],
                               [x_next, f(x_next)])

    # z = 1
    # x_start = -2
    # x_stop = 2
    # x_step = 0.1
    # for x in np.arange(x_start, x_stop + x_step, x_step):
    #     x_next = x + x_step + 0.1
    #     print(x, f(x, z))
    #     canvas_class.draw_line([x, f(x, z)], [x_next, f(x_next, z)])


def SolutionWrapper(choice, borders, step, canvas_class):
    # borders_x = get_two_answer(borders[0].get())
    # if borders_x[0] == FALSE:
    #     return

    # step_x = int_answer(step[0].get())
    # if not step_x:
    #     return

    # borders_z = get_two_answer(borders[1].get())
    # if borders_z[0] == FALSE:
    #     return

    # step_z = int_answer(step[1].get())
    # if not step_z:
    #     return

    index = CHOICE.index(choice.get())

    # print("borders_x = ", borders_x, "\nborders_z = ", borders_z)
    # print("step_x = ", step_x, "\nstep_z = ", step_z)
    # print("choice = ", index, " = ", choice.get())

    borders_x, step_x = [-5, 5], 1
    borders_z, step_z = [-5, 5], 1

    float_horizon(borders_x, step_x, borders_z, step_z, canvas_class)