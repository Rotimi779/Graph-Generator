# ECOR 1042 Lab 3 - Team submission

# Remember to include docstring and type annotations for your functions



# Update "" to list all students contributing to the team work

__author__ = "Isaiah Abolarinde, Nitten Purewal, Rotimi Ajayi, Kial Leroux-Malone"



# Update "" with your team (e.g. T102)

__team__ = "T-22"



#==========================================#

# Place your student_school_list function after this line

def student_school_list(file: str,school:str)-> list[dict]:

    """

    Return a list containing a dictionary for each value. the dictionary should contain the Age,StudyTime,Failures,Health,Absences,G1,G2,G3 for each student

    Precondtions: file exists, School is in file

    Examples:

    

    >>> student_school_list('student-mat.csv', 'GP')

    [ {'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 }, {another element}, …]

    

    >>> student_school_list('student-mat.csv', 'CF')

    [{'age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12},  {another element}, …]

    

    >>> student_school_list('student-mat.csv', 'd')

    []

    """

    infile = open(file,'r')

    my_list = []

    

    for line in infile:

        line = line.replace("\n","").split(',')

        if line[0] == school:            

            my_list.append({'Age':int(line[1]), 'StudyTime': float(line[2]), 'Failures': int(line[3]), 'Health': int(line[4]),

                            'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8]) })

    infile.close()

    

    return my_list





#==========================================#

# Place your student_health_list function after this line

def student_health_list(file: str, health: int) -> list[dict]:

    """

    return the health of the students from the given 

    data



    preconditions: None

    

    >>> student_health_list('student-mat.csv', 2)

    [{'school': 'GP', 'age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9},  {another element}, ...]

    >>> student_health_list('student-mat.csv', 3)

    [{'school': 'GP', 'age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, ...]

    >>>student_health_list('student-mat.csv', 4)

    [{'school': 'GP', 'age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {another element}, ...]

    """

    infile = open(file, 'r')

    my_health_list = []



    for line in infile:

        line = line.replace("\n", "").split(',')

        if line[4] == str(health):

            my_health_list.append({"School": line[0], 'Age':int(line[1]), 'StudyTime': float(line[2]), 'Failures': int(line[3]),

                            'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8]) })

    infile.close()

    return my_health_list





#==========================================#

# Place your student_age_list function after this line



def student_age_list(file:str, age:int):

    """ 

    Return a list of students with the same age as the input parameter.



    Preconditions: age >= 0



    >>>  student_age_list('student-mat.csv', 15)

    [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6,

    'G1': 7, 'G2': 8, 'G3': 10}, {another element}, …]



    >>> student_age_list('student-mat.csv', 16)

    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 4, 

    'G1': 6, 'G2': 10, 'G3': 10}, {another element}, …]



    >>> student_age_list('student-mat.csv', 152)

    []



    """

    inline = open(file, 'r')

    my_list = []



    for line in inline:

        line = line.replace("\n", "").split(',')

        if str(age) == line[1]:

            my_list.append({'School': line[0], 'StudyTime': float(line[2]), 'Failures': int(line[3]), 'Health': int(line[4]),

                            'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8]) })

    inline.close()

    return my_list





#==========================================#

# Place your student_failures_list function after this line

def student_failures_list(file:str, failures:int):

    """

    Return a list of students with the same number of failures as the input parameter.

    Preconditions: file exist, failures value is in document

    

    Example

    >>> student_failures_list('student-mat.csv',0)

    [{'School': 'GP', 'age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, …]

    

    >>> student_failures_list('student-mat.csv',3)

    [{'School': 'GP', 'age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, …]

    

    """

    inline = open(file, 'r')

    my_list = []



    for line in inline:

        line = line.replace("\n", "").split(',')

        if str(failures) == line[3]:

            my_list.append({'School': line[0], 'Age':int(line[1]), 'StudyTime': float(line[2]),'Health': int(line[4]),

                            'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8]) })

    inline.close()

    return my_list





#==========================================#

# Place your load_data function after this line

def load_data(file:str ,attribute_tuple: tuple)-> list[dict]:

    """

    Return a list containing a dictionary for each value in the file based on sorting specifications, specify which column to look through with the first entry in the tuple then 

    how you'd like to sort through that column with second entry in the tuple. to see all type 'All'

    

    Preconditions: file is a file, attribute_tuple contains 2 items

    

    Examples: 

    >>> load_data('student-mat.csv',('School','CF'))

    [{'age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12},  {another element}, …]

    

    >>> load_data('student-mat.csv',('G1','10'))

    Invalid Value

    []

    

    >>> load_data('student-mat.csv',('All','0'))

    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, …]

    """

    

    if attribute_tuple[0] == 'School':

        ans = student_school_list(file, attribute_tuple[1])

    elif attribute_tuple[0] == 'Health':

        ans = student_health_list(file, attribute_tuple[1])

    elif attribute_tuple[0] == 'Failures':

        ans = student_failures_list(file, attribute_tuple[1])

    elif attribute_tuple[0] == 'Age':

        ans = student_age_list(file, attribute_tuple[1])    

    elif attribute_tuple[0] == 'All':

        infile = open(file,'r')

        my_list = []

        

        for line in infile:

            if "School" in line:

                continue

            

            line = line.replace("\n","").split(',')

            my_list.append({'School': line[0],'Age':int(line[1]), 'StudyTime': float(line[2]), 'Failures': int(line[3]), 'Health': int(line[4]),

                            'Absences': int(line[5]), 'G1': int(line[6]), 'G2': int(line[7]), 'G3': int(line[8]) })

        

        return my_list        

        

    else:

        print("Invalid Value")

        return []

    return ans



#==========================================#

# Place your add_average function after this line

def add_average(student_list: list[dict])->list[dict]:

    """

    Returns a list of dictionaries where a new key and value is added to each dictionary, the key is 'g_Avg' and represnts the average of the other three grades in each dictionary

    Preconditions: student list is a list containing dictionaries

    Examples:

    

    >>> add_average(load_data('student-mat.csv',('All',0)))

    [{'school': 'GP', 'age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {another element}, ...]

    

    >>> add_average(load_data('student-mat.csv',('Health',2)))

    [{'school': 'GP', 'age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_Avg': 9.0}, {another element}, ...]

    

    """

    

    for i in student_list:

        i['G_Avg'] = round((int(i['G1'])+ int(i['G2'])+ int(i['G3']))/3,2)

    return student_list









# Do NOT include a main script in your submission

