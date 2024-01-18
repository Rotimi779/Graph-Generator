# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Isaiah Abolarinde"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101266083"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-22"

#==========================================#
import matplotlib.pyplot as plt
import numpy as np

# Place your curve_fit function after this line


def curve_fit(dic: list[dict], attribute: str, deg: int) -> str:
    """
    Return the equation of a plot based on the y-Axis being G_Avg and the x-axis being whichever attribute the user inputs.
    Preconditions: attribute, be a key in the list of dictonaries, deg: 1-5

    Examples: 
    >>> curve_fit([{'G_Avg':2, 'health':1},{'G_Avg':5, 'health':2},{'G_Avg':10, 'health':3}],'health',2)
    'y = +1.0x^2 -0.0x +1.0'

    >>> curve_fit([{'G_Avg':2, 'health':1},{'G_Avg':5, 'health':2},{'G_Avg':10, 'health':3}],'health',1)
    'y = +4.0x -2.33'

    >>> curve_fit([{'G_Avg':1, 'health':1},{'G_Avg':8, 'health':2},{'G_Avg':27, 'health':3},{'G_Avg':5, 'health':3}],'health',2)
    'y = +0.5x^2 +5.5x -5.0'

    """
    main_dic = {}

    string = 'y = '
    # input attribute into dict as keys because they cannot be duplicated then make a list of every 'G_Avg' assoiated with thet attribute
    for i in range(len(dic)):
        if dic[i][attribute] in main_dic:
            main_dic[dic[i][attribute]] += [dic[i]['G_Avg']]
        else:
            main_dic[dic[i][attribute]] = [dic[i]['G_Avg']]

    # reasign the attribute key to the calcuated average of the list of 'G_Avg'
    for i in main_dic:
        temp = 0
        count = 0
        for j in range(len(main_dic[i])):
            temp += main_dic[i][j]
            count += 1
        main_dic[i] = temp / count

    x = list(main_dic.keys())
    y = list(main_dic.values())

    # if degree is more then the number of points -1 change degree to number of points and use interpolation
    if deg > len(x) - 1:
        deg = len(x) - 1
        coef = np.polyfit(x, y, deg)
    else:
        coef = np.polyfit(x, y, deg)              # get
        x_e = np.linspace(min(x), max(x), 100)
        y_e = np.polyval(coef, x_e)
        coef = np.polyfit(x_e, y_e, deg)

    # formatting word
    j = len(coef) - 1
    for i in range(len(coef)):
        if j == 0:
            if coef[i] < 0:
                string += str(round(coef[i], 2))
            else:
                string += '+' + str(round(coef[i], 2))
            break
        if j == 1:
            if coef[i] < 0:
                string += str(round(coef[i], 2)) + 'x '
            else:
                string += '+' + str(round(coef[i], 2)) + 'x '
            j -= 1
            continue
        if coef[i] < 0:
            string += str(coef[i]) + f'x^{j} '
        else:
            string += '+' + str(round(coef[i], 2)) + f'x^{j} '
        j -= 1

    return string

# Do NOT include a main script in your submission
