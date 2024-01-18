# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Isaiah Abolarinde,Olurotimi Ajayi,Kial Leroux-Malone,Nitten Purewal"

# Update "" with your team (e.g. T102)
__team__ = "T-22"
#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(dic: list[dict], sort: str) -> list[dict]:
    """
    returns a list full of dictionaries in either ascending or descending order
    
    preconditions: sort == 'A' or 'D'
    
    >>> sort_students_age_bubble([{'Age': 12, 'School': 'GP'},{'Age': 8, 'School': 'AB'}], 'A')
    [{'Age': 12, 'School': 'GP'},{'Age': 8, 'School': 'AB'}]
    >>> sort_students_age_bubble([{'Age': 7, 'School': 'GP'},{'Age': 8, 'School': 'AB'}], 'D')
    [{'Age': 7, 'School': 'GP'},{'Age': 8, 'School': 'AB'}]
    >>> sort_students_age_bubble([{'School': 7, 'School': 'GP'},{'School': 8, 'School': 'AB'}], 'D')
    "Age" key is not present
    [{'School': 7, 'School': 'GP'},{'School': 8, 'School': 'AB'}]
    """
    if 'Age' not in dic[0]:
        print('"Age" is not present')
        return dic
     
    for i in range(len(dic)):
        for i in range(len(dic) - 1):
            if sort == 'A':
                if dic[i]['Age'] > dic[i + 1]['Age']:
                    temp = dic[i]
                    dic[i] = dic[i + 1]
                    dic[i + 1] = temp
            elif sort == 'D':
                if dic[i]['Age'] < dic[i + 1]['Age']:
                    temp = dic[i]
                    dic[i] = dic[i + 1]
                    dic[i + 1] = temp      
            
    return dic

#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(crown: list[dict], sortin: str) -> list[dict]:
    """ Return the sorted list if "Study Time" is a key in the dictionary, else
    print a message and return the original list

    >>>sort_students_time_selection ( [{"StudyTime":13.2,"School":"GP"},{"StudyTime":16.1,"School":"MS"}], "D")
    [{"StudyTime": 16.1, "School":"MS"}, {"StudyTime":13.2, "School":"GP"}]

    >>> sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]

    >>> sort_students_time_selection ( [{"StudyTime":6.2,"School":"GP"},{"StudyTime":11,"School":"MS"}], "A")
    [{'StudyTime': 6.2, 'School': 'GP'}, {'StudyTime': 11, 'School': 'MS'}]

    """
    if 'StudyTime' in crown[0].keys():
        for j in range(len(crown)):
            min_idx = j
            for k in range(j + 1, len(crown)):
                if crown[min_idx]['StudyTime'] > crown[k]['StudyTime']:
                    min_idx = k
                    crown[j], crown[min_idx] = crown[min_idx], crown[j]
        if sortin == 'D':
            crown.reverse()
            return crown
        else:
            return crown
    else:
        print('"StudyTime" key is not present')
        return crown

#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(dic:list[dict], order:str)->list[dict]:
    """
    Return a sorted list based on the average grade in either accending or decending order
    Precondtions: dic: a list of dictionaries order A for accending or D decending
    
    Examples: 
    
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}, {"G_Avg":8.6,"School":"GP"}], "A")
    [{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 8.6, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}]
    
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}, {"G_Avg":9.1,"School":"GP"}], "D")
    [{'G_Avg': 9.1, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}]
    
    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    G_Avg key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    """
    if 'G_Avg' in dic[0]:
        for i in range(1,len(dic)):
            key = dic[i]
            
            j = i-1
            
            while j >=0 and key['G_Avg'] < dic[j]['G_Avg']:
                dic[j+1] = dic[j]
                j-= 1
            dic[j+1] = key
    
        if order == 'A':
            dic
            return dic
        else:
            dic.reverse()
            return dic
    else: 
        print('"G_Avg key" is not present')
        return dic

#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(failures_list: list[dict], order: str) -> list[dict]:
    """ 
    Takes a specifed list of dictionaries and returns the list but sorted either ascending or descending order dependent on the input "A" or "D", if the key "Failures" is not present it will print that it is not present and return the originial list.

    Pre-conditions: order == "A" or order == "B"

    >>> sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{"Failures":19,"School":"MS"},{"Failures":10,"School":"GP"}]

    >>> sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "A")
    [{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}]

    >>> sort_students_failures_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "A")
    "Failures key is not present"

    """

    if "Failures" not in failures_list[0]:
        print('"Failures" key is not present')
        return failures_list

    switch = True
    while switch:
        switch = False
        for i in range(len(failures_list) - 1):
            if failures_list[i]["Failures"] > failures_list[i + 1]["Failures"]:

                temp = failures_list[i]["Failures"]
                failures_list[i]["Failures"] = failures_list[i + 1]["Failures"]
                failures_list[i + 1]["Failures"] = temp
                switch = True

    if order == "A":
        return failures_list

    elif order == "D":
        failures_list.reverse()
        return failures_list

    else:
        return "Please enter either A or D for ascending or descending order"
    
#==========================================#
# Place your sort function after this line
def sort_by_key(dic:list[dict], order:str, sort:str)->list[dict]:
    """
    Return a list of dictonaries sorted by the sort argument
    Preconditons: order A for accending or D decending
    
    Examples: 
    >>> sort_by_key([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{'School': 'GP'}, {'School': 'MS'}]
    
    >>> sort_by_key([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{'Age': 19.1, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
    
    >>> sort_by_key([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"A","Age")
    [{'Age': 10, 'School': 'GP'}, {'Age': 19.1, 'School': 'MS'}]
    """
    if sort == 'Age':
        return sort_students_age_bubble(dic,order)
    elif sort == 'StudyTime':
        return sort_students_time_selection(dic,order)
    elif sort == 'G_Avg':
        return sort_students_g_avg_insertion(dic,order) 
    elif sort == 'Failures':
        return sort_students_failures_bubble(dic,order)  
    else:
        print('Cannot be sorted by "'+ sort + '"')
        return dic


# Do NOT include a main script in your submission
