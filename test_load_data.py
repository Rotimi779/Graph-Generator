# ECOR 1042 Lab 4 - team submission

import check

import load_data


# Update "" with your the name of the active members of the team
__author__ = "Isaiah Abolarinde, Nitten Purewal, Rotimi Ajayi, Kial Leroux-Malone"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-22"

#==========================================#

# Place test_return_list function here


def test_return_list():

    # Complete the function with your test cases

    check.equal(type(load_data.student_school_list(
        'student-mat.csv', 'GP')), type(list()))

    check.equal(type(load_data.student_school_list(
        'student-mat.csv', 'S')), type(list()))

    check.equal(type(load_data.student_school_list(
        'student-mat.csv', 'CF')), type(list()))

    # test that student_age_list returns a list (3 different test cases required)

    # Complete the function with your test cases

    check.equal(type(load_data.student_age_list(
        'student-mat.csv', 18)), type(list()))

    check.equal(type(load_data.student_age_list(
        'student-mat.csv', 13)), type(list()))

    check.equal(type(load_data.student_age_list(
        'student-mat.csv', 15)), type(list()))

    # Complete the function with your test cases

    check.equal(type(load_data.student_health_list(
        'student-mat.csv', 2)), type(list()))

    check.equal(type(load_data.student_health_list(
        'student-mat.csv', -1)), type(list()))

    check.equal(type(load_data.student_health_list(
        'student-mat.csv', 3)), type(list()))

    # Complete the function with your test cases

    check.equal(type(load_data.student_failures_list(
        'student-mat.csv', 2)), type(list()))

    check.equal(type(load_data.student_failures_list(
        'student-mat.csv', 1)), type(list()))

    check.equal(type(load_data.student_failures_list(
        'student-mat.csv', 0)), type(list()))

    # Complete the function with your test cases

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('School', 'CF'))), type(list()))

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('Failures', 5))), type(list()))

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('Age', 15))), type(list()))

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('Absences', 3))), type(list()))

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('StudyTime', 2.0))), type(list()))

    check.equal(type(load_data.load_data(
        'student-mat.csv', ('G1', 10))), type(list()))

    # Complete the function with your test cases

    check.equal(type(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), type(list()))

    check.equal(type(load_data.add_average([{'School': 'MB', 'Age': '15', 'StudyTime': '2',
                'Failures': '0', 'Health': '2', 'Absences': '26', 'G1': '7', 'G2': '6', 'G3': '6'}])), type(list()))

    check.equal(type(load_data.add_average([{'school': 'MB', 'Age': '15', 'StudyTime': '2',
                'Failures': '0', 'Health': '2', 'Absences': '26', 'G1': '7', 'G2': '6', 'G3': '6'}])), type(list()))

    check.summary()


# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_school_list('student-mat.csv', 'GP')), 3)
    check.equal(len(load_data.student_school_list('student-mat.csv', 'MB')), 2)
    check.equal(len(load_data.student_school_list('student-mat.csv', 'MS')), 4)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list("student-mat.csv", 18)), 4)
    check.equal(len(load_data.student_age_list("student-mat.csv", 17)), 6)
    check.equal(len(load_data.student_age_list("student-mat.csv", 15)), 3)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list("student-mat.csv", 3)), 8)
    check.equal(len(load_data.student_health_list("student-mat.csv", 5)), 3)
    check.equal(len(load_data.student_health_list("student-mat.csv", 4)), 3)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(len(load_data.student_failures_list("student-mat.csv", 3)), 1)
    check.equal(len(load_data.student_failures_list("student-mat.csv", 0)), 11)
    check.equal(len(load_data.student_failures_list("student-mat.csv", 2)), 2)

    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data("student-mat.csv", ("School", "A"))), 0)
    check.equal(len(load_data.load_data("student-mat.csv", ("School", "GP"))), 3)
    check.equal(len(load_data.load_data("student-mat.csv", ("Health", "3"))), 8)
    check.equal(len(load_data.load_data("student-mat.csv", ("Failures", "1"))), 1)
    check.equal(len(load_data.load_data("student-mat.csv", ("Age", "15"))), 3)
    check.equal(len(load_data.load_data("student-mat.csv", ("All", "1"))), 15)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), 1)
    check.equal(len(load_data.add_average([])), 0)
    check.equal(len(load_data.add_average([{'school': 'MB', 'age': '15', 'StudyTime': '2', 'Failures': '0', 'Health': '2', 'Absences': '26', 'G1': '7', 'G2': '6', 'G3': '6'},
                                 {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), 2)

    check.summary()


# Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():

    # Complete the function with your test cases

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)

    # test case 1

    x = load_data.student_school_list('student-mat.csv', 'CF')

    check.equal(list(x[0].values()), [15, 5, 2, 3, 6, 5, 9, 7], '')

    # test case 2

    x = load_data.student_school_list('student-mat.csv', 'CF')

    check.equal(list(x[len(x) - 1].values()), [17, 1, 2, 5, 0, 7, 6, 0], '')

    # test case 3

    x = load_data.student_school_list('student-mat.csv', 'GP')

    check.equal(list(x[len(x) - 1].values()),
                [15, 2, 3, 3, 10, 7, 8, 10], '')

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    # test case 1

    x = load_data.student_age_list('student-mat.csv', 18)

    check.equal(list(x[0].values()), ['GP', 2, 0, 3, 6, 5, 6, 6], '')

    # test case 2

    x = load_data.student_age_list('student-mat.csv', 18)

    check.equal(list(x[len(x) - 1].values()),
                ['MS', 3.0, 0, 5, 2, 9, 8, 8], '')

    # test case 3

    x = load_data.student_age_list('student-mat.csv', '15')

    check.equal(list(x[0].values()), ['GP', 2, 3, 3, 10, 7, 8, 10], '')

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)

    # test case 1

    x = load_data.student_health_list('student-mat.csv', 3)

    check.equal(list(x[0].values()), ['GP', 18, 2.0, 0, 6, 5, 6, 6], '')

    # test case 2

    x = load_data.student_health_list('student-mat.csv', 3)

    check.equal(list(x[len(x) - 1].values()),
                ['BD', 18, 3.0, 0, 1, 13, 12, 12], '')

    # test case 3

    x = load_data.student_health_list('student-mat.csv', 1)

    check.equal(list(x[0].values()), ['MS', 17, 3.0, 0, 7, 10, 9, 9], '')

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)

    # test case 1

    x = load_data.student_failures_list('student-mat.csv', 3)

    check.equal(list(x[0].values()), ['GP', 15, 2.0, 3, 10, 7, 8, 10], '')

    # test case 2

    x = load_data.student_failures_list('student-mat.csv', 3)

    check.equal(list(x[len(x) - 1].values()),
                ['GP', 15, 2.0, 3, 10, 7, 8, 10], '')

    # test case 3

    x = load_data.student_failures_list('student-mat.csv', 1)

    check.equal(list(x[0].values()), ['CF', 16, 2.0, 5, 4, 10, 12, 12], '')

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)

    x = load_data.load_data('student-mat.csv', ('All', 0))

    check.equal(list(x[0].values()), ['GP', 18, 2.0, 0, 3, 6, 5, 6, 6], '')

    check.equal(list(x[len(x) - 1].values()),
                ['MS', 18, 3.0, 0, 5, 2, 9, 8, 8], '')

    x = load_data.load_data('student-mat.csv', ('School', 'GP'))

    check.equal(list(x[0].values()), [18, 2.0, 0, 3, 6, 5, 6, 6], '')

    check.equal(list(x[len(x) - 1].values()),
                [15, 2.0, 3, 3, 10, 7, 8, 10], '')

    x = load_data.load_data('student-mat.csv', ('Health', 3))

    check.equal(list(x[0].values()), ['GP', 18, 2.0, 0, 6, 5, 6, 6], '')

    check.equal(list(x[len(x) - 1].values()),
                ['BD', 18, 3.0, 0, 1, 13, 12, 12], '')

    # test that add_average returns a correct dictionary inside the list  (3 different test cases required)

    x = load_data.add_average(
        load_data.load_data('student-mat.csv', ('All', 0)))

    check.equal(list(x[0].values()), [
                'GP', 18, 2.0, 0, 3, 6, 5, 6, 6, 5.67], '')

    check.equal(list(x[len(x) - 1].values()),
                ['MS', 18, 3.0, 0, 5, 2, 9, 8, 8, 8.33], '')

    x = load_data.add_average(load_data.load_data(
        'student-mat.csv', ('School', 'GP')))

    check.equal(list(x[len(x) - 1].values()),
                [15, 2.0, 3, 3, 10, 7, 8, 10, 8.33], '')

    check.summary()


# Place test_add_average function here
def test_add_average():

    # Four cases for 'age' is not a key of the dict

    check.equal(load_data.add_average(
        load_data.student_age_list('student-mat.csv', 1859)), [])

    check.equal(len((load_data.add_average(load_data.student_age_list('student-mat.csv', 15))
                [0])), len((load_data.student_age_list('student-mat.csv', 15))[0]) + 1)

    check.equal(
        len(load_data.add_average(load_data.student_age_list('student-mat.csv', 15))), len(load_data.student_age_list('student-mat.csv', 15)))

    check.equal(load_data.add_average(load_data.student_age_list('student-mat.csv', 15))[0]['G_Avg'], round(((int(load_data.add_average(load_data.student_age_list('student-mat.csv', 15))[0]['G1']) + int(
        load_data.add_average(load_data.student_age_list('student-mat.csv', 15))[0]['G2']) + int(load_data.add_average(load_data.student_age_list('student-mat.csv', 15))[0]['G3']))) / 3, 2))

    # Four cases for 'school' is not a key of the dict

    check.equal(load_data.add_average(
        load_data.student_school_list('student-mat.csv', 'HB')), [])

    check.equal(len((load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))
                [0])), len((load_data.student_school_list('student-mat.csv', 'GP'))[0]) + 1)

    check.equal(
        len(load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))), len(load_data.student_school_list('student-mat.csv', 'GP')))

    check.equal(load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))[0]['G_Avg'], round(((int(load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))[0]['G1']) + int(
        load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))[0]['G2']) + int(load_data.add_average(load_data.student_school_list('student-mat.csv', 'GP'))[0]['G3']))) / 3, 2))

    # Four cases for 'health' is not a key of the dict

    check.equal(load_data.add_average(
        load_data.student_health_list('student-mat.csv', 2123)), [])

    check.equal(len(load_data.add_average(load_data.student_health_list('student-mat.csv', 3))
                [0]), len((load_data.student_health_list('student-mat.csv', 3))[0]) + 1)

    check.equal(
        len(load_data.add_average(load_data.student_health_list('student-mat.csv', 2))), len(load_data.student_health_list('student-mat.csv', 2)))

    check.equal(load_data.add_average(load_data.student_health_list('student-mat.csv', 3))[0]['G_Avg'], round(((int(load_data.add_average(load_data.student_health_list('student-mat.csv', 3))[0]['G1']) + int(
        load_data.add_average(load_data.student_health_list('student-mat.csv', 3))[0]['G2']) + int(load_data.add_average(load_data.student_health_list('student-mat.csv', 3))[0]['G3']))) / 3, 2))

    # Four cases for 'failures' is not a key of the dict

    check.equal(load_data.add_average(
        load_data.student_failures_list('student-mat.csv', 128947)), [])

    check.equal(len((load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))
                [0])), len((load_data.student_failures_list('student-mat.csv', 0))[0]) + 1)

    check.equal(
        len(load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))), len(load_data.student_failures_list('student-mat.csv', 0)))

    check.equal(load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))[0]['G_Avg'], round(((int(load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))[0]['G1']) + int(
        load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))[0]['G2']) + int(load_data.add_average(load_data.student_failures_list('student-mat.csv', 0))[0]['G3']))) / 3, 2))

    check.summary()


# Do NOT include a main script in your submission
